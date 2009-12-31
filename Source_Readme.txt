如果你想从源码运行LiteBook的话，那么下面是一些注意事项。

1. 需要的Python Module和文件：
    wxPython 2.8.10.1 unicode
    chardet 1.01 (http://chardet.feedparser.org/)
    rarfile 1.0 (http://pypi.python.org/pypi/rarfile/1.0)
    另外
    Windows版：unrar2, http://code.google.com/p/py-unrar2/
    Linux版：unrar linux版，http://www.rarlab.com


2. LiteBook所包含的文件
    运行时包括的文件：
	－Litebook.py
	 - icon/
	 - LiteBook_Readme.txt


3. LiteBook的配置文件
    LiteBook的配置文件名是litebook.ini，位置是
        * Windows版是在C:\Documents and Settings\【USER】\Application Data下，这里的【USER】是你Windows的登录名
        * Linux版的文件名是.litebook.ini是在运行用户的HOME目录下 
    
		
4. 授权
    本软件的主要授权采用的是Apache 2.0的许可证，具体内容参见http://www.apache.org/licenses/。  另外加上下面的内容：
    1.用户必须在衍生作品中注明来源及作者
    2.任何重新分发本作品或衍生作品的用户请发一封email到litebook.author@gmail.com告知。