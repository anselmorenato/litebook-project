from distutils.core import setup
import glob
import py2exe
import os,sys

manifest = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1"
manifestVersion="1.0">
<assemblyIdentity
    version="0.64.1.0"
    processorArchitecture="x86"
    name="Controls"
    type="win32"
/>
<description>Your Application</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
"""

"""
installs manifest and icon into the .exe
but icon is still needed as we open it
for the window icon (not just the .exe)
changelog and logo are included in dist
"""
sys.argv.append('py2exe')

setup(windows=[{'script':'litebook.py',"icon_resources": [(1, "litebook.ico")]}],
data_files=[('icon', glob.glob('icon/*.*')),"LiteBook_Readme.txt","litebook.exe.manifest","litebook.ico","unrar.dll"],
options = {'py2exe': {'bundle_files': 1,'compressed':2,'optimize':2}},
zipfile = None,


)