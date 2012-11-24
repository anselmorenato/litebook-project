#!/usr/bin/python
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------
# Name:        KPUB
# Purpose:     publish all books in the specified dir via KADP
#
# Author:      Hu Jun
#
# Created:     17/08/2012
# Copyright:   (c) Hu Jun 2012
# Licence:     GPLv3
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import os
import sys
import re
import xmlrpclib
import zipfile

import hashlib
import traceback
import time
import struct
import cPickle
import threading
import platform
import logging
import longbin
import base64
myos=platform.architecture()
ros = platform.system()
if myos[1]=='ELF' and ros == 'Linux':
    if myos[0]=='64bit':
        from lxml_linux_64 import etree
    elif myos[0]=='32bit':
        from lxml_linux import etree
else:
    from lxml import etree

if ros !='Windows':
    from pymmseg import mmseg
else:
    from pymmseg_win import mmseg

import urllib

def cur_file_dir():
    #获取脚本路径
    global myos
    if myos == 'Linux':
        path = sys.path[0]
    elif myos == 'Windows':
        return os.path.dirname(AnyToUnicode(os.path.abspath(sys.argv[0])))
    else:
        if sys.argv[0].find('/') != -1:
            path = sys.argv[0]
        else:
            path = sys.path[0]
    if isinstance(path,str):
        path=path.decode('utf-8')

    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def getEPUBMeta(ifile):
    """
    return a dict of epub meta data
    ifile is the path to the epub file
    """
    try:
        zfile = zipfile.ZipFile(ifile,'r')
    except:
        return False
    container_xml = zfile.open('META-INF/container.xml')
    context = etree.iterparse(container_xml)
    opfpath='OPS/content.opf'
    for action, elem in context:
        if elem.tag[-8:].lower()=='rootfile':
            try:
                opfpath=elem.attrib['full-path']
            except:
                break
            break
    opf_file = zfile.open(opfpath)
    context = etree.iterparse(opf_file)
    meta_list={}
    for action, elem in context:
        if elem.tag.split('}')[0][1:].lower()=='http://purl.org/dc/elements/1.1/':
            meta_list[elem.tag.split('}')[-1:][0]]=elem.text
    return meta_list

class KPUB(threading.Thread):
    def __init__(self,ipath,rloc_base_url=u'http://SELF:8000/',kcurl='http://127.0.0.1:50201/'):
        """
        ipath is a unicode, represent the share_root
        rloc_base_url is the base URL of resouce location, should be unicode
        kcurl is the XMLRPC URL of the KADP
        """
        threading.Thread.__init__(self)
        # create logger
        self.lifetime=60*60*24*3 #3 day lifetime
        self.SALT = 'DKUYUPUB'
        self.running = True

        self.logger = logging.getLogger("KPUB")
        self.logger.setLevel(logging.DEBUG)

        # create console log handler

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = \
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s'
                              )
        ch.setFormatter(formatter)

        # add console handler to logger, multiple handler could be added to same logger

        self.logger.addHandler(ch)
        self.logger.disabled = True

        self.states={}#this is a dict used to save pub states

        if os.path.isdir(ipath) != True:
            raise ValueError('Invalid Path:'+ipath)
        else:
            self.root=os.path.abspath(ipath)
        self.rloc_base=unicode(rloc_base_url).encode('utf-8')
        self.kserver=xmlrpclib.Server(kcurl)




        #load saved states



##        rid,
##        data,
##        rtype=1,
##        rloc=None,
##        metadata={},
##        owner_id='SELF',
##        ctime=None


    def saveStates(self):
        fname = self.root+os.sep+'.kpub.states'
        savef = open(fname, 'wb')
        saves = cPickle.dumps(self.states, 2)
        saves = struct.pack('f',time.time()) + saves
        m = hashlib.sha224()
        m.update(saves+self.SALT)
        savef.write(m.digest()+saves) #use sha224 to hash
        savef.close()


    def loadStates(self):
        fname = self.root+os.sep+'.kpub.states'
        if not os.path.exists(fname):
            self.logger.warning('saved states not found')
            return False
        try:
            savef = open(fname, 'rb')
            loads = savef.read()
            m = hashlib.sha224()
            m.update(loads[28:]+self.SALT)
            if m.digest() != loads[:28]:
                return False
            if time.time() - (struct.unpack('f',loads[28:32])[0]) > self.lifetime:
                return False
            self.states = cPickle.loads(loads[32:])
            savef.close()
        except Exception, inst:
            self.logger.error("loadStates failed\n")
            self.logger.error(str(inst))
            return False
        return True


    def pubBook(self,bookpath):
        """
        Publish a book via KADP
        bpath is the full path to the book
        """
        bpath=os.path.abspath(bookpath)
        if os.path.isfile(bpath) == False:
            return False
        meta_list={}
        if os.path.splitext(bpath)[1].lower()=='.epub':
            meta_list=getEPUBMeta(bpath)
        else:
            meta_list['size']=os.stat(bpath).st_size
        for k,v in meta_list.items():
            if v == None:
                meta_list[k]=''
        inf=open(bpath,'rb')
        m = hashlib.sha1()
        m.update(inf.read())
        rid=m.digest()
        #rid = longbin.LongBin(rid)

        inf.close()
        data=os.path.basename(bpath)
        #data=KADP.AnyToUnicode(data)
        if isinstance(data,str):
            data=data.decode('utf-8')
        try:
            rlpath=os.path.relpath(bpath,self.root)
        except Exception, inst:
            self.logger.error('pubBook:'+traceback.format_exc())
            self.logger.error('pubBook: catched exception: '
                         + str(inst))
            return False

        if rlpath[:2]=='..':
            return False
        if isinstance(rlpath,unicode):
            rlpath=rlpath.encode('utf-8')
        rlpath=urllib.quote(rlpath)
        #check if the resource has been published within last lifetime
        if rid in self.states:
            if self.states[rid]['relpath']==rlpath:
                if time.time()-self.states[rid]['lastpub']<=self.lifetime:
                    return False
            else:
                if os.path.exists(self.states[rid]['bookpath']):
                    return False
        rloc=self.rloc_base+rlpath
        rtype=1
        #kres = KADP.KADRes(rid,data,rtype,rloc,meta_list)
        fname=os.path.splitext(data)[0]
        if os.path.splitext(bpath)[1].lower()=='.epub':
            if 'title' in meta_list:
                fname=meta_list['title']
        if not isinstance(fname,unicode):
            fname=fname.decode('utf-8')
        fname=fname.encode('utf-8')
        kw_list = mmseg.Algorithm(fname)
        klist = []
        p = re.compile('^\d+$')
        for tok in kw_list:
            kw = tok.text.decode('utf-8')
            if len(kw)<2:continue
            if p.search(kw) != None:continue
            klist.append(tok.text.decode('utf-8'))
        if not fname.decode('utf-8') in klist:
            klist.append(fname.decode('utf-8'))

        if klist != []:
            try:
                self.logger.debug(u'pubBook: publishing '+data+u' with keywords: '+u' '.join(klist))
                self.kserver.publishRes(klist,base64.b16encode(rid),data,rtype,rloc,meta_list,'SELF')
            except Exception, inst:
                self.logger.error('pubBook:'+traceback.format_exc())
                self.logger.error('pubBook: catched exception: '
                             + str(inst))
                return False
        self.states[rid]={'relpath':rlpath,'lastpub':time.time(),'bookpath':bookpath}
        return True


    def getNovelFileList(self):
        """
        return a list of file with following suffix:
            txt/html/htm/epub/umd/jar/zip/rar
        following files will be excluded:
            - filesize smaller than 256KB
            -
        """
        ext_list=['txt','html','htm','epub','umd','jar','zip','rar']
        rlist=[]
        #p = re.compile('^[0-9_]+$')
        for root,dirs,files in os.walk(self.root):
            for fname in files:
                if os.path.splitext(fname)[1].lower()[1:] in ext_list:
                    #if p.match(os.path.splitext(fname)[0]) == None:
                    fpath=os.path.join(root,fname)
                    if os.stat(fpath).st_size>=256000: # this is to avoid publishing small file
                        rlist.append(fpath)
        return rlist

    def run(self):
        mmseg.dict_load_chars(cur_file_dir()+os.sep+'chars.dic')
        mmseg.dict_load_words(cur_file_dir()+os.sep+'booknames.dic')
        self.loadStates()
        while self.running == True:
            flist=self.getNovelFileList()
            for book in flist:
                self.pubBook(book)
                if self.running == False:
                    self.saveStates()
                    return
                time.sleep(3)
            time.sleep(60)
            self.saveStates()
        return

    def stop(self):
        self.running=False




if __name__ == '__main__':

    import signal
    def signal_handler(signal, frame):
        global kp
        print 'You pressed Ctrl+C!'
        kp.stop()
    signal.signal(signal.SIGINT, signal_handler)
    kurl='http://127.0.0.1:50201'
    if len(sys.argv)<2:
        print "kpub <ctrl_url>"
    else:
        kurl='http://' + sys.argv[1] + ':50201'
    if ros=='Linux':
        kp = KPUB('/root/book',kcurl=kurl)
    else:
        kp = KPUB(u'd:\\book')
    kp.start()
    print "starting..."
