# -*- coding: UTF-8 -*-
# -*- coding: mbcs -*-  

import sys
sys.dont_write_bytecode = True

from abaqusGui import *
from plugins.beamCreate.beamCreateForm import BeamCreateForm
from plugins.beamLoad.beamLoadForm import BeamLoadForm
from plugins.beamMesh.beamMeshForm import BeamMeshForm
from plugins.beamMaxValue.beamMaxValueForm import BeamMaxValueForm
from plugins.welcome.welcomeForm import WelcomeForm
import os.path

class NewStepToolsetGui(AFXToolsetGui):

	# 分配插件ID，这些ID是类属性，调用时要加类名或self.
	[
		ID_BeamCreate, 
		ID_BeamLoad, 
		ID_BeamMesh, 
		ID_BeamMaxValue
	] = range(AFXToolsetGui.ID_LAST + 4, AFXToolsetGui.ID_LAST + 8)
		
	def __init__(self):

		# 显式调用父类AFXToolsetGui的构造方法
		AFXToolsetGui.__init__(self, 'Step toolbar' )

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		# 将消息类型、ID与方法做映射
		FXMAPFUNC(self, SEL_COMMAND, self.ID_BeamCreate, 	NewStepToolsetGui.onBeamCreate)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_BeamLoad, 		NewStepToolsetGui.onBeamLoad)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_BeamMesh, 		NewStepToolsetGui.onBeamMesh)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_BeamMaxValue, 	NewStepToolsetGui.onBeamMaxValue)

		# 获得脚本绝对路径。 
		mainWindow = getAFXApp().getAFXMainWindow()
		workDir = mainWindow.getWorkDirectory()
		dirPath = os.path.abspath(os.path.join(workDir, '..'))

		# 创建图标
		beamCreateIcon  		= afxCreateIcon(os.path.join(dirPath, 'icons', 'football.png'))
		beamCreateIconSmall  	= afxCreateIcon(os.path.join(dirPath, 'icons', 'footballSmall.png'))
		beamLoadIcon 			= afxCreateIcon(os.path.join(dirPath, 'icons', 'basketball.PNG'))
		beamMeshIcon 			= afxCreateIcon(os.path.join(dirPath, 'icons', 'pingpongball.PNG'))
		beamMaxValueIcon		= afxCreateIcon(os.path.join(dirPath, 'icons', 'billiardball.PNG'))
		welcomeIcon				= afxCreateIcon(os.path.join(dirPath, 'icons', 'picIcon.PNG'))
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		# 创建菜单栏并添加4个菜单项
		newMenu = AFXMenuPane(self)
		AFXMenuTitle(self, 'Ste&p Menu', beamCreateIconSmall, newMenu)
		AFXMenuCommand(self, newMenu, 'Beam &Create', 	beamCreateIcon 	, BeamCreateForm(self), 	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'Beam &Load',   	beamLoadIcon 	, BeamLoadForm(self),   	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'Beam &Mesh',   	beamMeshIcon 	, BeamMeshForm(self),   	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'Beam Max &Value',beamMaxValueIcon, BeamMaxValueForm(self), 	AFXMode.ID_ACTIVATE)
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建工具条的组件
		beamToolbar = AFXToolbarGroup(owner = self, title = 'Step toolbar')
		# 创建工具条的按钮
		AFXToolButton(beamToolbar, '\tBeam Create', 	beamCreateIcon, 	BeamCreateForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbar, '\tBeam Load', 		beamLoadIcon, 		BeamLoadForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbar, '\tBeam Mesh', 		beamMeshIcon, 		BeamMeshForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbar, '\tBeam MaxValue', 	beamMaxValueIcon, 	BeamMaxValueForm(self), AFXMode.ID_ACTIVATE)
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建工具箱的组件1
		beamToolbox1 = AFXToolboxGroup(self)
		# 创建工具箱的按钮
		AFXToolButton(beamToolbox1, '\tBeam Create', 	beamCreateIcon, 	BeamCreateForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbox1, '\tBeam Load', 		beamLoadIcon, 		BeamLoadForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbox1, '\tBeam Mesh', 		beamMeshIcon, 		BeamMeshForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbox1, '\tBeam MaxValue', 	beamMaxValueIcon, 	BeamMaxValueForm(self), AFXMode.ID_ACTIVATE)

		# 创建工具箱的组件2
		beamToolbox2 = AFXToolboxGroup(self)
		Welcome_plugin = WelcomeForm(self)
		AFXToolButton(beamToolbox2, '\tWelcome to Abaqus', welcomeIcon, 	Welcome_plugin, 		AFXMode.ID_ACTIVATE)
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	# 定义实例方法，用于激活功能组件
	def onBeamCreate(self, sender, sel, ptr):
		BeamCreate = BeamCreateForm(self)
		BeamCreateForm.activate(BeamCreate)
		return True

	def onBeamLoad(self, sender, sel, ptr):
		BeamLoad = BeamLoadForm(self)
		BeamLoadForm.activate(self.BeamLoad)
		return True

	def onBeamMesh(self, sender, sel, ptr):
		BeamMesh = BeamMeshForm(self)
		BeamMeshForm.activate(self.BeamMesh)
		return True

	def onBeamMaxValue(self, sender, sel, ptr):
		BeamMaxValue = BeamMaxValueForm(self)
		BeamMaxValueForm.activate(self.BeamMaxValue)
		return True
