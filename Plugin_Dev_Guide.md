

# litebook在线搜索下载插件的开发指南(for 3.1) #

本文介绍了开发litebook在线搜索及下载插件（以下简称插件）所需要了解的信息


## 编程语言 ##

  * python 2.6
  * 脚本编码格式：utf-8

## 调用接口函数 ##

  * plugin必需提供如下两个函数供litebook主程序调用：
```
    * GetSearchResults(key,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='')
      *传入参数说明：
         *key: 搜索关键字，类型unicode
         *useproxy: 是否使用带来代理，类型boolean
         *proxyserver:HTTP代理服务器地址（IP或域名），类型unicode
         *proxyport: HTTP代理服务器端口，类型unicode
         *proxyuser: HTTP代理服务器认证用户名，类型unicode
         *proxypass: HTTP代理服务器认证口令，类型unicode
      *此函数返回搜索结果列表，且结果为一个dict list，r[x]={'bookname':,'book_index_url':,'booksize':,'authorname':,'bookstatus':,'lastupdatetime'}
        *类型均为unicode
        *bookname：小说名称
        *book_index_url：小说的章节列表页的URL
        *booksize：小说大小，用途仅为显示，可以为空字符串
        *authorname：小说作者，用途仅为显示，可以为空字符串
        *bookstatus：小说状态（如连载中或完本），用途仅为显示，可以为空字符串
        *lastupdatetime：最后更新时间，用途仅为显示，可以为空字符串
        *如果搜索失败的话，则返回[]
  
    * GetBook(url,bkname='',win=None,evt=None,useproxy=False,proxyserver='',proxyport=0,proxyuser='',proxypass='',concurrent=10,mode='new',last_chapter_count=0,dmode='down',sevt=None,control=[])
      *传入参数说明：
         *book_index_page_url: 小说目录页的URL
         *win: litebook主窗口
         *evt:  用于回传的事件，litebook主窗口收到这个事件之后会在状态栏显示evt.Value的内容。此事件可以用来向litebook主窗口报告下载进度(wx.PostEvent(win,evt))
         *proxyserver:HTTP代理服务器地址（IP或域名），类型unicode
         *proxyport: HTTP代理服务器端口，类型unicode
         *proxyuser: HTTP代理服务器认证用户名，类型unicode
         *proxypass: HTTP代理服务器认证口令，类型unicode
         *concurrent：同时下载的线程数
         *mode：下载模式，类型str，可以为'new'或'update'。'new'代表全部下载, 'update'代表只下载更新的章节
         *last_chapter_count：上次下载的章节总数，类型int，当mode 为'update'时，此参数用来判断是否有更新的章节
         *dmode：下载模式，类型str，当dmode 为'down'时，为普通下载；如果dmode为'stream'的话则代表边下载边看
         *sevt：当下载模式为"stream"，这个是用来回传下载章节的事件，sevt.value是单一章节的内容（应该以章节名开头）
         *control: 控制变量，当其为非空的话，停止下载

     *此函数返回一个tuple,包含两个值：
         1. 整合后的小说内容，类型为unicode （如果mode是'update'的话，则只包括更新章节的内容）
         2. 一个dict，包含如下key:
            "bookname": unicode，小说名称
            "index_url": unicode，小说章节列表页的URL
            "last_chapter_name": unicode，最后一章的标题
            "last_update": unicode,下载完成的日期和时间
            "chapter_count": 下载的章节总数
     *如果下载失败的话或是没有更新的章节的话，则返回(None, {'index_url":})
     *除了返回一个tuple值以外，此函数在下载完成后还可以用如下code向主窗口回传一个事件：
           evt.Value=bookname+u' 下载完毕!' #如果是
           evt.status='ok' #如果是下载失败则设置为"nok"
           wx.PostEvent(win,evt)
   *插件中还可以包括一个可选的全局变量Description，类型为unicode，其内容主要是插件的简介，特性介绍，使用注意等内容。这些内容会显示在输入搜索关键字对话框的下方。
```

## HTML解析 ##
对HTML页面的解析，litebook内置了lxml，用如下code来import
```
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

```

## 插件的安装 ##
  * 将写好的python脚本文件(.py)拷贝到plugin的子目录下。
  * 然后点击菜单"文件->重新读入插件"使其生效；或者重启litebook亦可。
  * 建议脚本的文件名格式为：网站名.py