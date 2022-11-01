# -*- coding: UTF-8 -*-
# -*- coding: mbcs -*-  

import sys
sys.dont_write_bytecode = True

from abaqusGui import *
from plugins.welcome.welcomeForm import WelcomeForm

# 继承CanvasToolsetGui
class NewCanvasToolsetGui(CanvasToolsetGui):

	def __init__(self):

		# 显式地调用父类的构造方法
		CanvasToolsetGui.__init__(self)

		# 得到菜单的句柄
		menubar = getAFXApp().getAFXMainWindow().getMenubar()
		
		# 得到菜单标题view的句柄
		viewTitle = getWidgetFromText(menubar, 'View')

		# 得到下拉菜单的句柄
		viewMenu = viewTitle.getMenu()

		# 获得的菜单项的句柄，并隐藏
		getWidgetFromText(viewMenu, 'Save...').hide()
		getWidgetFromText(viewMenu, 'Parallel').hide()
		getWidgetFromText(viewMenu, 'Perspective').hide()

		# 得到下拉菜单中的第一、二条分隔线，并隐藏
		getSeparator(viewMenu, 1).hide()
		getSeparator(viewMenu, 2).hide()

		# 创建图标
		icon = afxCreatePNGIcon(r"icons\picIcon.PNG")

		# 创建菜单项
		welcomeItem = AFXMenuCommand(self, viewMenu, 'Welcome to Abaqus v1', icon, WelcomeForm(self), AFXMode.ID_ACTIVATE)
		
		# 得到某菜单项的句柄
		refItem = getWidgetFromText(viewMenu, 'Part Display Options...')
		
		# 放置新的菜单项
		welcomeItem.linkAfter(refItem)

		# 创建分隔线
		newSep = FXMenuSeparator(viewMenu)
		
		# 放置分隔线
		newSep.linkBefore(welcomeItem)

		# 修改菜单名称
		viewTitle.setText('Our &View')

		# 不要忘记在主窗口中进行注册：
		# self.registerToolset(NewCanvasToolsetGui(), 	GUI_IN_MENUBAR)

