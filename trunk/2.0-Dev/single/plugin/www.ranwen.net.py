#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#-------------------------------------------------------------------------------
# Name:        litebook plugin for www.ranwen.net
# Purpose:
#
# Author:
#
# Created:     02/01/2013
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import platform
import sys
MYOS = platform.system()
osarch=platform.architecture()
if osarch[1]=='ELF' and MYOS == 'Linux':
    sys.path.append('..')
    if osarch[0]=='64bit':
        from lxml_linux_64 import html
    elif osarch[0]=='32bit':
        from lxml_linux import html
elif MYOS == 'Darwin':
    from lxml_osx import html
else:
    from lxml import html
#import lxml.html
import urlparse
import urllib2
import time
import re
import wx
import thread
import threading
import htmlentitydefs
import urllib

Description=u"""支持的网站: http://www.ranwen.net/
插件版本：1.0
发布时间: 2013-01-02
简介：
    - 支持多线程下载
    - 关键字不能为空
    - 支持HTTP代理
作者：litebook.author@gmail.com
"""

SearchURL='http://www.ranwen.net/modules/article/search.php'

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

def isfull(l):
    xx=0
    n=len(l)
    while xx<n:
        if l[xx]==-1: return False
        xx+=1
    return True



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
    post_data=urllib.urlencode({u"searchkey":key,u'searchType':'articlename'})
    myrequest=urllib2.Request(url,post_data)
    #spoof user-agent as IE8 on win7
    myrequest.add_header("User-Agent","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")
    try:
        rr=urllib2.urlopen(myrequest)
        return rr.read()
    except Exception as inst:
        return None

def GetSearchResults(key,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass=''):
    global SearchURL
    if key.strip()=='':return []
    rlist=[]
    page=get_search_result(SearchURL,key,useproxy,proxyserver,proxyport,proxyuser,proxypass)
    if page==None:
        return None
    doc=html.document_fromstring(page)
    rtable=doc.xpath('//*[@id="searchhight"]/table') #get the main table, you could use chrome inspect element to get the xpath
    if len(rtable)!=0:
        row_list=rtable[0].findall('tr') #get the row list
        row_list=row_list[1:] #remove first row of caption
        for row in row_list:
            r={}
            col_list = row.getchildren() #get col list in each row
            r['bookname']=col_list[0].xpath('a')[0].text
            r['book_index_url']=col_list[1].xpath('a')[0].get('href')
            r['authorname']=col_list[2].xpath('a')[0].text
            r['booksize']=col_list[3].text
            r['lastupdatetime']=col_list[4].text
            r['bookstatus']=col_list[5].xpath('font')[0].text
            rlist.append(r)
        return rlist
    else:#means the search result is a direct hit, the result page is the book portal page
        #rtable=doc.xpath('//*[@id="content"]/div[2]/div[2]/table')
        r={}
        r['bookname']=doc.xpath('//*[@id="content"]/div[2]/div[2]/table/tr/td/table/tbody/tr[1]/td/table/tr[1]/td/h1')[0].text
        r['bookstatus']=doc.xpath('//*[@id="content"]/div[2]/div[2]/table/tr/td/table/tbody/tr[1]/td/table/tr[2]/td[2]/table/tr[1]/td[4]')[0].text
        r['lastupdatetime']=doc.xpath('//*[@id="content"]/div[2]/div[2]/table/tr/td/table/tbody/tr[1]/td/table/tr[2]/td[2]/table/tr[1]/td[6]')[0].text
        r['authorname']=doc.xpath('//*[@id="content"]/div[2]/div[2]/table/tr/td/table/tbody/tr[1]/td/table/tr[2]/td[2]/table/tr[2]/td[6]/a/b')[0].text
        r['book_index_url']=doc.xpath('//*[@id="content"]/div[2]/div[2]/table/tr/td/table/tbody/tr[1]/td/table/tr[2]/td[2]/table/tr[4]/td/div/b/a[1]')[0].get('href')
        r['booksize']=''
##        for k,v in r.items():
##            print k,v
        return [r]
##        burl=''
##        for e in rtable[0].iter():
##            print e.tag,e.text
##            if e.text==u'点击阅读':
##                p=e.getparent()
##                burl = p.get('href')
##                #break
##        col_list = row.getchildren() #get col list in each row
##        r['bookname']=key
##        r['book_index_url']=burl
##        r['authorname']=''
##        r['booksize']=''
##        r['lastupdatetime']=''
##        r['bookstatus']=''




##    myp=DSRP_yilook()
##    myp.feed(page)
##
##    return myp.rlist

def GetBook(url,bkname='',win=None,evt=None,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='',concurrent=10):
    bb=''
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
    fs=up.read()

    up.close()
    doc=html.document_fromstring(fs)
    r=doc.xpath('//*[@id="defaulthtml4"]/table') #get the main table, you could use chrome inspect element to get the xpath
    row_list=r[0].findall('tr') #get the row list
    clist=[]
    for r in row_list:
        for col in r.getchildren(): #get col list in each row
            for a in col.xpath('div/a'): #use relative xpath to locate <a>
                chapt_name=a.text,
                chapt_url=urlparse.urljoin(url,a.get('href'))
                clist.append({'cname':chapt_name,'curl':chapt_url})
    ccount=len(clist)
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
            tlist=DThread(clist[(i+m)]['curl'],m,useproxy,proxyserver,proxyport,proxyuser,proxypass,tr,cv)
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







if __name__ == '__main__':
    pass
    #GetBook('http://www.ranwen.net/files/article/17/17543/index.html')
    GetSearchResults(u'修真世界')

