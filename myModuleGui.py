# -*- coding: UTF-8 -*-
# -*- coding: mbcs -*-  
# 自定义模块

import sys
sys.dont_write_bytecode = True

from abaqusGui import *
from plugins.beamMaxValue.beamMaxValueForm import BeamMaxValueForm
from plugins.welcome.welcomeForm import WelcomeForm
from plugins.husanjiaov22.husanjiaov22Form import Husanjiaov22Form
from plugins.yuankongxing.yuankongxingForm import YuankongxingForm
from plugins.zhisanjiaokongv2.zhisanjiaokongv2Form import Zhisanjiaokongv2Form
from plugins.K1huzg.k1huzgForm import K1huzgForm
from plugins.k1yuanzg.k1yuanzgForm import K1yuanzgForm
from plugins.k1zhizg.k1zhizgForm import K1zhizgForm
import os.path

class MyModuleGui(AFXModuleGui):

	def __init__(self):

		# 显式调用父类AFXModuleGui的构造方法
		AFXModuleGui.__init__(self, '轧制&系统', AFXModuleGui.PART)

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# 获得主窗口的句柄
		mainWindow = getAFXApp().getAFXMainWindow()

		# 确保模型树可用和可见
		mainWindow.appendApplicableModuleForTreeTab('Model', self.getModuleName())
		mainWindow.appendVisibleModuleForTreeTab('Model', self.getModuleName())
		# 确保结果树可用和可见
		mainWindow.appendApplicableModuleForTreeTab('Results', self.getModuleName())
		mainWindow.appendVisibleModuleForTreeTab('Results', self.getModuleName())
		
		# 使用绝对路径创建图标。 此处有更新，详见课程第16讲
		dirPath = mainWindow.getWorkDirectory()
		# mainWindow.writeToMessageArea('The work directory is {0}'.format(dirPath))

		beamMaxValueIcon		= afxCreateIcon(os.path.join(dirPath, 'icons', 'beamMaxValueIcon.PNG'))
		welcomeIcon				= afxCreateIcon(os.path.join(dirPath, 'icons', 'picIcon.PNG'))
		hzg3Icon				= afxCreateIcon(os.path.join(dirPath, 'icons', 'hzg3.PNG'))
		yzg3Icon				= afxCreateIcon(os.path.join(dirPath, 'icons', 'yzg3.PNG'))
		pzg3Icon				= afxCreateIcon(os.path.join(dirPath, 'icons', 'zzg3.PNG'))
		hzgIcon					= afxCreateIcon(os.path.join(dirPath, 'icons', 'hzg.PNG'))
		yzgIcon					= afxCreateIcon(os.path.join(dirPath, 'icons', 'yzg.PNG'))
		pzgIcon					= afxCreateIcon(os.path.join(dirPath, 'icons', 'pzg.PNG'))
		logoIcon 				= afxCreateIcon(os.path.join(dirPath, 'icons', 'zzg3.PNG'))

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建菜单栏并添加4个菜单项
		moduleMenu = AFXMenuPane(self)
		AFXMenuTitle(self, 'ZG Mo&dule0', logoIcon, moduleMenu)  #更新：快捷键改成了“d”，详见课程第16讲
		AFXMenuCommand(self, moduleMenu, 'yzg &Create', 	yzgIcon 	, YuankongxingForm(self), 	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, moduleMenu, 'pzg &Create',   	pzgIcon 	, Zhisanjiaokongv2Form(self),   	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, moduleMenu, 'hzg &Create',   	hzgIcon 	, Husanjiaov22Form(self),   	AFXMode.ID_ACTIVATE)	
		# 创建子菜单并添加4个子菜单项
		moduleSubMenu = AFXMenuPane(self)
		AFXMenuCascade(self, moduleMenu, 	'K1_ZG Module1', 	logoIcon, moduleSubMenu)
		AFXMenuCommand(self, moduleSubMenu, 'yzg3 &Create', 	yzg3Icon 	, K1yuanzgForm(self), 	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, moduleSubMenu, 'pzg3 &Create',   	pzg3Icon 	, K1zhizgForm(self),   	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, moduleSubMenu, 'hzg3 &Create',   	hzg3Icon 	, K1huzgForm(self),   	AFXMode.ID_ACTIVATE)

		
		# 创建welcome菜单项
		Welcome_plugin = WelcomeForm(self)
		AFXMenuCommand(self, moduleMenu, 'Welcome to Abaqus',welcomeIcon,
											Welcome_plugin, AFXMode.ID_ACTIVATE)

		# 子菜单放在welcome之前
		welcomeItem = getWidgetFromText(moduleMenu, 'Welcome to Abaqus')
		moduleSubMenu.linkBefore(welcomeItem)

		# 创建和放置分隔线
		newSep1 = FXMenuSeparator(moduleMenu)
		newSep1.linkBefore(welcomeItem)

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建工具条的组件
		beamModuleToolbar = AFXToolbarGroup(owner = self, title = 'ZG Module3')
		# 创建工具条的按钮，这里的\t，是鼠标停留时的提示
		AFXToolButton(beamModuleToolbar, '\tyzg &Create', 		yzgIcon, 	YuankongxingForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbar, '\tpzg &Create', 		pzgIcon, 	Zhisanjiaokongv2Form(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbar, '\thzg &Create', 		hzgIcon, 	Husanjiaov22Form(self), 	AFXMode.ID_ACTIVATE)

		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建工具箱的组件
		beamModuleToolbox = AFXToolboxGroup(self)
		# 创建工具箱的按钮
		AFXToolButton(beamModuleToolbox, '\tyzg &Createx', 		yzgIcon, 	YuankongxingForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbox, '\tpzg &Createx', 		pzgIcon, 	Zhisanjiaokongv2Form(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbox, '\thzg &Createx', 		hzgIcon, 	Husanjiaov22Form(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbox, '\tyzg3 &Create', 		yzg3Icon,   K1yuanzgForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbox, '\tpzg3 &Create',   	pzg3Icon, 	K1zhizgForm(self),   	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamModuleToolbox, '\thzg3 &Create',   	hzg3Icon, 	K1huzgForm(self),   	AFXMode.ID_ACTIVATE)
		
	
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建飞出工具箱的组件
		beamModuleToolbox_Flyout = AFXToolboxGroup(self)
		# 创建popup组件
		beamModulePopup = FXPopup(mainWindow)

		# 创建飞出图标的按钮
		# AFXFlyoutItem(beamModulePopup, '\tBeam Create m', 	yzgIcon, 	YuankongxingForm(self), 	AFXMode.ID_ACTIVATE)
		# AFXFlyoutItem(beamModulePopup, '\tBeam Load m', 		pzgIcon, 		Zhisanjiaokongv2Form(self), 	AFXMode.ID_ACTIVATE)
		# AFXFlyoutItem(beamModulePopup, '\tBeam Mesh m', 		hzgIcon, 		Husanjiaov22Form(self), 	AFXMode.ID_ACTIVATE)

		
		# 生成飞出图标按钮
		# AFXFlyoutButton(beamModuleToolbox_Flyout, beamModulePopup)

		# 创建和放置分隔线
		refBox = getWidgetFromText(beamModuleToolbox, 'hzg &Createx')
		newSep2 = FXHorizontalSeparator(beamModuleToolbox)
		newSep2.linkAfter(refBox)

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		# 更改工作目录
		curDir = mainWindow.getWorkDirectory()
		workDir= os.path.join(curDir, 'abaqus temp')
		mainWindow.setWorkDirectory(workDir)

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	# 导入内核脚本，该方法会自动调用
	def getKernelInitializationCommand(self):
		return   'import plugins.beamCreate.beamCreate\
				\nimport plugins.beamLoad.beamLoad\
				\nimport plugins.beamMesh.beamMesh\
				\nimport plugins.beamMaxValue.beamMaxValue\
				\nimport plugins.husanjiaov22.hujiaokongv22\
				\nimport plugins.zhisanjiaokongv2.zhisanjiaokong_fun\
				\nimport plugins.yuankongxing.yuankong_fun\
				\nimport plugins.K1huzg.huzgk1script\
				\nimport plugins.k1yuanzg.yuanzgk1script\
				\nimport plugins.k1zhizg.pingzgk1script'

	# 打印出当前Module的欢迎语句
	def onPrintModuleName(moduleName):
		moduleName = getCurrentModuleGui().getModuleName()
		getAFXApp().getAFXMainWindow().writeToMessageArea('Now we switch to the module : {0}.'.format(moduleName))

	# 执行欢迎语句的命令
	setSwitchModuleHook(onPrintModuleName)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 当调用这个脚本，自动实例化这个类
MyModuleGui()
