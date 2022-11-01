# -*- coding: UTF-8-*-
# -*- coding: mbcs -*-

import sys
sys.dont_write_bytecode = True

from abaqusGui import *
# 导入自定义工具集
from newToolsetGui import NewToolsetGui
from newCanvasToolsetGui import NewCanvasToolsetGui
from newSelectionToolsetGui import NewSelectionToolsetGui
from newQueryToolsetGui import NewQueryToolsetGui
import os.path, os
class MainWindow(AFXMainWindow):

	def __init__(self, app, title = '三辊轧制自动建模系统'):
		
		# 调用父类的构造方法
		AFXMainWindow.__init__(self, app, title)

		# 注册标准abaqus/CAE自带的工具集
		self.registerToolset(FileToolsetGui(), 			GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		self.registerToolset(ModelToolsetGui(), 		GUI_IN_MENUBAR)
		self.registerToolset(ViewManipToolsetGui(), 	GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		self.registerToolset(AnnotationToolsetGui(),	GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		self.registerToolset(DatumToolsetGui(),  		GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE)
		self.registerToolset(EditMeshToolsetGui(), 		GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE)
		self.registerToolset(TreeToolsetGui(),			GUI_IN_MENUBAR)
		self.registerToolset(CustomizeToolsetGui(), 	GUI_IN_TOOL_PANE)
		# 注册帮助工具集	
		self.registerHelpToolset(HelpToolsetGui(), 		GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		# 注册插件程序，不用加self.
		registerPluginToolset()
		
		# 注册自定义的工具集
		self.registerToolset(NewToolsetGui(), 			GUI_IN_MENUBAR | GUI_IN_TOOLBAR | GUI_IN_TOOLBOX)

		# self.registerToolset(CanvasToolsetGui(), 		GUI_IN_MENUBAR)                   
		self.registerToolset(NewCanvasToolsetGui(), 	GUI_IN_MENUBAR)
		
		# self.registerToolset(SelectionToolsetGui(), 	GUI_IN_TOOLBAR)                   
		self.registerToolset(NewSelectionToolsetGui(), 	GUI_IN_TOOLBAR)
		
		# self.registerToolset(QueryToolsetGui(),		GUI_IN_TOOLBAR | GUI_IN_TOOL_PANE)
		self.registerToolset(NewQueryToolsetGui(),		GUI_IN_TOOLBAR | GUI_IN_TOOL_PANE)

		# 第一个参数为模块名，第二个参数为同级文件
		# 注册自定义模块'Beam Module'、'New Step'和自带模块
		self.registerModule('轧制系统',  	'myModuleGui')
		self.registerModule('Part',         	'Part')
		self.registerModule('Property',     	'Property')
		self.registerModule('Assembly',     	'Assembly')
		# self.registerModule('Step',         	'Step')
		# self.registerModule('New Step',     	'newStepGui')
		self.registerModule('Interaction',  	'Interaction')
		self.registerModule('Load',         	'Load')
		self.registerModule('Mesh',         	'Mesh')
		self.registerModule('Job',          	'Job')
		self.registerModule('Visualization',	'Visualization')
		self.registerModule('Sketch',       	'Sketch')

		# 更改工作目录。 此处有更新，详见课程第16讲
		workDir = os.getcwd()
		newWorkDir = os.path.abspath(os.path.join(workDir, 'abaqus temp'))
		mainWindow = getAFXApp().getAFXMainWindow()
		mainWindow.setWorkDirectory(newWorkDir)
