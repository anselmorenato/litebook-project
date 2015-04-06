# 版本历史 #
## 2013-10-13 3.2 ##

  * 重写简繁字体转换算法，速度得到极大地提升
  * 修正一个竖排书本间距较小的排版问题
  * 竖排书本显示时，所有标点符号自动转换成竖排标点
  * 增加一个控制选项使得竖排书本显示时自动删除除句号外所有标点
  * 修正一个Windows下用右键菜单打开的BUG
  * 配置文件目录现在可以自定义了，方便把配置文件和书放在云中，详情见帮助文件

## 2013-08-07 3.1 ##
  * WEB下载新增边下载边看功能 fix [issue 45](https://code.google.com/p/litebook-project/issues/detail?id=45)
  * 新增WEB下载管理器 fix [issue 45](https://code.google.com/p/litebook-project/issues/detail?id=45)
  * 新增跳转历史, fix [issue 40](https://code.google.com/p/litebook-project/issues/detail?id=40)
  * 新增一个WEB下载插件
  * 缺省关闭WEB服务器、LTBNET和UPNP功能，启动速度加快；这些功能在完全版中支持
  * 通过命令行参数"-full"使用完全版
  * 一些其他的修正

## 2013-1-5 3.0 ##
  * 新增LTBNET，一个共享和搜索图书的点对点网络
  * 支持MAC OSX
  * Windows/Linux/OSX统一到同一套源文件
  * 更新了在线搜索和下载的插件系统，支持订阅功能
  * 更好的EPUB支持
  * 修正一个UMD的BUG (fix [issue 66](https://code.google.com/p/litebook-project/issues/detail?id=66))
  * 许多其他修正和更新



## 2011-9-15 ver2.4 ##
  * 新增章节侧边栏
  * 工具栏可缩放
  * 修正一个无法载入某些EPUB文件的BUG
  * 修正一个Linux下无法用命令行方式载入中文文件名的文件的BUG
  * 修正一个在Windows下某些情况下无法启动的BUG
  * 一些小更新

## 2011-5-17 ver2.3 ##

  * 新增转换为EPUB格式的功能
  * 新增内置WEB服务器（for Stanza and iBooks）
  * 新增基于组播DNS的自动发现功能（For Stanza）
  * 消除一些BUG
  * Linux版将所依赖的一些第三方程序一同打包 ，这样就无需另外安装了。
  * 更改了缓存目录的位置; Windows: ['USERPROFILE']\litebook\cache; Linux: ~/litebook/cache

## 2011-3-8 ver2.21 ##
  * 新增文字替换功能，缺省快捷键Ctrl+H
  * EPUB和JAR文件解码新增缓存功能，解决有大量章节时载入慢的问题（需要占用一些磁盘空间，详见本帮助文件的功能介绍-》缓存）
  * 新增自动生成章节列表功能，缺省快捷键Ctrl+U
  * 新增像窗口内拖动文件直接打开的功能
  * 消除一些BUG ([issue 28](https://code.google.com/p/litebook-project/issues/detail?id=28)/31/32/39/42)
  * 消除一个打开Rar文件中包含中文目录名出错的BUG
  * 消除一个无法保持下划线颜色的BUG

## 2011-1-16 ver2.1 ##
  * 新增如下导航快捷键：
```
      * 向上翻半页    ，
      * 向下翻半页    。
      * 后退10%      [
      * 前进10%      ]
      * 后退1%       9
      * 前进1%       0
```
  * Linux版新增工具栏进度条
  * 自动翻页的缺省快捷键改成 ALT+T
  * 消除一些BUG

## 2011-1-2 ver2.0 正式版 ##
  * 重写显示核心组建，新增三种显示模式/页面背景/页边距/行间距均可设置
  * 重写选项对话框
  * 重写帮助系统
  * 所有功能的快捷键均可配置
  * 显示方案和按键方案均可导入导出
  * 新增进度条
  * 新增windows资源管理器右键菜单和命令行选项
  * 新增恢复到缺省配置的操作
  * 修正若干BUG

## 2010-05-06 ver1.70 正式版 ##
  * 新增在文件侧边栏中输入拼音过滤当前文件列表的功能
  * 修正N个和中文路径名相关的BUG（惭愧，现在才发现）fix [issue 19](https://code.google.com/p/litebook-project/issues/detail?id=19)
  * 修正在64bit系统上打开UMD文件出错的问题. fix [issue 18](https://code.google.com/p/litebook-project/issues/detail?id=18)

## 2010-05-1 ver1.70 beta3 ##
  * 改写了导入插件的方式，使其工作更加稳定
  * 改进现有插件多线程下载能力，新增支持多个任务同时下载
  * 新增“搜索所有网站”的功能，找书更加方便
  * 新增“搜索及下载”的工具栏图标
  * 新增“重新读入插件”菜单



## 2010-03-24 ver1.70 beta2 ##
  * 大幅改进了搜索及下载功能，使用更加方便
    * 插件开发指南更新
  * 原有插件升级支持多线程下载
  * 新增一个插件
  * 修正了几个小Bug


## 2010-03-19 ver1.70 beta ##
  * 支持智能分段
  * 在线小说搜索及下载(Alt+C)
    * 支持HTTP代理（通过选项设置）
    * 可以通过插件的形式支持新的网站，插件开发指南请参见本站Wiki
  * 改进了HTML标签的过滤算法
  * fix [issue 14](https://code.google.com/p/litebook-project/issues/detail?id=14) comment 3

## 2009-12-31 ver.160 ##
  * 支持新的电子书格式EPUB. fix [issue10](https://code.google.com/p/litebook-project/issues/detail?id=10)
  * 能够记住隐藏工具栏的设置. fix [issue13](https://code.google.com/p/litebook-project/issues/detail?id=13)
  * 最大曾经打开文件的菜单数可以在选项中设置. fix [issue14](https://code.google.com/p/litebook-project/issues/detail?id=14)
  * 修正一个在某些情况下可能导致字体变化的BUG
  * 增加"帮助"－> “版本更新内容"菜单

## 2009-11-20 ver1.55 ##
  * 重写了zip/rar文件打开对话框的列表显示部分，修复了N个相关Bug
  * 重写了"上一个文件/下一个文件"的搜索算法，支持中文数字文件名（如第一章，第二章），使得阅读更加方便。
  * 提升了HTML转TEXT的准确率，新增支持将HTML Codepoint转换为相应的unicode

## 2009-10-13 ver1.54 ##
  * 修正了一个如果没有配置文件就无法启动的Bug. fix [issue 12](https://code.google.com/p/litebook-project/issues/detail?id=12)
  * 增加了一个选项控制是否在文件侧边栏中显示所有文件还是只显示已支持格式的文件
  * 在全屏显示的时候，按鼠标右键会弹出”关闭全屏"的菜单

## 2009-9-28 ver1.53 ##
  * 修正了包括如下相关的N(N>5)个Bug
    * zip/rar/umd/jar载入
    * 侧边栏/文件列表对话框

## 2009-9-25 ver1.52 ##
  * 将对文件内容哈希改为对文件名（不包括路径）哈希，也就是说具备相同文件名的文件会被认为是同一本书，从而在载入时自动跳转至上次阅读位置。fix [issue9](https://code.google.com/p/litebook-project/issues/detail?id=9)
  * 增加了“视图－》全屏显示”菜单项，快捷键为Ctrl+I
  * 取消配置文件中启动时全屏显示的配置项
  * 以往文件打开历史的对话框中文件会缺省以时间排序，最近的打开的文件排在最前面
  * 如果打开一个已经在“曾经打开的文件”菜单中的文件，那么“曾经打开的文件”菜单将不会被更新
  * 注：由于发现几个大BUG，此版本停止下载。


## 2009-8-18 ver1.51发布 ##
  * 在工具栏中新增打开侧边栏的图标 (Fix [Issue 5](https://code.google.com/p/litebook-project/issues/detail?id=5))
  * 提升文件侧边栏的显示速度 (Fix [Issue 5](https://code.google.com/p/litebook-project/issues/detail?id=5))
  * 侧边栏进入子目录，然后再返回的时候，会自动选择之前的父目录 (Fix [Issue 5](https://code.google.com/p/litebook-project/issues/detail?id=5))
  * 新增查看打开文件历史功能，所有已打开的文件历史都记录在litebook.bookdb中(Fix [Issue 3](https://code.google.com/p/litebook-project/issues/detail?id=3))

## 2009-6-26 ver1.5发布 ##
  * 新增文件选择侧边栏(Alt+D) ([Issue 5](https://code.google.com/p/litebook-project/issues/detail?id=5))
    * 侧边栏内回到上级目录快捷键：左箭头
    * 进入被选择的目录/打开被选择的文件:右箭头
    * 可以在选项菜单内设置是否在侧边栏中是否预览文件内容
  * 新增版本检查更新功能，此功能可以在选项菜单内进行设置([Issue 6](https://code.google.com/p/litebook-project/issues/detail?id=6))
  * Windows版新增选项控制是否启用ESC作为老板键





## 2009-6-17 FAQ Updated ##
[常见问题(FAQ)更新](http://code.google.com/p/litebook-project/wiki/FAQ)

## 2009-6-17 v1.4发布 ##
  * 增加隐藏工具栏的功能(Ctrl+T)
  * 为HTML过滤，转换为简体，转换为繁体字这三个功能增加快捷键（SHIFT+H/J/F）
  * 现在如果要保存的界面方案和已有方案名字相同的话，会询问是否覆盖
  * 不再允许空的界面方案名称
  * 修正Linux获取运行文件所在目录的Bug
  * 修正一个读取配置文件的Bug
  * Linux版的配置文件改名为.litebook.ini，存放在HOME下面



## 2009-6-16 源代码发布 ##

  * 请从SVN中Checkout

## 2009-6-12 v1.31发布(Only for Windows version) ##

  * 修正一个在载入某些Unicode编码的文件时，显示不完全的Bug，此Bug仅在Windows版发现，强烈推荐升级。



## 2009-6-5 v1.3发布 ##

  * 将工具栏中"简"和"繁"的图标改成背景透明的图片

  * 修正载入文件时的一个Bug

  * 增加鼠标控制功能，详情参见帮助（仅For Windows版）

  * 将ESC注册为全局性热键，按一下ESC会最小化窗口，再按一下窗口还原（仅For Windows版）


## 2009-6-3 v1.21发布 ##

  * 增加面向ubuntu 8.04的版本，也就是支持GLIBC 2.7的版本

  * 重写了配置类，以增加程序的兼容性

  * 增加关闭文件的快捷键：Ctrl+Z

  * 将网站搬到http://code.google.com/p/litebook-project/