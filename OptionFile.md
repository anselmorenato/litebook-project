

# litebook配置文件详述 #

本文详细描述了litebook配置文件内各个配置项的使用方法。
注：本文内容适用于版本1.70或之前。


## 文件名和位置 ##

  * Windows版是在C:\Documents and Settings\【USER】\Application Data（注意：这是一个隐藏文件夹）下，这里的【USER】是你Windows的登录名；文件名是litebook.ini
  * 1.4版之前 Linux版的名称也是litebook.ini，在litebook的目录下
  * 1.4版之后 Linux版的名称为改为.litebook.ini，存放在用户的HOME目录下，

## 综述 ##
  * litebook的配置文件是文本文件格式，可以用任意编辑器修改。
  * 配置文件内容分为几大配置类别，每个配置类别都以`[`xxx`]`开头，如`[`settings`]`。
  * 每个配置类别里面都有很多配置项，配置项的格式都是"xxx = yyy"，xxx是配置项，yyy是配置项的值。每个配置项占一行
  * 配置文件都是unix换行格式（windows版也是如此），也就是说每行都是以"\n"结尾的。在windows版下最好用支持unix换行格式的编辑器进行修改（如ultraedit,ulipad等等）


## 配置项详述 ##
以下配置项详述按照配置类别展开。

### BookDB ###
  * 此配置类别里面存放都是已阅读文件的最后阅读位置。
  * xxx是文件内容或文件标题的md5值，yyy是最后阅读位置。每一行代表一个文件。
  * 此大类最多可存放的文件数受![settings](settings.md)里面的maxbookdb控制，缺省为50个。
  * 注：从ver1.51起，此部分内容被litebook.bookdb文件替代，其格式为sqlite3。

### BookMark ###
  * 此配置类别里面存放的是已保存的书签
  * xxx是书签的编号，yyy是书签的内容，格式为：文件路径?阅读位置?预览内容；如果是压缩文件（或UMD/JAR格式）的话，那么格式为：压缩文件路径|压缩包内实际文件名?阅读位置?预览内容。


### settings ###
  * 此配置类别里面存放的是一般控制选项如下。
  * showfullscreen：启动时是否自动全屏（此配置项在ver1.52中被取消）
  * autoscrollinterval：自动翻页间隔，以毫秒为单位，缺省是12秒
  * maxopenedfiles：“曾经打开文件”菜单中的文件个数，缺省是5个
  * enableesc：是否启用ESC作为老板键，only for windows version
  * maxbookdb：控制"BookDB"中的条目个数
  * enablesidebarpreview：在文件选择侧边栏中是否启用预览
  * loadlastfile：启动时是否自动载入上次阅读的文件
  * remindinterval：阅读时间提醒，单位是分钟，缺省为60分钟
  * lastdir：记录最后浏览文件的目录
  * vercheckonstartup：是否在启动时检查版本更新
  * hashtitle：是否启用文件名作为md5hash的内容，如果否的话，则使用文件内容作。
  * showallfileinsidebar: 是否在文件侧边栏中显示所有文件，否则为否的话，只显示已支持格式的文件
  * defaultsavedir: 缺省下载保存的目录
  * lastweb: 最后一次选择的网站插件
  * lastwebsearchkeyword: 最后一次网站搜索的关键字
  * hidetoolbar: 是否隐藏工具栏
  * proxyserver: HTTP代理服务器地址
  * proxyport: HTTP代理服务器端口
  * proxyuser: HTTP代理服务器认证用户名
  * proxypass: HTTP代理服务器认证密码
  * useproxy: 是否启用代理服务器
  * defaultactionupondownloadfinished: 文件下载完成后采取的动作
  * numberofthreads: 每个下载任务并发的线程数

### Appearance ###
  * 此配置类别内存放的是字体颜色显示方案的配置
  * xxx是方案名，yyy是方案内容，其格式为：字体大小:font family:style:weight:underline:facename:encoding:字体颜色:背景颜色
  * 方案名为"last"代表最后运行时所使用的显示方案

### LastOpenedFiles ###
  * 此配置类别存放的是“曾经打开文件”的菜单内容
  * xxx是菜单编号，yyy是文件路径，如果是压缩文件（或UMD/JAR格式）的话，那么格式为：压缩文件路径|压缩包内实际文件名

### LastPosition ###
  * 此配置类别存放的是最后一次所打开的文件和阅读位置
  * lastfile:最后打开文件的路径，如果是压缩文件（或UMD/JAR格式）的话，那么格式为：压缩文件路径|压缩包内实际文件名
  * pos：最后阅读位置