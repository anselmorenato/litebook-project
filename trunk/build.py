from distutils.core import setup
import glob
import py2exe
import os,sys


sys.argv.append('py2exe')

setup(windows=[{'script':'litebook.py',"icon_resources": [(1, "litebook.ico")]}],
data_files=[('icon', glob.glob('icon/*.*')),"LiteBook_Readme.txt","litebook.exe.manifest","litebook.ico","unrar.dll"],
options = {'py2exe': {'bundle_files': 1,'compressed':2,'optimize':2}},
zipfile = "lib/library.zip",


)