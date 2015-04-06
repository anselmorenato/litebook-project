由于各个linux系统之间的差异，litebook在linux下只提供源码版，下面是litebook在linux下的安装运行方法：

  * 从官方网站 ( http://code.google.com/p/litebook-project/) 的SVN中获取最新的源代码，或是在官方网站的 下载页面 下载源码版。
    * 从svn中checkout源码的方法：svn checkout http ://litebook-project.googlecode.com/svn/trunk/2.0-Dev/single litebook3

  * 确认你的系统中安装有如下python环境：
    * python 2.7 （不支持python 3.0）
    * wxpython 2.8 unicode (ubuntu下sudo apt-get install python-wxgtk2.8)
    * twisted (ubuntu下sudo apt-get install python-twisted)
    * netifaces (ubuntu下sudo apt-get install python-netifaces)
    * unrar linux版( http://www.rarlab.com)
      * 放在litebook所在的目录即可

  * 在Linux下，运行python litebook.py