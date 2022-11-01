# -*- coding: UTF-8-*-
# -*- coding: mbcs -*-  

import sys
# 不生成pyc文件
sys.dont_write_bytecode = True

# 导入abaqusGui模块，可以使用Abaqus GUI Toolkit
from abaqusGui import *
# 导入主窗口文件
from mainWindow import MainWindow

# 创建应用程序
app = AFXApp('Abaqus/CAE', '测控实验室', '三辊轧制自动建模系统', 1, 1, 1)

# 初始化刚创建的应用程序
app.init(sys.argv)

# 创建主窗口
mw = MainWindow(app)

# 创建应用程序
app.create()

# 自动进入模块
# switchMoudle('Load')
# 启动应用程序
app.run()
