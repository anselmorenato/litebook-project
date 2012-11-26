"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['litebook.py']
DATA_FILES = []
OPTIONS = {'arch':'i386','argv_emulation': True,
            'packages':['lxml',],
            'iconfile':'l2.icns',
            'plist':{'CFBundleName':'litebook','CFBundleShortVersionString':'3.0','CFBundleGetInfoString':'litebook 3.0','CFBundleExecutable':'litebook',},
          }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
