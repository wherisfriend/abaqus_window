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
from plugins.husanjiaov22.husanjiaov22Form import Husanjiaov22Form
from plugins.yuankongxing.yuankongxingForm import YuankongxingForm
from plugins.zhisanjiaokongv2.zhisanjiaokongv2Form import Zhisanjiaokongv2Form

class NewToolsetGui(AFXToolsetGui):

	# 分配插件ID，这些ID是类属性，调用时要加类名或self.
	[
		ID_YuKongXing, 
		ID_ZhiKongXing,
		ID_HuKongXing, 
		ID_BeamMesh, 
		ID_BeamMaxValue
		
	] = range(AFXToolsetGui.ID_LAST, AFXToolsetGui.ID_LAST + 5)

	# 定义构造方法。如不新建实例属性，可只填self，也能继承父类的实例属性
	def __init__(self):

		# 显式调用父类AFXToolsetGui的构造方法
		AFXToolsetGui.__init__(self, 'ZG Create')

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		# 将消息类型、ID与方法做映射
		FXMAPFUNC(self, SEL_COMMAND, self.ID_YuKongXing, 	self.onYuanKongXing)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_ZhiKongXing, 		self.onZhiKongXing)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_HuKongXing, 	self.onHuKongXing)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_BeamMesh, 		self.onBeamMesh)
		FXMAPFUNC(self, SEL_COMMAND, self.ID_BeamMaxValue, 	self.onBeamMaxValue)
		



		# 创建图标
		beamCreateIcon 			= afxCreatePNGIcon(r'icons\zzg3.PNG')
		beamCreateIconSmall 	= afxCreatePNGIcon(r'icons\yzg3.PNG')
		beamLoadIcon 			= afxCreatePNGIcon(r'icons\hzg3.PNG')
		beamMeshIcon 			= afxCreatePNGIcon(r'icons\beamMeshLight.PNG')
		yuanKongXingIcon	= afxCreatePNGIcon(r'icons\yzg.PNG')
		zhiKongXingIcon		= afxCreatePNGIcon(r'icons\pzg.PNG')
		huKongXingIcon			= afxCreatePNGIcon(r'icons\hzg.PNG')

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建菜单栏并添加4+1个菜单项
		newMenu = AFXMenuPane(self)
		AFXMenuTitle(self, '&ZG_create', beamCreateIconSmall, newMenu)
		AFXMenuCommand(self, newMenu, 'YZG &Create', 	yuanKongXingIcon 	, YuankongxingForm(self), 	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'PZG &create',	zhiKongXingIcon, Zhisanjiaokongv2Form(self), 	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'HZG &create',	huKongXingIcon, Husanjiaov22Form(self), 	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'Beam &Load',   	beamLoadIcon 	, BeamLoadForm(self),   	AFXMode.ID_ACTIVATE)
		AFXMenuCommand(self, newMenu, 'YZG &Create',   	beamMeshIcon 	, BeamMeshForm(self),   	AFXMode.ID_ACTIVATE)


		# 创建子菜单并添加4+1个子菜单项
		newSubMenu = AFXMenuPane(self)
		AFXMenuCascade(self, newMenu, 	 'ZG_create', 	zhiKongXingIcon , newSubMenu)
		AFXMenuCommand(self, newSubMenu, 'YZG &Create', 	yuanKongXingIcon, self,	NewToolsetGui.ID_YuKongXing)
		AFXMenuCommand(self, newSubMenu, 'PZG &create',   	zhiKongXingIcon, self,	NewToolsetGui.ID_ZhiKongXing)
		AFXMenuCommand(self, newSubMenu, 'HZG &create', 	huKongXingIcon, self, NewToolsetGui.ID_HuKongXing)
		
		# 创建welcome菜单项
		Welcome_plugin = WelcomeForm(self)
		AFXMenuCommand(self, newMenu, 'Welcome to Abaqus', afxCreatePNGIcon(r'icons\picIcon.PNG'),
											Welcome_plugin, AFXMode.ID_ACTIVATE)

		# 子菜单放在welcome之前
		welcomeItem = getWidgetFromText(newMenu, 'Welcome to Abaqus')
		newSubMenu.linkBefore(welcomeItem)

		# 创建和放置分隔线
		newSep = FXMenuSeparator(newMenu)
		newSep.linkBefore(welcomeItem)

		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		
		# 创建工具条的组件
		beamToolbar = AFXToolbarGroup(owner = self, title = 'ZG Create1')
		# 创建工具条的按钮
		AFXToolButton(beamToolbar, '\tYZG &Create', 		yuanKongXingIcon,	YuankongxingForm(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbar, '\tPZG &Create', 		zhiKongXingIcon,	Zhisanjiaokongv2Form(self), 	AFXMode.ID_ACTIVATE)
		AFXToolButton(beamToolbar, '\tHZG &Create', 	huKongXingIcon, 	Husanjiaov22Form(self), AFXMode.ID_ACTIVATE)
		# AFXToolButton(beamToolbar, '\tBeam Mesh', 		beamMeshIcon 	,	BeamMeshForm(self), 	AFXMode.ID_ACTIVATE)
		# AFXToolButton(beamToolbar, '\tBeam MaxValue', 	yuanKongXingIcon, 	BeamMaxValueForm(self), AFXMode.ID_ACTIVATE)
		
		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# 创建工具箱的组件
		beamToolbox = AFXToolboxGroup(self)
		# 创建工具箱的按钮
		AFXToolButton(beamToolbox, '\tWelcome to Abaqus', afxCreatePNGIcon(r'icons\picIconBig.png'),\
											Welcome_plugin, AFXMode.ID_ACTIVATE)

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	# 定义实例方法，用于激活功能组件
	def onYuanKongXing(self, sender, sel, ptr):
		YuanKongXing = YuankongxingForm(self)
		YuankongxingForm.activate(YuanKongXing)
		return True

	def onZhiKongXing(self, sender, sel, ptr):
		ZhiKongXing = Zhisanjiaokongv2Form(self)
		Zhisanjiaokongv2Form.activate(ZhiKongXing)
		return True
		
	def onHuKongXing(self, sender, sel, ptr):
		HuKongXing = Husanjiaov22Form(self)
		Husanjiaov22Form.activate(self.HuKongXing)
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


