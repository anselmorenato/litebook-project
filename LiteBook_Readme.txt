LiteBook for Windows ver1.70 Beta3 帮助
(c)2010 Hu Jun	


1.LiteBook 键盘操作说明
	
	打开搜索网站对话框	Alt+C

	向下翻一行：		Down
	向上翻一行：		Up
	向下翻一页：		PageDown/空格键/右箭头
	向上翻一页：		PageUp/左箭头
	回到首页：		Home
	跳到最后一页：		End
	下一个文件：		Ctrl+右箭头
	上一个文件：		Ctrl+左箭头

	智能分段		Alt+P

	打开/关闭文件侧边栏：	Alt+D
	侧边栏内回到上级目录：	左箭头
	进入被选择的目录
	/打开被选择的文件:	右箭头

	打开/关闭自动翻页：	回车键
	打开/关闭全屏显示：	Ctrl+I
	打开/关闭工具栏：	Ctrl+T
	最小化/恢复：		ESC

	打开文件：		Ctrl+O
	打开当前文件列表：	Ctrl+L
	关闭当前文件：		Ctrl+Z
	选项：			Alt+O
	加入收藏夹：		Ctrl+D
	打开收藏夹：		Ctrl+M
	
	全部选择：		Ctrl+A
	拷贝：			Ctrl+C
	查找:			Ctrl+F
	查找下一个：		F3
	查找上一个：		F4
	过滤HTML标记：	Shift+H
	转换为繁体字：	Shift+F
	转换为简体字：	Shift+J

	显示本帮助：		F1

2.LiteBook 鼠标操作说明
	向下翻一页：		按住鼠标右键后，向下滚动中间转轮
	向上翻一页：		按住鼠标右键后，向上滚动中间转轮
	下一个文件：		双击鼠标中键
	上一个文件：		按住鼠标右键后，双击鼠标中键

2.1 LiteBook 插件功能介绍
LiteBook从1.70 beta1开始加入“搜索小说网站”功能，此功能通过插件的方式实现，不同的小说的网站通过不同的插件实现，每个插件由一个python脚本文件组成。这些插件都放在"plugin"子目录下。
LiteBook在启动时会将"plugun"下所有的".py"文件读入内存；如果要安装新的插件的话，只要把"xxx.py"文件拷到"plugin"子目录下，然后点击"文件->重新读入插件"菜单使之生效。


3.LiteBook功能说明
－ 支持Windows XP/Vista/Windows 7 
－ 从版本1.2起支持Linux，请到本软件的官方站点下载Linux版本
－ 支持Text文件
－ 支持HTML文件过滤（包括对一些站点HTML保护的自动去除）
－ 支持UMD格式
－ 支持Jar格式
－ 支持EPUB格式
－ 支持智能分段
－ 在线小说网站搜索并下载（可以通过插件的方式进行扩展）
－ 打开文件时预览内容
－ 支持直接读取ZIP和RAR格式的文件
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



4.和作者联系
Email:	litebook.author@gmail.com
WWW:	http://code.google.com/p/litebook-project/


5.致谢
本软件使用了如下的库程序，在此向其作者致谢：
Python:Guido van Rossum
WxPython:Robin Dunn,Harri Pasanen
chardect: Mark Pilgrim
rarfile: Marko Kreen
unrar2:Konstantin Yegupov
fanjian:ne.manman@gmail.com
本软件的网络搜索功能支持并感谢如下网站：
易读：www.yilook.com
