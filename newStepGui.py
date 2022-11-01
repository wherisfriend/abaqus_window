# -*- coding: UTF-8 -*-
# -*- coding: mbcs -*-  

import sys
sys.dont_write_bytecode = True

from abaqusGui import *
from newStepToolsetGui import NewStepToolsetGui

class NewStepGui(StepGui):

    def __init__(self):

        StepGui.__init__(self)

        self.registerToolset(NewStepToolsetGui(), GUI_IN_MENUBAR|GUI_IN_TOOLBAR|GUI_IN_TOOLBOX)

NewStepGui() 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 类名					模块名称
# PartGui 				"Part" 
# PropertyGui 			"Property" 
# AssemblyGui 			"Assembly" 
# StepGui 				"Step" 
# InteractionGui 		"Interaction" 
# LoadGui 				"Load" 
# MeshGui 				"Mesh" 
# OptimizationGui 		"Optimization" 
# JobGui 				"Job" 
# VisualizationGui		"Visualization" 
# SketchGui 			"Sketch" 
