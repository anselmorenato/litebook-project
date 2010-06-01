@echo off 
del build /q /f
del dist /q /f

"C:\Python26\python.exe" build.py 

cd dist

 
"C:\Program Files\upx303w\upx.exe" --best *.* 

copy litebook.exe g:\readbook\ /Y