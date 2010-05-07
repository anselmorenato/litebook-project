from distutils.core import setup
import glob
import py2exe
import os,sys


sys.argv.append('py2exe')

setup(windows=[{'script':'litebook.py',"icon_resources": [(1, "litebook.ico")]}],
data_files=[('icon', glob.glob('icon/*.*')),('plugin', glob.glob('plugin/*.*')),"LiteBook_Readme.txt","litebook.exe.manifest","litebook.ico","unrar.dll","LiteBook_WhatsNew.txt","bh.dat","py.dat"],
options = {'py2exe': {'bundle_files': 1,'compressed':2,'optimize':2}},
zipfile = "lib/library.zip",


)