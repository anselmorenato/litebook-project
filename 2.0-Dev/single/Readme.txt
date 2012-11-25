LiteBook ver3.0 Beta 1
(c)2012 Hu Jun	

1.概述
LiteBook是一个开源看书软件，具备如下主要功能：
－ 支持Windows XP/Vista/Windows 7 
－ 支持Linux
－ 支持MAC OSX
－ 支持P2P网络LTBNET共享图书
－ 三种不同的显示模式：纸张/书本/竖排书本
－ 可以灵活定制的显示主题
－ 可以灵活定制的快捷键方案
－ 支持Text/HTML/UMD/JAR/EPUB格式
－ 支持直接读取ZIP和RAR压缩包中的文件
－ 支持智能分段
－ 支持自动生成章节列表
－ 在线小说网站搜索并下载（可以通过插件的方式进行扩展）
－ 打开文件时预览内容
－ 文件编码自动识别
－ 支持Unicode
－ 支持简繁体转换
－ 支持按文件名顺序打开文件
－ 可以在同一个窗口内打开多个文件（通过Ctrl+L进行快速切换）
－ 支持收藏夹
－ 支持自动翻页/全屏显示
－ 阅读时间提醒
－ 字体及颜色的显示方案
－ 自动记忆每个文件上次的阅读位置，并在打开时自动跳转。
－ 支持将当前打开的文件内容另存为UTF-8或是GBK编码的文本文件
－ 文件选择侧边栏
－ 在线版本检查
－ 记录并查看文件打开历史


2. 安装和运行
- LiteBook在windows下提供安装文件，安装完毕即可运行。
- LiteBook在Linux下面只能以python源码形式运行,步骤如下：
	(1)从官方网站( http://code.google.com/p/litebook-project/)的SVN中获取最新的源代码，或是在官方网站的下载页面下载源码版。从svn中checkout源码的方法：svn checkout http ://litebook-project.googlecode.com/svn/trunk/2.0-Dev/single litebook3

	(2).确认你的系统中安装有如下python环境：
	- Python 2.7（不支持python 3.0）
	- wxpython 2.8 unicode (ubuntu下sudo apt-get install python-wxgtk2.8)
	- twisted (ubuntu下sudo apt-get install python-twisted)
	- netifaces (ubuntu下sudo apt-get install python-netifaces)
	- unrar linux版( http://www.rarlab.com) 放在litebook2所在的目录即可
 
	(3).在Linux下，运行python litebook.py



3.帮助文档
- 在litebook运行之后点击菜单“帮助”-》“简明帮助”或是快捷键F1
- 或者直接用web浏览器打开litebook子目录"helpdoc"下的"index.htm"

4. LiteBook 插件功能介绍
LiteBook从1.70 beta1开始加入“搜索小说网站”功能，此功能通过插件的方式实现，不同的
小说的网站通过不同的插件实现，每个插件由一个python脚本文件组成。这些插件都放在"
plugin"子目录下。LiteBook在启动时会将"plugun"下所有的".py"文件读入内存；如果要安
装新的插件的话，只要把"xxx.py"文件拷到"plugin"子目录下，然后点击"文件->重新读入
插件"菜单使之生效。

4.1 插件开发指南
litebook的插件直接使用python编写，具体编写指南请参考这篇Wiki: http://code.google
.com/p/litebook-project/wiki/Plugin_Dev_Guide

5.和作者联系
Email:	litebook.author@gmail.com
WWW:	http://code.google.com/p/litebook-project/


6.致谢
本软件使用了如下的库程序，在此向其作者致谢：
Python:Guido van Rossum
WxPython:Robin Dunn,Harri Pasanen
chardect: Mark Pilgrim
rarfile: Marko Kreen
unrar2:Konstantin Yegupov
fanjian:ne.manman@gmail.com
genshi:http://genshi.edgewall.org/
lxml:http://lxml.de
ez_epub:timtanbin@gmail.com
pyzeroconf: Paul Scott-Murphy

本软件的网络搜索功能支持并感谢如下网站：
易读：www.yilook.com
小说520：www.xsxs520.com

7.本软件授权（License）
本软件遵循GPL 3.0和如下条款：
- 如果你希望重新分发（无论修改或是不修改源码），那么在你这么做以前，必须发一个
email到litebook.author@gmail.com告知。
