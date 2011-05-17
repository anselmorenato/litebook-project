﻿var contents = new Array("\n\r\n\rLitebook从ver2.2起开始支持缓存功能，此功能的目的主要是为了加快epub和jar文件的载入速度。由于epub和jar文件都是ZIP压缩格式，因此如果其中包含的章节很多的话，每次载入的时候所花费的时间就很长了，为了缩短这个时间，litebook会把第一次打开之后文本另存为一个文本文件存在cache子目录下，这样以后再次打开的时候就直接打开这个文本文件了。 \n\r\n\r注：从ver2.3开始cache子目录位置修改为：\n\r  Windows: C:\\Documents and   Settings\\[用户名]\\litebook\\cache\n\r  Linux:   ~/litebook/cache\n\r\n\r\n\r这个特性的代价是会消耗一些硬盘空间，不过就目前普遍上百G的硬盘来讲，问题也不大，当然如果你希望清空这些文件的话，可以用菜单“文件”-》“清空缓存”。\n\r\n\r&nbsp;\n\r\n\r&nbsp;","缓存","scr\\cache.html","\n\r\n\rlitebook从ver2.2起加入自动生成章节列表功能，缺省快捷键Ctrl+U，进一步方便读者在文本内导航，如下图所示： \n\r\n\r \n\r\n\r&nbsp;\n\r\n\r&nbsp;","自动生成章节列表","scr\\catalog.htm","\n\r\n\rlitebook2支持如下命令行选项： \n\r\n\rlitebook2 [-reset | &lt;filename&gt;]\n\r  -reset：   会删除litebook.ini和litebook_key.ini，并恢复到缺省配置。此选项可以用于解决某些无法启动的问题。  filename： litebook会直接载入filename所指定的文件\n\r","命令行选项","scr\\commandline.html","\n\r\n\rlitebook2支持Windows资源管理器右键菜单\"用litebook阅读\"，可以直接在资源管理器中启动litebook2，使用更加方便。 ","Windows资源管理器集成","scr\\explorer.html","   Hu Jun  Hu Jun  6  8  2011-01-02T22:43:00Z  2011-01-02T22:51:00Z  1  418  2387  Alcatel-Lucent  19  5  2800  11.9999    Clean  Clean    false  false  false         MicrosoftInternetExplorer4        \n\r\n\r TOC\\o &quot;1-3&quot; \\h \\z \\u 常见问题...  PAGEREF _Toc281743236 \\h 1 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200330036000000\n\r\n\r运行相关...  PAGEREF _Toc281743237 \\h 1 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200330037000000\n\r\n\r启动litebook 时报错怎么办？...  PAGEREF _Toc281743238 \\h 1 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200330038000000\n\r\n\r为什么litebook无法在我的操作系统上运行？...  PAGEREF _Toc281743239 \\h 1 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200330039000000\n\r\n\r如何以源码形式运行litebook？...  PAGEREF _Toc281743240 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340030000000\n\r\n\r为什么我把Linux版的litebook升级到1.4之后，我的配置都消失了？...  PAGEREF _Toc281743241 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340031000000\n\r\n\r使用相关...  PAGEREF _Toc281743242 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340032000000\n\r\n\r为什么我无法打开ZIP/RAR中UMD/JAR/ZIP/RAR？...  PAGEREF _Toc281743243 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340033000000\n\r\n\r功能相关...  PAGEREF _Toc281743244 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340034000000\n\r\n\r能不能在将来的版本中增加xxx功能？...  PAGEREF _Toc281743245 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340035000000\n\r\n\r我发现一个Bug.  PAGEREF _Toc281743246 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340036000000\n\r\n\r其它...  PAGEREF _Toc281743247 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340037000000\n\r\n\rlitebook是免费软件吗？...  PAGEREF _Toc281743248 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340038000000\n\r\n\rlitebook有没有手机版？...  PAGEREF _Toc281743249 \\h 2 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200340039000000\n\r\n\rlitebook是开源软件吗？...  PAGEREF _Toc281743250 \\h 3 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200350030000000\n\r\n\r你为什么要写这么一个软件？...  PAGEREF _Toc281743251 \\h 3 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200350031000000\n\r\n\rlitebook是用什么语言写的？...  PAGEREF _Toc281743252 \\h 3 08D0C9EA79F9BACE118C8200AA004BA90B02000000080000000E0000005F0054006F0063003200380031003700340033003200350032000000&nbsp;常见问题运行相关启动litebook时报错怎么办？\n\r\n\r请尝试如下办法：\n\r 如果是Windows 绿色版无法运行，那么请安装Microsoft     VC++ 2008 Redistrbute运行库。在微软的网站或是本网站都可以下载。 或者： \n\r  Windows下：在litebook开始菜单程序组里，选择“恢复到缺省配置启动”，或者在命令行下执行“litebook2.exe      –reset”  Linux下：执行命令 “python      litebook2_linux.py –reset”\n\r  如果还不行的话，建议升级到最新版试试。\n\r为什么litebook无法在我的操作系统上运行？\n\r litebook目前在如下平台上提供能够直接运行的软件包： \n\r  Windows XP/Vista/7\n\r  litebook可以以源码的形式运行在各种Linux软件平台上，但需要安装一些第三方的软件包。 MAC OS X暂时不支持（买不起苹果的电脑...） 至于xxBSD就没打算支持，因为那些系统本来就不是用来做桌面应用的。 如果litebook连源码形式都无法在你的操作系统运行的话，那么只有最后一招：你自己Hack吧。\n\r如何以源码形式运行litebook？\n\r 参见本帮助文件\n\r为什么我把Linux版的litebook升级到1.4之后，我的配置都消失了？\n\r\n\r这是因为1.4版之后，Linux版的配置文件名称改为.litebook.ini，存放在用户的HOME目录下了。所以你只要将原来目录中的litebook.ini拷贝到HOME下，并改为.litebook.ini，就可以实现平滑升级了。使用相关为什么我无法打开ZIP/RAR中UMD/JAR/ZIP/RAR？\n\r\n\r\n\rUMD和JAR本身都已经是压缩格式了，再压缩一遍没什么意思，所以这个功能暂时不打算做了。功能相关能不能在将来的版本中增加xxx功能？\n\r\n\r优先推荐你使用GoogleCode的Issues系统，其次也可以发信到litebook.author@gmail.com。我会尽力，但是无法保证每个要求都能得到满足。我发现一个Bug\n\r\n\r请先升级到最新版看看Bug是否已经修复，如果没有的话，优先推荐你使用GoogleCode的Issues系统，其次也可以写信到litebook.author@gmail.com，包括你的操作系统及版本，litebook的版本，错误情况描述等等，越具体越好。其它litebook是免费软件吗？\n\r\n\r是的，你无需为使用它而支付任何费用。litebook有没有手机版？\n\r\n\r目前还没有做手机版的打算，因为手机上已经有了不错的看书软件，没必要再去重复劳动了。litebook是开源软件吗？\n\r\n\r是的，源代码已经放进 google code中的SVN。你为什么要写这么一个软件？\n\r\n\r我平时没事的时候也喜欢在电脑上看看闲书，但是总觉得找不到一个能让我完全满意的看书软件，所以就自己写了一个。litebook是用什么语言写的？\n\r\n\rpython+wxpython","常见问题","scr\\FAQ.html","\n\r\n\r请看各个分章节的内容","功能介绍","scr\\features.html","\n\r\n\r智能分段的作用就是把一篇排版较为凌乱的文本重新排版整齐，本功能通过菜单“视图”－》“智能分段”或是通过下列工具栏图标激活。 \n\r\n\r \n\r\n\r下面是个例子：\n\r  智能分段前的文本：\n\r\n\r\n\r\n\r  智能分段后的文本\n\r\n\r\n\r\n\r\n\r&nbsp;","智能分段","scr\\fenduan.html","\n\r\n\r以下是litebook2常用功能快捷键，更多快捷键设置请看“功能介绍”章中的“按键控制”。 \n\r\n\r              向上翻行    方向上键      向下翻行    方向下键      向上翻页    方向左键      向上翻页    PAGEUP      向下翻页    PAGEDOWN      向下翻页    空格键      向下翻页    方向右键      向上翻半页    ，      向下翻半页    。      后退10%    [      前进10%    ]      后退1%    9      前进1%    0      跳到首页    HOME      跳到结尾    END      最小化    ESC      显示进度条    Z      上一个文件    CTRL+[      下一个文件    CTRL+]      增大字体    =      减小字体    -","常用快捷键","scr\\Fkey.html","\n\r\n\r从ver2.3开始，litebook支持将电脑中的书上传到移动设备，目前支持如下移动看书APP： \n\r  IPHONE/IPAD上的Stanza  IPHONE/IPAD上的iBooks\n\r\n\r\n\r由于Stanza和iBooks都支持EPUB格式的电子书，因此上传书分为以下步骤：\n\r  将图书转化为EPUB格式（如果已经是EPUB格式，那么这步可以跳过）  将EPUB电子书拷入电脑上的共享目录（或者可以在第一步格式转换将输出目录直接设置为共享目录）  启用litebook内置的WEB服务器  使用Stanza/iBooks下载共享的EPUB图书\n\r\n\r\n\rStanza的操作步骤:\n\r  生成EPUB文件，见下图：\n\r\n\r\n\r\n\r\n\r两种章节划分方式：\n\r  自动：litebook会自动检测并划分章节  安装字数：安装所输入的字数划分章节\n\r\n\r\n\r注：输出文件的缺省目录就是缺省的共享文件目录，当前文件名会作为新的EPUB文件名。\n\r\n\r2.将EPUB文件拷入共享目录，共享目录可以在选项-控制设置里进行选择。如果在第一步中已经将输出文件放在了共享目录中，那么这步可以跳过。\n\r\n\r3.启用WEB服务器：通过菜单“工具”-》“启用WEB服务器”\n\r\n\r4.打开Stanza程序，在下方的主菜单中选择“Get Books\"。缺省情况下Stanza将自动发现litebook的共享源，如下图所示：\n\r\n\r \n\r\n\r 选择“litebook_shared“，然后下载图书即可。\n\r\n\r如果Stanza无法自动发现litebook的话，也可以按右上方的“+”按钮手动添加源，URL的格式为“http://MY_IP:8000”，其中MY_IP是你电脑的IPv4地址。在windows下可以通过IPCONFIG命令获得，8000是缺省的端口号，你也可以在litebook选项中修改为其他的端口。\n\r\n\riBooks 的操作步骤：\n\r\n\r 1，2两步和Stanza相同。\n\r\n\r3. 打开Safari浏览器，访问http://MY_IP:8000”，其中MY_IP是你电脑的IPv4地址。在windows下可以通过IPCONFIG命令获得，8000是缺省的端口号，你也可以在litebook选项中修改为其他的端口。\n\r\n\r 4.下载你要的书，下载完毕和选择“用iBooks打开”\n\r\n\r&nbsp;","上传至移动设备","scr\\iOS_uploading.html","\n\r\n\rlitebook2几乎所有的功能都提供相应的快捷键，而且所有的快捷键在“文件”－》“选项”对话框里都可以进行配置，并且还提供相应的按键方案导入和导出的功能。 \n\r\n\r下面是缺省的按键设置：\n\r\n\r              向上翻行    方向上键      向下翻行    方向下键      向上翻页    方向左键      向上翻页    PAGEUP      向下翻页    PAGEDOWN      向下翻页    空格键      向下翻页    方向右键      向上翻半页    ，      向下翻半页    。      后退10%    [      前进10%    ]      后退1%    9      前进1%    0      跳到首页    HOME      跳到结尾    END      最小化    ESC      显示进度条    Z      上一个文件    CTRL+[      下一个文件    CTRL+]      增大字体    =      减小字体    -      智能分段    ALT+P      查找    CTRL+F      查找下一个    F3      查找上一个    F4      替换    CTRL+H      自动翻页    回车      全屏显示    CTRL+I      选项    ALT+O      显示文件侧边栏    ALT+D      显示目录    CTRL+U      打开文件    CTRL+P      文件列表    CTRL+O      另存为    CTRL+S      纸张显示模式    ALT+M      书本显示模式    ALT+B      竖排书本显示模式    ALT+N      添加到收藏夹    CTRL+D      整理收藏夹    CTRL+M      搜索小说网站    ALT+C      重新载入插件    CTRL+R      清空缓存    CTRL+ALT+Q      拷贝    CTRL+C      显示工具栏    CTRL+T      切换为简体字    F7      切换为繁体字    F8      简明帮助    F1      版本更新内容    F2      检查更新    F5      关于    F6      过滤HTML标记    F9      生成EPUB    CTRL+E      启用/关闭WEB服务器    ALT+W      关闭    CTRL+Z      退出    ALT+X  ","按键控制","scr\\key.html","  \n\r\n\r由于各个linux系统之间的差异，litebook2在linux下只提供源码版，下面是litebook2在linux下的安装运行方法：\n\r    从官方网站   (  http://code.google.com/p/litebook-project/)   的SVN中获取最新的源代码，或是在官方网站的    下载页面   下载源码版。      \n\r      从svn中checkout源码的方法：        \n\r        svn checkout&nbsp;http       ://litebook-project.googlecode.com/svn/trunk/2.0-Dev&nbsp;litebook2                 \n\r\n\r    确认你的系统中安装有如下python环境：  \n\r    Python 2.6     （不支持python 3.0）            wxpython     2.8.10.1 unicode (ubuntu/debian下参见        http://wiki.wxpython.org/InstallingOnUbuntuOrDebian)      \n\r\n\rchardet 2.01     (   http://chardet.feedparser.org/)    \n\r      \n\r\n\r下载下来后，解压并用这个命令安装：sudo python setup.py install                \n\r      \n\r\n\rrarfile 2.0     (   http://pypi.python.org/pypi/rarfile/2.0)    \n\r      \n\r\n\r下载下来后，解压并用这个命令安装：sudo python setup.py install                \n\r      \n\r\n\runrar     linux版(  http://www.rarlab.com)    \n\r      \n\r\n\r放在litebook2所在的目录即可\n\r\n\r  在Linux下，运行python   litebook2_linux.py    \n\r","如何在Linux下安装并运行","scr\\linux.htm","\n\r\n\rlitebook2同样支持用鼠标进行操作，下面是鼠标操作列表： \n\r\n\r                向上翻行    鼠标滚轮    &nbsp;      向下翻行    鼠标滚轮    &nbsp;      上一个文件    双击鼠标中键    仅windows版      下一个文件    按住鼠标右键后，双击鼠标中键                 仅windows版\n\r\n\r&nbsp;","鼠标控制","scr\\mouse.html","\n\r\n\rLitebook支持定制化的显示主题，通过“文件”－》“选项”菜单或是工具栏图标打开对话框： \n\r\n\r\n\r  Litebook2预置了几种显示主题，可以通过预览窗口下面的下拉菜单进行快速选择。   显示主题的定制是非常灵活的，从背景图片/背景颜色/显示方式/下划线/字体/行间距等等均可定制，定制的效果可以在预览窗口所见及所得。   定制的主题可以通过“另存为”按钮存为新的主题；已有的主题也可以通过“删除按钮”进行删除   另外显示主题还可以导出（和导入）后缀为\".lbt\"的文件；\n\r\n\r\n\r&nbsp;\n\r\n\r&nbsp;","显示主题","scr\\option_display.html","\n\r\n\r本文介绍了开发litebook在线搜索及下载插件（以下简称插件）所需要了解的信息编程语言\n\r  python 2.6/2.7  脚本编码格式：utf-8\n\r调用接口函数\n\r  plugin必需提供如下两个函数供litebook主程序调用：&nbsp; &nbsp; * GetSearchResults(key,useproxy=False,proxyserver=\'\',proxyport=0,proxyuser=\'\',proxypass=\'\')\n\r&nbsp; &nbsp; &nbsp; *传入参数说明：\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*key: 搜索关键字，类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*useproxy: 是否使用带来代理，类型boolean\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxyserver:HTTP代理服务器地址（IP或域名），类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxyport: HTTP代理服务器端口，类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxyuser: HTTP代理服务器认证用户名，类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxypass: HTTP代理服务器认证口令，类型unicode\n\r&nbsp; &nbsp; &nbsp; *此函数返回搜索结果列表，且结果为一个dict list，r[x]={\'bookname\':,\'booksize\':,\'authorname\':,\'bookstatus\':,\'lastupdatetime\'}\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*类型均为unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*如果搜索失败的话，则返回None\n\r&nbsp; \n\r&nbsp; &nbsp; * GetBook(url,bkname=\'\',win=None,evt=None,useproxy=False,proxyserver=\'\',proxyport=0,proxyuser=\'\',proxypass=\'\',concurrent=10)\n\r&nbsp; &nbsp; &nbsp; *传入参数说明：\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*book_index_page_url: 小说目录页的URL\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*win: litebook主窗口\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*evt: 用于回传的事件，litebook主窗口收到这个事件之后会在状态栏显示evt.Value的内容。另外如果在下载结束时收到evt.status=\'nok\'的事件，则代表下载失败。\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxyserver:HTTP代理服务器地址（IP或域名），类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxyport: HTTP代理服务器端口，类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxyuser: HTTP代理服务器认证用户名，类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*proxypass: HTTP代理服务器认证口令，类型unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*concurrent：同时下载的线程数\n\r&nbsp; &nbsp; &nbsp; *此函数返回整合后的小说内容，类型为unicode\n\r&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;*如果下载失败的话，则返回None\n\r\n\r插件中还可以包括一个可选的全局变量Description，类型为unicode，其内容主要是插件的简介，特性介绍，使用注意等内容。这些内容会显示在输入搜索关键字对话框的下方。\n\r插件的安装\n\r  将写好的python脚本文件(.py)拷贝到plugin的子目录下。   然后点击菜单\"文件-&gt;重新读入插件\"使其生效；或者重启litebook亦可。   建议脚本的文件名格式为：网站名.py\n\r","在线搜索及下载插件开发指南","scr\\plugin.html","\n\r\n\r在载入后缀名为\".htm\"或\".html\"的文件时，litebook2会自动去除文件中的HTML标记 ，但是如果是其他类型的文件内含有HTML标记，你也可以通过这个功能去除。 \n\r\n\r本功能可以通过点击下列工具栏图标或是菜单“工具”－》“过滤HTML标签”实现：\n\r\n\r\n\r\n\r&nbsp;","去除HTML标记","scr\\remove_html.html","\n\r\n\r由于litebook2完全重写了核心显示组件，因此其进度条安排如下： \n\r  \n\r    可以拖动工具栏上的进度条     可以按\"z\"键显示/关闭\n\r  \n\r\n\r&nbsp;","进度条","scr\\scrollbar.html","litebook在线搜索和下载功能介绍\n\r\n\rlitebook从ver1.70 beta起开始加入在线搜索和下载的功能，其原理就是利用HTTP协议直接获取小说网站的搜索结果页面和小说的目录页面，然后加以分析，提取出小说的内容，然后加以整合、过滤，最后是获得一个整合后的文本文件。 上述过程说的通俗一点就是litebook把如下的步骤自动化了：\n\r  访问某小说网站，并在其搜索框内输入关键字   在搜索结果页面点击某个小说的链接，转入小说的目录页   把这本小说所有的章节都下载下来，然后拼成一个文本文件\n\r\n\r\n\r\n\r\n\r此功能具备如下特点：\n\r  每个小说网站的支持都是通过一个插件的形式来实现   插件可以直接用python编写，编写完之后把脚本文件拷贝到plugin子目录下即可生效   支持HTTP代理(需插件支持)   支持多线程下载(需插件支持)   支持同时多个任务下载   支持同时搜索所有的网站\n\r\n\r\n\r使用说明\n\r  首先在“文件”菜单中选择“搜索小说网站”，也可以使用快捷键 Alt+C\n\r  \n\r\n\r \n\r    然后在弹出的对话框中选择要搜索的网站以及输入关键字 \n\r  \n\r\n\r \n\r    在搜索结果对话框中选择你要下载的小说，然后点击“下载”按钮 \n\r  \n\r\n\r \n\r    在下载过程中，你可以继续看别的小说，下载是在后台进行的，底部的状态栏中会显示当前进程 \n\r  \n\r\n\r&nbsp; \n\r    下载结束后，会有弹出对话框提醒（你也可以在选项中设置直接保存而不提醒） \n\r  \n\r\n\r&nbsp; \n\r    &nbsp;你也可以选择直接观看，结果如下： \n\r  \n\r\n\r \n\r    关于本功能的设置，请参见选项对话框中的下载设置页 \n\r  \n\r\n\r ","在线搜索及下载","scr\\search_download.htm","\n\r\n\rlitebook2支持三种显示模式：纸张/书本/竖排书本。三种显示模式可以通过菜单“视图”或是通过下列工具栏图标进行选择： \n\r\n\r\n\r\n\r下面是三种显示模式的截屏：\n\r  纸张模式\n\r\n\r\n\r\n\r  书本模式\n\r\n\r\n\r\n\r  竖排书本模式\n\r\n\r\n\r","多种显示模式","scr\\showmode.html","\n\r\n\r文件选择侧边栏是litebook2中能够快速方便地选择要打开文件的一个功能，通过ALT+D或是菜单“视图”－》“显示文件选择侧边栏”打开或是关闭。如下图所示： \n\r\n\r\n\r  在文件选择侧边栏上方有一个输入栏，在这个输入栏中可以输入拼音来过滤你想寻找的文件，比如说你想只显示文件名中含有“修仙”的文件你可以输入“xiuxian”进行过滤。  另外你还可以用如下快捷键在文件选择侧边栏内进行操作：\n\r\n\r\n\r              上下选择文件    上、下方向键      回到上级目录    左方向键      进入当前子目录    右方向键      打开当前选择的文件    右方向键      在拼音输入栏和文件列表区切换    TAB键\n\r  文件选择侧边栏缺省会显示一个当前选择文件的内容预览窗口，你可以在选项对话框（控制设置页）中选择关闭这个特性。\n\r\n\r\n\r&nbsp;\n\r\n\r&nbsp;","文件选择侧边栏","scr\\sidebar.html","\n\r  支持Windows XP/Vista/7\n\r  支持各种主流Linux桌面\n\r","系统需求","scr\\system_requirement.htm","\n\r\n\rlitebook2是一个注重于用户体验、开源的中文看书软件，目前支持Windows和Linux。\n\r\n\r具备如下特点：\n\r  三种不同的显示模式：纸张/书本/竖排书本  可以灵活定制的显示主题  可以灵活定制的快捷键方案  支持Text/HTML/UMD/JAR/EPUB格式  导出为EPUB文件  内置WEB服务器以及基于mDNS的自动发现功能  完美支持IPHONE/IPAD上的看书APP: Stanza  支持iBooks  支持直接从ZIP/RAR压缩包中读取TXT/HTML文件  小说在线搜索和下载  智能分段  自动生成章节列表  支持各种文件编码（包括UTF-8）  快捷方便的文件选择侧边栏（支持拼音过滤）  简繁转换\n\r\n\r\n\r\n\r\n\r\n\r官方网站：http://code.google.com/p/litebook-project/\n\r","简介","scr\\topic.htm","   Hu Jun  Hu Jun  2  4  2011-01-16T20:29:00Z  2011-01-16T20:33:00Z  1  447  2550  Alcatel-Lucent  21  5  2992  11.9999    Clean  Clean    false  false  false         MicrosoftInternetExplorer4        \n\r\n\r版本历史\n\r\n\r2011-5-17 ver2.3\n\r\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;新增转换为EPUB格式的功能\n\r&nbsp;&nbsp;&nbsp;&nbsp;* 新增内置WEB服务器（for Stanza and iBooks）&nbsp;&nbsp;\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;新增基于组播DNS的自动发现功能（For Stanza）&nbsp;\n\r&nbsp;&nbsp;&nbsp;&nbsp;* 消除一些BUG\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;Linux版将所依赖的一些第三方程序一同打包&nbsp;，这样就无需另外安装了。&nbsp;&nbsp;&nbsp;   \n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;更改了缓存目录的位置\n\r \n\r\n\r \n\r\n\r2011-3-6 ver2.21\n\r\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;新增文字替换功能，缺省快捷键Ctrl+H\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;EPUB和JAR文件解码新增缓存功能，解决有大量章节时载入慢的问题（需要占用一些磁盘空间，详见本帮助文件的功能介绍-》缓存）&nbsp;&nbsp;\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;&nbsp;新增自动生成章节列表功能，缺省快捷键Ctrl+U\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;新增像窗口内拖动文件直接打开的功能&nbsp;&nbsp;&nbsp;\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;消除一些BUG (issue 28/31/32/39/42)&nbsp; \n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;消除一个打开Rar文件中包含中文目录名出错的BUG&nbsp;&nbsp;\n\r&nbsp;&nbsp;&nbsp;&nbsp;*&nbsp;消除一个无法保持下划线颜色的BUG     \n\r\n\r 2011-1-16 ver2.1     \n\r\n\r* 新增如下导航快捷键：&nbsp;      \n\r\n\r向上翻半页        \n\r\n\r，         \n\r\n\r向下翻半页      \n\r\n\r。        \n\r\n\r后退10%      \n\r\n\r[        \n\r\n\r前进10%      \n\r\n\r]        \n\r\n\r后退1%      \n\r\n\r9        \n\r\n\r前进1%      \n\r\n\r0\n\r\n\r&nbsp;&nbsp;&nbsp; * Linux版新增工具栏进度条\n\r&nbsp;&nbsp;&nbsp; * 自动翻页的缺省快捷键改成ALT+T\n\r&nbsp;&nbsp;&nbsp; * 消除一些BUG\n\r\n\r2011-1-2 ver2.0 正式版\n\r&nbsp;&nbsp;&nbsp; * 重写显示核心组建，新增三种显示模式/页面背景/页边距/行间距均可设置\n\r&nbsp;&nbsp;&nbsp; * 重写选项对话框\n\r&nbsp;&nbsp;&nbsp; * 重写帮助系统\n\r&nbsp;&nbsp;&nbsp; * 所有功能的快捷键均可配置\n\r&nbsp;&nbsp;&nbsp; * 显示方案和按键方案均可导入导出\n\r&nbsp;&nbsp;&nbsp; * 新增进度条\n\r&nbsp;&nbsp;&nbsp; * 新增windows资源管理器右键菜单和命令行选项\n\r&nbsp;&nbsp;&nbsp; * 新增恢复到缺省配置的操作\n\r&nbsp;&nbsp;&nbsp; * 修正若干BUG\n\r&nbsp;&nbsp; \n\r2010-05-06 ver1.70 正式版\n\r&nbsp;&nbsp;&nbsp; * 新增在文件侧边栏中输入拼音过滤当前文件列表的功能\n\r&nbsp;&nbsp;&nbsp; * 修正N个和中文路径名相关的BUG（惭愧，现在才发现）fix issue 19\n\r&nbsp;&nbsp;&nbsp; * 修正在64bit系统上打开UMD文件出错的问题. fix issue 18\n\r\n\r2010-05-01 ver1.70 beta3\n\r&nbsp;&nbsp;&nbsp; * 改写了导入插件的方式，使其工作更加稳定\n\r&nbsp;&nbsp;&nbsp; * 改进现有插件多线程下载能力，新增支持多个任务同时下载\n\r&nbsp;&nbsp;&nbsp; * 新增“搜索所有网站”的功能，找书更加方便 \n\r&nbsp;&nbsp;&nbsp; * 新增“搜索及下载”的工具栏图标\n\r&nbsp;&nbsp;&nbsp; * 新增“重新读入插件”菜单\n\r\n\r2010-03-24 ver1.70 beta2\n\r&nbsp;&nbsp;&nbsp; * 改进了搜索及下载功能，试用更加方便\n\r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *插件开发指南更新\n\r&nbsp;&nbsp;&nbsp; * 原有插件升级支持多线程下载；新增一个插件\n\r\n\r2010-03-19 ver1.70 beta\n\r&nbsp;&nbsp;&nbsp; * 支持智能分段\n\r&nbsp;&nbsp;&nbsp; * 在线小说网站搜索及下载(Alt+C)\n\r&nbsp;* 1.70 beta版中内置了www.yilook.com的插件\n\r&nbsp;* 可以通过插件的形式支持新的网站，插件开发指南请参见http://code.google.com/p/litebook-project/\n\r&nbsp;&nbsp;&nbsp; * 改进了HTML标签的过滤算法\n\r&nbsp;&nbsp;&nbsp; * fix issue 14 comment 3\n\r\n\r\n\r2009-12-31 ver.160\n\r&nbsp;&nbsp;&nbsp; * 支持新的电子书格式EPUB\n\r&nbsp;&nbsp;&nbsp; * 能够记住隐藏工具栏的设置\n\r&nbsp;&nbsp;&nbsp; * 最大曾经打开文件的菜单数可以在选项中设置\n\r&nbsp;&nbsp;&nbsp; * 修正一个在某些情况下可能导致字体变化的BUG\n\r&nbsp;&nbsp;&nbsp; * 增加\"帮助\"－&gt; “版本更新内容\"菜单\n\r\n\r\n\r2009-11-20 ver1.55\n\r&nbsp;&nbsp;&nbsp; * 重写了zip/rar文件打开对话框的列表显示部分，修复了N个相关Bug\n\r&nbsp;&nbsp;&nbsp; * 重写了\"上一个文件/下一个文件\"的搜索算法，支持中文数字文件名（如第一章，第二章），使得阅读更加方便。&nbsp;\n\r\n\r\n\r2009-10-13 ver1.54\n\r&nbsp;&nbsp;&nbsp; * 修正了一个如果没有配置文件就无法启动的Bug\n\r&nbsp;&nbsp;&nbsp; * 增加了一个选项控制是否在文件侧边栏中显示所有文件还是只显示已支持格式的文件\n\r&nbsp;&nbsp;&nbsp; * 在全屏显示的时候，按鼠标右键会弹出”关闭全屏\"的菜单\n\r\n\r2009-9-28 ver1.53\n\r\n\r&nbsp;&nbsp;&nbsp; * 修正了包括如下相关的N(N&gt;5)个Bug\n\r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; o zip/rar/umd/jar载入\n\r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; o 侧边栏/文件列表对话框 \n\r\n\r\n\r2009-9-25 ver1.52\n\r&nbsp;&nbsp;&nbsp; * 将对文件内容哈希改为对文件名（不包括路径）哈希，也就是说具备相同文件名的文件会被认为是同一本书，从而在载入时自动跳转至上次阅读位置。\n\r&nbsp;&nbsp;&nbsp; * 增加了“视图－》全屏显示”菜单项，快捷键为Ctrl+I\n\r&nbsp;&nbsp;&nbsp; * 取消配置文件中启动时全屏显示的配置项\n\r&nbsp;&nbsp;&nbsp; * 以往文件打开历史的对话框中文件会缺省以时间排序，最近的打开的文件排在最前面\n\r&nbsp;&nbsp;&nbsp; * 如果打开一个已经在“曾经打开的文件”菜单中的文件，那么“曾经打开的文件”菜单将不会被更新\n\r\n\r\n\r2009-8-18 ver1.51\n\r&nbsp;&nbsp;&nbsp; * 在工具栏中新增打开侧边栏的图标\n\r&nbsp;&nbsp;&nbsp; * 提升文件侧边栏的显示速度\n\r&nbsp;&nbsp;&nbsp; * 侧边栏进入子目录，然后再返回的时候，会自动选择之前的父目录\n\r&nbsp;&nbsp;&nbsp; * 新增查看打开文件历史功能，所有已打开的文件历史都记录在litebook.bookdb中\n\r&nbsp;\n\r\n\r\n\r2009-6-26 ver1.5发布\n\r\n\r&nbsp;&nbsp;&nbsp; * 新增文件选择侧边栏(Alt+D) ( Issue 5 )\n\r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; o 侧边栏内回到上级目录快捷键：左箭头\n\r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; o 进入被选择的目录/打开被选择的文件:右箭头\n\r&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; o 可以在选项菜单内设置是否在侧边栏中是否预览文件内容 \n\r&nbsp;&nbsp;&nbsp; * 新增版本检查更新功能，此功能可以在选项菜单内进行设置(Issue 6 )\n\r&nbsp;&nbsp;&nbsp; * Windows版新增选项控制是否启用ESC作为老板键 \n\r\n\r2009-6-17 FAQ Updated\n\r\n\r常见问题(FAQ)更新\n\r\n\r\n\r2009-6-17 v1.4发布\n\r\n\r&nbsp;&nbsp;&nbsp; * 增加隐藏工具栏的功能(Ctrl+T)\n\r&nbsp;&nbsp;&nbsp; * 为HTML过滤，转换为简体，转换为繁体字这三个功能增加快捷键（SHIFT+H/J/F）\n\r&nbsp;&nbsp;&nbsp; * 现在如果要保存的界面方案和已有方案名字相同的话，会询问是否覆盖\n\r&nbsp;&nbsp;&nbsp; * 不再允许空的界面方案名称\n\r&nbsp;&nbsp;&nbsp; * 修正Linux获取运行文件所在目录的Bug\n\r&nbsp;&nbsp;&nbsp; * 修正一个读取配置文件的Bug\n\r&nbsp;&nbsp;&nbsp; * Linux版的配置文件改名为.litebook.ini，存放在HOME下面 \n\r\n\r2009-6-16 源代码发布\n\r\n\r&nbsp;&nbsp;&nbsp; * 请从SVN中Checkout \n\r\n\r2009-6-12 v1.31发布(Onlyfor Windows version)\n\r\n\r&nbsp;&nbsp;&nbsp; * 修正一个在载入某些Unicode编码的文件时，显示不完全的Bug，此Bug仅在Windows版发现，强烈推荐升级。 \n\r\n\r2009-6-5 v1.3发布\n\r\n\r&nbsp;&nbsp;&nbsp; * 将工具栏中\"简\"和\"繁\"的图标改成背景透明的图片 \n\r\n\r&nbsp;&nbsp;&nbsp; * 修正载入文件时的一个Bug\n\r\n\r&nbsp;&nbsp;&nbsp; * 增加鼠标控制功能，详情参见帮助（仅ForWindows版） \n\r\n\r&nbsp;&nbsp;&nbsp; * 将ESC注册为全局性热键，按一下ESC会最小化窗口，再按一下窗口还原（仅For Windows版） \n\r\n\r2009-6-3 v1.21发布\n\r\n\r&nbsp;&nbsp;&nbsp; * 增加面向ubuntu 8.04的版本，也就是支持GLIBC2.7的版本 \n\r\n\r&nbsp;&nbsp;&nbsp; * 重写了配置类，以增加程序的兼容性 \n\r\n\r&nbsp;&nbsp;&nbsp; * 增加关闭文件的快捷键：Ctrl+Z \n\r\n\r&nbsp;&nbsp;&nbsp; * 将网站搬到http://code.google.com/p/litebook-project/","版本历史","scr\\version_history.htm");