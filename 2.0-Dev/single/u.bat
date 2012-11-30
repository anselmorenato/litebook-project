del /q /s build
del /q /s dist
python build.py
xcopy /Y /E /I kadp D:\hujun\litebook\tobuild\svn3\single\dist\kadp
xcopy /Y /E /I jieba D:\hujun\litebook\tobuild\svn3\single\dist\jieba
copy /Y mainlist.txt D:\hujun\litebook\tobuild\svn3\single\dist