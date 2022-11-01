# -*- coding: UTF-8 -*-
# -*- coding: mbcs -*-  

import sys
sys.dont_write_bytecode = True

from abaqusGui import * 
from plugins.welcome.welcomeForm import WelcomeForm

class NewSelectionToolsetGui(SelectionToolsetGui):

    def __init__(self):
        
        # 显式的调用父类的构造方法
        SelectionToolsetGui.__init__(self)

        # 获取名为Selection的工具条group
        selToolbar = self.getToolbarGroup('Selection')        
        
        # 把Form脚本实例化
        Welcome_plugin = WelcomeForm(self)

        # 创建图标
        welIcon = afxCreatePNGIcon(r'icons\picIcon.PNG')
        
        # 创建按钮
        welButton = AFXToolButton(selToolbar, '\tWelcome to Abaqus', welIcon, Welcome_plugin, AFXMode.ID_ACTIVATE)

        # 把按钮移动位置
        refBut = getWidgetFromText(selToolbar, 'Enable Selection')
        welButton.linkAfter(refBut)
        
        # 创建垂直分隔线
        newSep = FXVerticalSeparator(selToolbar)
        newSep.linkAfter(refBut)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 类名                        名称                 位置
# AmplitudeToolsetGui         "Amplitude"         GUI_IN_TOOL_PANE  
# AnnotationToolsetGui        "Annotation"        GUI_IN_MENUBAR | GUI_IN_TOOLBAR 
# CanvasToolsetGui            "Canvas"            GUI_IN_MENUBAR 
# CustomizeToolsetGui         "Customize"         GUI_IN_TOOL_PANE 
# DatumToolsetGui             "Datum"             GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE  
# EditMeshToolsetGui          "Mesh Editor"       GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE  
# FileToolsetGui              "File"              GUI_IN_MENUBAR | GUI_IN_TOOLBAR 
# HelpToolsetGui              "Help"              GUI_IN_MENUBAR | GUI_IN_TOOLBAR 
# ModelToolsetGui             "Model"             GUI_IN_MENUBAR 
# PartitionToolsetGui         "Partition"         GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE  
# QueryToolsetGui             "Query"             GUI_IN_TOOLBAR | GUI_IN_TOOL_PANE  
# RegionToolsetGui            "Region"            GUI_IN_TOOL_PANE  
# RepairToolsetGui            "Repair"            GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE  
# SelectionToolsetGui         "Selection"         GUI_IN_TOOLBAR 
# TreeToolsetGui              "Tree"              GUI_IN_MENUBAR 
# ViewManipToolsetGui         "View Manipulation" GUI_IN_MENUBAR | GUI_IN_TOOLBAR 
