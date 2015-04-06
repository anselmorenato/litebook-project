


# 常见问题 #

## 运行相关 ##

### 启动litebook 时报错怎么办？ ###
> 请尝试如下办法：
    * 如果是windows下，点击程序组内的“恢复到缺省配置启动”链接；如果是linux下，执行“python litebook2\_linux.py -reset"
    * 删除litebook.ini后重新运行，litebook.ini的位置：
      * Windows版是在C:\Documents and Settings\【USER】\Application Data（注意：这是一个隐藏文件夹）下，这里的【USER】是你Windows的登录名
      * 1.4版之前 Linux版的名称也是litebook.ini，在litebook的目录下
      * 1.4版之后 Linux版的名称为改为.litebook.ini，存放在用户的HOME目录下，这样修改之后每个Linux用户都可以和Windows版一样，有自己独立的配置文件了。
    * 如果还不行的话，建议升级到最新版试试。

### 为什么litebook无法在我的操作系统上运行？ ###
  * litebook目前在如下平台上提供能够直接运行的软件包：
    * Windows XP/Vista/7
    * ubuntu linux下可以以源码形式运行
  * 理论上，litebook可以以源码的形式运行在其他Linux软件平台上，但需要安装一些第三方的软件包。所需软件包的列表，请参见源代码中的Readme文件。<br>
<ul><li>MAC OSX下可以以源码形式运行（自3.0开始）<br>
</li><li>至于xxBSD就没打算支持，因为那些系统本来就不是用来做桌面应用的。<br>
</li><li>如果litebook连源码形式都无法在你的操作系统运行的话，那么只有最后一招：你自己Hack吧。<br></li></ul>

<h3>如何以源码形式运行litebook？</h3>
<ul><li>Linux下参见这篇<a href='http://code.google.com/p/litebook-project/wiki/RunUnderLinux'>WIKI</a>
</li><li>OSX下参见这篇<a href='http://code.google.com/p/litebook-project/wiki/RunUnderOSX'>WIKI</a></li></ul>





<h3>为什么我把Linux版的litebook升级到1.4之后，我的配置都消失了？</h3>
<blockquote>这是因为1.4版之后，Linux版的配置文件名称改为.litebook.ini，存放在用户的HOME目录下了。所以你只要将原来目录中的litebook.ini拷贝到HOME下，并改为.litebook.ini，就可以实现平滑升级了。</blockquote>

<h2>使用相关</h2>

<h3>为什么我无法打开ZIP/RAR中UMD/JAR/ZIP/RAR？</h3>
<blockquote>目前的版本暂不支持，不过计划在将来支持打开ZIP/RAR文件中UMD和JAR文件<br>
2009-06-21更新：回头一想，UMD和JAR本身都已经是压缩格式了，再压缩一遍没什么意思，所以这个功能暂时不打算做了。</blockquote>


<h2>功能相关</h2>

<h3>能不能在将来的版本中增加 行间距/当前行高亮/页边距/全行下划线 功能？</h3>
<blockquote>已经在2.0中实现（除当前行高亮）</blockquote>


<h3>能不能在将来的版本中增加xxx功能？</h3>
<blockquote>优先推荐你使用Google Code的<a href='http://code.google.com/p/litebook-project/issues/list'>Issues系统</a>，其次也可以发信到litebook.author@gmail.com。我会尽力，但是无法保证每个要求都能得到满足。</blockquote>

<h3>我发现一个Bug</h3>
<blockquote>请先升级到最新版看看Bug是否已经修复，如果没有的话，优先推荐你使用Google Code的<a href='http://code.google.com/p/litebook-project/issues/list'>Issues系统</a>，其次也可以写信到litebook.author@gmail.com，包括你的操作系统及版本，litebook的版本，错误情况描述等等，越具体越好。</blockquote>


<h2>其它</h2>
<h3>litebook是免费软件吗？</h3>
<blockquote>是的，你无需为使用它而支付任何费用。</blockquote>

<h3>litebook是开源软件吗？</h3>
<blockquote>是的，源代码已经放进 google code中的 SVN。</blockquote>

<h3>你为什么要写这么一个软件？</h3>
<blockquote>我平时没事的时候也喜欢在电脑上看看闲书，但是总觉得找不到一个能让我完全满意的看书软件，所以就自己写了一个。</blockquote>

<h3>litebook是用什么语言写的？</h3>
<blockquote>python+wxpython