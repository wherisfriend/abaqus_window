# -*- coding: UTF-8-*-
# -*- coding: mbcs -*-

import sys
sys.dont_write_bytecode = True

from abaqusGui import *
# �����Զ��幤�߼�
from newToolsetGui import NewToolsetGui
from newCanvasToolsetGui import NewCanvasToolsetGui
from newSelectionToolsetGui import NewSelectionToolsetGui
from newQueryToolsetGui import NewQueryToolsetGui
import os.path, os
class MainWindow(AFXMainWindow):

	def __init__(self, app, title = '���������Զ���ģϵͳ'):
		
		# ���ø���Ĺ��췽��
		AFXMainWindow.__init__(self, app, title)

		# ע���׼abaqus/CAE�Դ��Ĺ��߼�
		self.registerToolset(FileToolsetGui(), 			GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		self.registerToolset(ModelToolsetGui(), 		GUI_IN_MENUBAR)
		self.registerToolset(ViewManipToolsetGui(), 	GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		self.registerToolset(AnnotationToolsetGui(),	GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		self.registerToolset(DatumToolsetGui(),  		GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE)
		self.registerToolset(EditMeshToolsetGui(), 		GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE)
		self.registerToolset(TreeToolsetGui(),			GUI_IN_MENUBAR)
		self.registerToolset(CustomizeToolsetGui(), 	GUI_IN_TOOL_PANE)
		# ע��������߼�	
		self.registerHelpToolset(HelpToolsetGui(), 		GUI_IN_MENUBAR | GUI_IN_TOOLBAR)
		# ע�������򣬲��ü�self.
		registerPluginToolset()
		
		# ע���Զ���Ĺ��߼�
		self.registerToolset(NewToolsetGui(), 			GUI_IN_MENUBAR | GUI_IN_TOOLBAR | GUI_IN_TOOLBOX)

		# self.registerToolset(CanvasToolsetGui(), 		GUI_IN_MENUBAR)                   
		self.registerToolset(NewCanvasToolsetGui(), 	GUI_IN_MENUBAR)
		
		# self.registerToolset(SelectionToolsetGui(), 	GUI_IN_TOOLBAR)                   
		self.registerToolset(NewSelectionToolsetGui(), 	GUI_IN_TOOLBAR)
		
		# self.registerToolset(QueryToolsetGui(),		GUI_IN_TOOLBAR | GUI_IN_TOOL_PANE)
		self.registerToolset(NewQueryToolsetGui(),		GUI_IN_TOOLBAR | GUI_IN_TOOL_PANE)

		# ��һ������Ϊģ�������ڶ�������Ϊͬ���ļ�
		# ע���Զ���ģ��'Beam Module'��'New Step'���Դ�ģ��
		self.registerModule('����ϵͳ',  	'myModuleGui')
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

		# ���Ĺ���Ŀ¼�� �˴��и��£�����γ̵�16��
		workDir = os.getcwd()
		newWorkDir = os.path.abspath(os.path.join(workDir, 'abaqus temp'))
		mainWindow = getAFXApp().getAFXMainWindow()
		mainWindow.setWorkDirectory(newWorkDir)
