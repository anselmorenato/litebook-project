LiteBook在MAC OSX下面只能以python源码形式运行,步骤如下：
  * 从官方网站的SVN中获取最新的源代码，或是在官方网站的下载页面下载源码版。从svn中checkout源码的方法：svn checkout http://litebook-project.googlecode.com/svn/trunk/2.0-Dev/single litebook3

  * 确认你的系统中安装有如下python环境：
    * Python 2.7（不支持python 3.0）
    * wxpython 2.8 unicode for python 2.7 (http://wxpython.org/download.php#stable)
      * 注意：如果在安装时遇到”... is damaged and can’t be opened. You should eject the disk image."错误，请使用如下命令安装："sudo installer -pkg /Volumes/<path-to-wxpython.pkg> -target /"
    * twisted (推荐采用mac port安装: sudo port install py-twisted)

  * 在litebook的目录下运行“bash lb3\_osx"