#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# LiteBook Plugin for www.xsxs520.com
#  - support multi-thread download(default 10 threads)
#  - minimal length of search keyword is 2, otherwise, litebook will just return white page


import urllib2
import urllib
import re
import math
import sys
import time
import wx
import thread
import threading
from HTMLParser import HTMLParser


base_url="http://www.xsxs520.com/"
search_url="http://www.xsxs520.com/modules/article/search.php"
tlock=thread.allocate_lock()
Description=u"""支持的网站: http://www.xsxs520.com/
插件版本：2.0
发布时间: 2010-5-1
简介：
    - 支持多线程下载
    - 最短搜索关键字为两个汉字
    - 支持HTTP代理
作者：litebook.author@gmail.com
"""

def isfull(l):
    xx=0
    n=len(l)
    while xx<n:
        if l[xx]==-1: return False
        xx+=1
    return True

def htmname2uni(htm):
    if htm[1]=='#':
        try:
            uc=unichr(int(htm[2:-1]))
            return uc
        except:
            return htm
    else:
        try:
            uc=unichr(htmlentitydefs.name2codepoint[htm[1:-1]])
            return uc
        except:
            return htm

def htm2txt(inf):
    """ filter out all html tags/JS script in input string, return a clean string"""
    f_str=inf
    #conver <p> to "\n"
    p=re.compile('<\s*p\s*>',re.I)
    f_str=p.sub('\n',f_str)


    #conver <br> to "\n"
    p=re.compile('<br.*?>',re.I)
    f_str=p.sub('\n',f_str)

    #conver "\n\r" to "\n"
    p=re.compile('\n\r',re.S)
    f_str=p.sub('\n',f_str)

    #this is used to remove protection of http://www.jjwxc.net
    p=re.compile('<font color=.*?>.*?</font>',re.I|re.S)
    f_str=p.sub('',f_str)

    #this is used to remove protection of HJSM
    p=re.compile("<\s*span\s*class='transparent'\s*>.*?<\s*/span\s*>",re.I|re.S)
    f_str=p.sub('',f_str)

    #remove <script xxxx>xxxx</script>
    p=re.compile('<script.*?>.*?</script>',re.I|re.S)
    f_str=p.sub('',f_str)

    #remove <style></style>
    p=re.compile('<style>.*?</style>',re.I|re.S)
    f_str=p.sub('',f_str)

    #remove <option>
    p=re.compile('<option.*?>.*?</option>',re.I|re.S)
    f_str=p.sub('',f_str)

    #remove <xxx>
    p=re.compile('<.*?>',re.S)
    f_str=p.sub('',f_str)

    #remove <!-- -->
    p=re.compile('<!--.*?-->',re.S)
    f_str=p.sub('',f_str)

    #conver &nbsp; into space
    p=re.compile('&nbsp;',re.I)
    f_str=p.sub(' ',f_str)

    #convert html codename like "&quot;" into real character
    p=re.compile("&#?\w{1,9};")
    str_list=p.findall(f_str)
    e_list=[]
    for x in str_list:
        if x not in e_list:
            e_list.append(x)
    for x in e_list:
        f_str=f_str.replace(x,htmname2uni(x))

    #convert more than 10 newline in a row into one newline
    f_str=f_str.replace("\r\n","\n")
    p=re.compile('\n{5,}?')
    f_str=p.sub('-----',f_str)


    return f_str



def get_search_result(url,key,useproxy,proxyserver='',proxyport=0,proxyuser='',proxypass=''):
    #get search result web from url by using key as the keyword
    #this only apply for POST
    #return None when fetch fails
    if isinstance(key,unicode):
        key=key.encode("GBK")
    post_data=urllib.urlencode({u"searchkey":key})
    return myopen(url,post_data,useproxy,proxyserver,proxyport,proxyuser,proxypass)



class GetContent(HTMLParser):
    #this class is used to extract content of result Page from www.xsxs520.com
    #the result is put into self.rstr
    rstr=''
    title=''
    start_counting=False
    start_adv=False
    start_title=False
    i=0
    def handle_starttag(self,tag, attrs):
        if tag=='h1':
            self.start_counting=True
            self.start_title=True
        if tag=='div':
            if attrs[0][0]=='id' and attrs[0][1]=='Centent_top': self.start_adv=True
            if self.i>=4:
                self.start_counting=False
            if self.start_counting:
                self.i+=1


    def handle_endtag(self,tag):
        if tag=='h1':self.start_title=False
        if tag=='div':
            if self.start_adv:self.start_adv=False


    def handle_data(self,data):
        if self.start_title:self.title=data.decode('gbk','replace')
        if self.start_counting and not self.start_adv:
            self.rstr+=data.decode('gbk','replace')


class DBIP(HTMLParser):
    #this class is used to Decode Book Index Page from www.xsxs520.com
    #the decoded result is put into self.rlist
    rlist=[]
    def handle_starttag(self,tag, attrs):
        if tag=='a':
            if attrs[0][0]=='href':
                p=re.compile('^\d{7}.html$',re.U)
                if p.match(attrs[0][1])<>None:
                    self.rlist.append(attrs[0][1])

class DSRP(HTMLParser):
    #this class is used to Decode Search Result Page from www.xsxs520.com
    #the decoded result is put into self.rlist

    def __init__(self):
        HTMLParser.__init__(self)
        self.rlist=[]
        self.prebegin=False
        self.mybegin=False
        self.pos=None
        self.item={}
        self.i=0


    def handle_starttag(self,tag,attrs):
        if self.mybegin:
            if tag=='td':
                if self.pos==None:
                    self.pos=0
                else:
                    self.pos+=1


    def handle_endtag(self,tag):
        if self.prebegin and not self.mybegin and tag=='tr':
            self.mybegin=True
        else:
            if self.mybegin and tag=='tr':
                #print "i am here"
                self.pos=None
        if self.mybegin and tag=='table':
            self.mybegin=False
            self.prebegin=False


    def handle_data(self,data):
        if not isinstance(data,unicode):
            data=data.decode("gbk")
        if data==u'搜索结果' and self.prebegin==False:
            self.prebegin=True
        if self.mybegin and self.pos<>None:
            r=re.compile('\s+')
            m=r.sub('',data)
            if m<>'':
                if self.pos==0:
                    self.item['bookname']=data
                if self.pos==1:
                    r=re.compile('[\'\"].+\.html?',re.U)
                    url=r.findall(self.get_starttag_text())[0][1:]
                    self.item['book_index_url']=url
                if self.pos==2:self.item['authorname']=data
                if self.pos==3:self.item['booksize']=data
                if self.pos==4:
                    self.item['lastupdatetime']=data
                if self.pos==5:
                    self.item['bookstatus']=data
                    self.rlist.append(self.item)
                    self.item={}
                #print self.rlist



def myopen(url,post_data=None,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass=''):
    interval=10 #number of seconds to wait after fail download attampt
    max_retries=3 #max number of retry
    retry=0
    finished=False
    if useproxy:
        proxy_info = {
            'user' : proxyuser,
            'pass' : proxypass,
            'host' : proxyserver,
            'port' : proxyport
            }
        proxy_support = urllib2.ProxyHandler({"http" : \
        "http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    if post_data<>None:
        myrequest=urllib2.Request(url,post_data)
    else:
        myrequest=urllib2.Request(url)
        #spoof user-agent as IE8 on win7
    myrequest.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")

    while retry<max_retries and finished==False:
        try:
            fp=urllib2.urlopen(myrequest)
            finished=True
        except:
            retry+=1
            time.sleep(interval)
    if finished==False:
        return None
    else:
        try:
            return fp.read()
        except:
            return None






def GetSearchResults(key,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass=''):
    page=get_search_result(search_url,key,useproxy,proxyserver,proxyport,proxyuser,proxypass)
    if page==None:
        return None
    myp=DSRP()
    if not isinstance(page,unicode):
        page=page.decode("gbk","replace")
    try:
        myp.feed(page)
    except:
        pass
    return myp.rlist

def GetBook(url,bkname='',win=None,evt=None,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='',concurrent=10):
    bb=''
    tr=[]
    cv=threading.Condition()
    evt.Value=u"开始下载《"+bkname+u"》"
    wx.PostEvent(win,evt)
    index_page=myopen(url,None,useproxy,proxyserver,proxyport,proxyuser,proxypass)
    if index_page==None:
        return None
    mybip=DBIP()
    mybip.feed(index_page)
    ccount=len(mybip.rlist)
    i=0
    while i<ccount:
        tlist=None
        m=0
        if ccount-i>=concurrent:
            n=concurrent
        else:
            n=ccount-i
        evt.Value=u'正在下载 '+bkname+u' 第'+unicode(i)+u'-'+unicode(i+n)+u'章,共'+unicode(ccount)+u'章'
        wx.PostEvent(win,evt)
        tr=[]
        x=0
        while x<n:
            tr.append(-1)
            x+=1
        while m<n:
            tlist=DThread(url[:-10]+mybip.rlist[(i+m)],m,useproxy,proxyserver,proxyport,proxyuser,proxypass,tr,cv)
            m+=1
        isfinished=False
        x=0
        while not isfinished:
            time.sleep(1)
            isfinished=isfull(tr)
        x=0
        while x<n:
            if tr[x]==None:
                evt.status='nok'
                return None
            else:
                mycd=GetContent()
                ttt=tr[x].replace('<br />','\n')
                mycd.feed(ttt)
                bb+='3de03ac38cc1c2dc0547ee09f866ee7b'+mycd.title+'\n'
                bb+=mycd.rstr
                #bb+=tr[x]
                x+=1
        i+=n
    if not isinstance(bb,unicode):

        bb=bb.decode('GBK','replace')
        bb=htm2txt(bb)
    evt.Value=bkname+u' 下载完毕!'
    evt.status='ok'
    wx.PostEvent(win,evt)
    return bb

class DThread:
    def __init__(self,url,i,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='',tr=None,cv=None):
        self.url=url
        self.proxyserver=proxyserver
        self.proxyport=proxyport
        self.proxyuser=proxyuser
        self.proxypass=proxypass
        self.useproxy=useproxy
        self.i=i
        self.tr=tr
        self.cv=cv
        thread.start_new_thread(self.run, ())

    def run(self):
        self.cv.acquire()
        self.tr[self.i]=myopen(self.url,None,self.useproxy,self.proxyserver,self.proxyport,self.proxyuser,self.proxypass)
        self.cv.release()
