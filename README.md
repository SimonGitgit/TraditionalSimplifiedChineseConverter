# TraditionalSimplifiedChineseConverter
Converter from and to Traditional and Simplified Chinese with Changjie input code

Environment:
Windows

Procedure:
1. Just download the exe
2. open the exe

Input: 
1. highlight traditional chinese text
2. press Ctrl + Alt to convert it to simplified chinese text
3. press Alt + x to terminate exe

Function:
1. Press key to convert traditional to simplified chinese
2. the converted text is also copy to the clipboard
3. If the traditional Chinese input text has only one character, it will open up a browser to check its Changjie code

https://zhuanlan.zhihu.com/p/442768333
基本流程
virtualenv envname #创建新的虚拟环境
cd envname # 进入虚拟环境目录
cd Scripts # 进入虚拟环境的Scripts文件夹中
activate # 激活虚拟环境
pip install pyinstaller # 安装打包工具pyinstaller
pip install pypiwin32 # 安装打包工具相关依赖
pip install python-packages # 安装python程序中需要引入的外部包
将需要打包的python文件或文件夹复制到Scripts目录中（该步骤也可以不用执行）
pyinstaller -F py文件路径
切换到Scripts目录下，执行deactivate，取消激活虚拟环境
打包结束，exe文件存放在dist文件夹中
