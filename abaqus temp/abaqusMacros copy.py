# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def sangun1():
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
    plugins.yuankongxing.yuankong_fun.yuankong(partname_k='yzg', alf_k='35', 
        R_k='10', Dh_k='100', gunfeng_k='2', yanshen_k='5')
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['yzg']
    a1.Instance(name='yzg-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=208.611, 
        farPlane=318.168, width=143.366, height=61.0605, viewOffsetX=7.11746, 
        viewOffsetY=-0.673441)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=200.521, 
        farPlane=327.734, width=137.806, height=58.6926, cameraPosition=(
        -15.8144, 97.1441, 243.667), cameraUpVector=(0.0745844, 0.924083, 
        -0.374845), cameraTarget=(-46.5401, 0.947429, 0.40521), 
        viewOffsetX=6.84144, viewOffsetY=-0.647325)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=185.276, 
        farPlane=339.85, width=196.35, height=83.6272, viewOffsetX=8.44449, 
        viewOffsetY=-1.16967)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.rotate(instanceList=('yzg-1', ), axisPoint=(-50.0, 0.0, 0.0), 
        axisDirection=(0.0, 0.0, -10.0), angle=90.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=165.858, 
        farPlane=321.3, width=165.226, height=70.371, viewOffsetX=5.78774, 
        viewOffsetY=-3.44289)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('yzg-1', ), vector=(50.0, 50.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=161.625, 
        farPlane=321.632, width=235.304, height=100.218, viewOffsetX=64.7887, 
        viewOffsetY=10.6417)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['yzg']
    a1.Instance(name='yzg-2', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=294.065, 
        farPlane=458.12, width=122.632, height=52.23, viewOffsetX=15.2717, 
        viewOffsetY=-17.1882)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.rotate(instanceList=('yzg-2', ), axisPoint=(-50.0, 0.0, 0.0), 
        axisDirection=(0.0, 0.0, -10.0), angle=-30.0)
    session.viewports['Viewport: 1'].view.setValues(width=130.832, height=55.7223, 
        viewOffsetX=16.339, viewOffsetY=-17.11)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('yzg-2', ), vector=(6.6987, -25.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['yzg']
    a1.Instance(name='yzg-3', part=p, dependent=ON)
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['yzg']
    a1.Instance(name='yzg-4', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    del a.features['yzg-4']
    session.viewports['Viewport: 1'].view.setValues(width=436.896, height=186.078, 
        viewOffsetX=0.84169, viewOffsetY=0.134789)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.rotate(instanceList=('yzg-3', ), axisPoint=(-50.0, 0.0, 0.0), 
        axisDirection=(0.0, 0.0, -10.0), angle=30.0)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('yzg-3', ), vector=(93.3013, -25.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    p = mdb.models['Model-1'].parts['yzg']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)


