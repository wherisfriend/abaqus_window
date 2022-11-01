# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by 14415 on Wed Jul  6 13:58:47 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=187.8466796875, 
    height=197.333343505859)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
import plugins.beamCreate.beamCreate
from caeModules import *
import os
os.chdir(r"D:\abaqus_2021_tmp\Abaqus MainWindow GUI\abaqus temp")
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
import plugins.beamCreate.beamCreate
import plugins.beamLoad.beamLoad
import plugins.beamMesh.beamMesh
import plugins.beamMaxValue.beamMaxValue
import plugins.husanjiaov22.hujiaokongv22
import plugins.zhisanjiaokongv2.zhisanjiaokong_fun
import plugins.yuankongxing.yuankong_fun
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
import plugins.beamCreate.beamCreate
execfile('D:/abaqus_2021_tmp/SecondDevelop/abaqu_k1.py', __main__.__dict__)
session.viewports['Viewport: 1'].view.setValues(nearPlane=568.648, 
    farPlane=764.181, width=674.413, height=297.887, viewOffsetX=83.5553, 
    viewOffsetY=-10.6478)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('pzg1-1', 'pzg1-2', 'pzg1-3', ))
p1 = mdb.models['Model-1'].parts['pzg1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['pzg1']
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
    farPlane=327.734, width=137.806, height=58.6926, cameraPosition=(-15.8144, 
    97.1441, 243.667), cameraUpVector=(0.0745844, 0.924083, -0.374845), 
    cameraTarget=(-46.5401, 0.947429, 0.40521), viewOffsetX=6.84144, 
    viewOffsetY=-0.647325)
session.viewports['Viewport: 1'].view.setValues(nearPlane=185.276, 
    farPlane=339.85, width=196.35, height=83.6272, viewOffsetX=8.44449, 
    viewOffsetY=-1.16967)
a1 = mdb.models['Model-1'].rootAssembly
a1.rotate(instanceList=('yzg-1', ), axisPoint=(-50.0, 0.0, 0.0), 
    axisDirection=(0.0, 0.0, -10.0), angle=90.0)
#: The instance yzg-1 was rotated by 90. degrees about the axis defined by the point -50., 0., 0. and the vector 0., 0., -10.
session.viewports['Viewport: 1'].view.setValues(nearPlane=165.858, 
    farPlane=321.3, width=165.226, height=70.371, viewOffsetX=5.78774, 
    viewOffsetY=-3.44289)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('yzg-1', ), vector=(50.0, 50.0, 0.0))
#: The instance yzg-1 was translated by 50., 50., 0. with respect to the assembly coordinate system
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
#: The instance yzg-2 was rotated by -30. degrees about the axis defined by the point -50., 0., 0. and the vector 0., 0., -10.
session.viewports['Viewport: 1'].view.setValues(width=130.832, height=55.7223, 
    viewOffsetX=16.339, viewOffsetY=-17.11)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('yzg-2', ), vector=(6.6987, -25.0, 0.0))
#: The instance yzg-2 was translated by 6.6987, -25., 0. with respect to the assembly coordinate system
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
#: The instance yzg-3 was rotated by 30. degrees about the axis defined by the point -50., 0., 0. and the vector 0., 0., -10.
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('yzg-3', ), vector=(93.3013, -25.0, 0.0))
#: The instance yzg-3 was translated by 93.3013, -25., 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
p = mdb.models['Model-1'].parts['yzg']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
