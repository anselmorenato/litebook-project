#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import urllib2
import urllib
import re
import math
import thread
import wx
import time
import threading
from HTMLParser import HTMLParser


yilook_base_url="http://www.yi-look.com/"
yilook_search_url="http://www.yi-look.com/search.php"

##try:
##    tr
##except:
##    tr=[]


Description=u"""支持的网站: http://www.yilook.com/
插件版本：3.0
发布时间: 2010-05-1
简介：
    - 支持多线程下载
    - 空关键字也会返回结果
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
        print proxy_info
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


def ch2num(ch):
    if not isinstance(ch,unicode):
        ch=ch.decode("gbk")
    chnum_str=u'(零|一|二|三|四|五|六|七|八|九|十|百|千|万|0|1|2|3|4|5|6|7|8|9)'
    ch_ten_str=u'(十|百|千|万)'
    ch_ten_dict={u'十':u'0',u'百':u'00',u'千':u'000',u'万':u'0000',}
    ch_dict={u'零':u'0',u'一':u'1',u'二':u'2',u'三':u'3',u'四':u'4',u'五':u'5',u'六':u'6',u'七':u'7',u'八':u'8',u'九':u'9',}
    p=re.compile(u'第'+chnum_str+u'+(章|节|部|卷)',re.L|re.U)
    m_list=p.finditer(ch)
#    mid_str=m.string[m.start():m.end()]
    rr=[]
    #print m_list
    for pr in m_list:
        mid_str=pr.string[pr.start():pr.end()]
        mid_str=mid_str[1:-1]
        if mid_str[0]==u'十':
            if len(mid_str)<>1:
                mid_str=mid_str.replace(u'十',u'1',1)
            else:
                rr.append(10)
                break
        if mid_str[-1:]==u'万':
            try:
                mid_str+=ch_ten_dict[mid_str[-2:-1]]+u'0000'
            except:
                mid_str+=u'0000'
        else:
            try:
                mid_str+=ch_ten_dict[mid_str[-1:]]
            except:
                pass
        p=re.compile(ch_ten_str,re.L|re.U)
        mid_str=p.sub('',mid_str)
        for key,val in ch_dict.items():
            mid_str=mid_str.replace(key,val)
        rr.append(long(mid_str))
    i=0
    x=0
    while i<len(rr):
       x+=rr[i]*math.pow(10,5*(3-i))
       i+=1
    return long(x)


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




def get_search_result(url,key,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass=''):
    #get search result web from url by using key as the keyword
    #this only apply for POST
    #return None when fetch fails
    if useproxy:
        proxy_info = {
            'user' : proxyuser,
            'pass' : proxypass,
            'host' : proxyserver,
            'port' : proxyport # or 8080 or whatever
            }
        proxy_support = urllib2.ProxyHandler({"http" : \
        "http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        # install it
        urllib2.install_opener(opener)
    if isinstance(key,unicode):
        key=key.encode("GBK")
    post_data=urllib.urlencode({u"key":key})
    myrequest=urllib2.Request(url,post_data)
    #spoof user-agent as IE8 on win7
    myrequest.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")
    try:
        rr=urllib2.urlopen(myrequest)
        return rr.read()
    except Exception as inst:
        return None


class DSRP_yilook(HTMLParser):
    #this class is used to Decode Search Result Page from www.xsxs520.com
    #the decoded result is put into self.rlist

    def __init__(self):
        HTMLParser.__init__(self)
        self.rlist=[]
        self.mybegin=False
        self.pos=None
        self.item={}
        self.begineval=False
        self.i=0


    def handle_starttag(self,tag,attrs):
        if self.mybegin:
            if tag=='td':
                if self.pos==None:
                    self.pos=0
                else:
                    self.pos+=1


    def handle_endtag(self,tag):
        if not self.mybegin and tag=='form':
            self.mybegin=True
        else:
            if self.mybegin and tag=='tr':
                #print "i am here"
                self.pos=None
        if self.mybegin and tag=='table' and self.begineval:
            self.mybegin=False



    def handle_data(self,data):

        if not isinstance(data,unicode):
            data=data.decode("gbk")
        if self.mybegin and self.pos<>None:
##            r=re.compile('\s+')
##            data=r.sub('',data)
            if data<>'' and data<>'':
                if self.pos==0:
                    self.begineval=True
                    self.item['bookname']=data
                    r=re.compile('[\'\"].+\.html?',re.U)
                    try:
                        url=r.findall(self.get_starttag_text())[0][1:]
                    except:
                        return
                    self.item['book_index_url']=yilook_base_url+url
                if self.pos==1:
                    self.item['authorname']=data
                if self.pos==2:
                    self.item['booksize']=''
                    self.item['bookstatus']=''
                    self.item['lastupdatetime']=''
                    if self.item['bookname']<>u'更多书目':
                        self.rlist.append(self.item)
                    self.item={}
                #print self.rlist

class DBIP_yilook(HTMLParser):
    #this class is used to Decode Book Index Page from www.yilook.com
    #the decoded result is put into self.rlist

    def __init__(self):
        HTMLParser.__init__(self)
        self.rlist={}
        self.srlist=[]

    def handle_data(self,data):
        data=data.decode('GBK')
        chnum_str=u'(零|一|二|三|四|五|六|七|八|九|十|百|千|万|0|1|2|3|4|5|6|7|8|9)'
        p=re.compile(u'第'+chnum_str+u'+(章|节|部|卷)',re.L|re.U)
        if p.match(data)<>None:
            r=re.compile('[\'\"].+\.html?',re.U)
            url=r.findall(self.get_starttag_text())[0][1:]
            url=yilook_base_url+url
            if not isinstance(url,unicode):
                url=url.decode('GBK')
            self.rlist[data]=url
    def sort_list(self):
        klist=self.rlist.keys()
        klist=sorted(klist,cmp=lambda x,y:cmp(ch2num(x),ch2num(y)))
        nlist={}
        for k in klist:
            self.srlist.append([k,self.rlist[k]])


def GetSearchResults(key,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass=''):

    page=get_search_result(yilook_search_url,key,useproxy,proxyserver,proxyport,proxyuser,proxypass)
    if page==None:
        return None
    myp=DSRP_yilook()
    myp.feed(page)

    return myp.rlist

def GetBook(url,bkname='',win=None,evt=None,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='',concurrent=10):
    bb=''
    tr=[]
    cv=threading.Condition()
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
    try:
        up=urllib2.urlopen(url)
    except:
        return None

    mybip=DBIP_yilook()
    mybip.feed(up.read())
    mybip.sort_list()
    ccount=len(mybip.srlist)
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
            tlist=DThread(mybip.srlist[(i+m)][1],m,useproxy,proxyserver,proxyport,proxyuser,proxypass,tr,cv)
            m+=1
        isfinished=False
        x=0
        while not isfinished:
            time.sleep(1)
            isfinished=isfull(tr)
        x=0
        if isfinished==-1:return "canceled"
        while x<n:
            if tr[x]==None:
                evt.status='nok'
                return None
            else:
                bb+=tr[x]
                x+=1
        i+=n
    if not isinstance(bb,unicode):
        bb=bb.decode('GBK','replace')
        bb=htm2txt(bb)
    evt.Value=bkname+u' 下载完毕!'
    evt.status='ok'
##    evt.bk=bb
    wx.PostEvent(win,evt)

    return bb


class DThread:
    def __init__(self,url,i,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='',tr=[],cv=None):
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
        self.tr[self.i]=myopen(self.url,post_data=None,useproxy=self.useproxy,proxyserver=self.proxyserver,proxyport=self.proxyport,proxyuser=self.proxyuser,proxypass=self.proxypass)
        self.cv.release()





