# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by 14415 on Wed Jul  6 21:16:09 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import math
import sys
sys.path.insert(10, 
    r'd:/abaqus_2021_tmp/Abaqus MainWindow GUI/abaqus temp/abaqus_plugins/zhisanjiaokongv2')
import zhisanjiaokong_fun

def k1_zhizg(partname_k, yanshen_k, gunfeng_k, d_k, Dh_k):
    zhisanjiaokong_fun.zhisanjiaokongv2(partname_k, yanshen_k, gunfeng_k, d_k, Dh_k)

    du = math.pi/180
    Rh_k = float(Dh_k)/2
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[partname_k]
    a.Instance(name='yzg-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=212.132, 
        farPlane=319.072, width=127.533, height=56.9588, viewOffsetX=1.42122, 
        viewOffsetY=-0.543148)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=206.026, 
        farPlane=324.31, width=123.863, height=55.3193, cameraPosition=(
        -57.335, 141.498, 224.007), cameraUpVector=(0.0255554, 0.846029, 
        -0.532524), cameraTarget=(-46.6707, -0.104327, -0.446836), 
        viewOffsetX=1.38031, viewOffsetY=-0.527514)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=205.273, 
        farPlane=325.063, width=144.388, height=64.4864, viewOffsetX=2.01257, 
        viewOffsetY=0.67954)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=203.399, 
        farPlane=327.526, width=143.07, height=63.8977, cameraPosition=(
        -27.0953, 140.37, 224.461), cameraUpVector=(0.0211263, 0.847119, 
        -0.530984), cameraTarget=(-46.7116, 0.0446565, -0.191139), 
        viewOffsetX=1.9942, viewOffsetY=0.673337)
    a = mdb.models['Model-1'].rootAssembly
    a.rotate(instanceList=('yzg-1', ), axisPoint=(-Rh_k, 0.0, 0.0), axisDirection=(
        0.0, 0.0, -10.0), angle=90.0)
    session.viewports['Viewport: 1'].view.setValues(width=125.887, height=56.2237, 
        viewOffsetX=1.27453, viewOffsetY=0.587077)
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('yzg-1', ), vector=(Rh_k, Rh_k, 0.0))
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[partname_k]
    a.Instance(name='yzg-2', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(width=246.697, height=110.179, 
        viewOffsetX=-0.169607, viewOffsetY=-1.16321)
    a = mdb.models['Model-1'].rootAssembly
    a.rotate(instanceList=('yzg-2', ), axisPoint=(-Rh_k, 0.0, 0.0), axisDirection=(
        0.0, 0.0, -10.0), angle=-30.0)
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('yzg-2', ), vector=(Rh_k-Rh_k*(math.sin(60*du)), -Rh_k/2, 0.0))
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[partname_k]
    a.Instance(name='yzg-3', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    a.rotate(instanceList=('yzg-3', ), axisPoint=(-Rh_k, 0.0, 0.0), axisDirection=(
        0.0, 0.0, -10.0), angle=30.0)
    session.viewports['Viewport: 1'].view.setValues(width=373.542, height=166.831, 
        viewOffsetX=-6.4744, viewOffsetY=-1.00549)
    a = mdb.models['Model-1'].rootAssembly
    a.translate(instanceList=('yzg-3', ), vector=(Rh_k+Rh_k*(math.sin(60*du)), -Rh_k/2, 0.0))
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])


# k1_yuanzg(partname_k=partname_k, alf_k='35', R_k='10', Dh_k='150', gunfeng_k='2', yanshen_k='7')