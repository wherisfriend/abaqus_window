# -*- coding: mbcs -*-
# Do not delete the following import lines
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

# 辊缝
# partname_k = str('mmn')
# yanshen_k = str(float(9))
# gunfeng_k = str(float(2))
# d_k = str(float(30))
# Dh_k = str(float(100))

def zhisanjiaokongv2(partname_k, yanshen_k, gunfeng_k, d_k, Dh_k):
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.806, 
        farPlane=348.167, width=245.047, height=109.443, viewOffsetX=1.55311, 
        viewOffsetY=-0.355335)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.ConstructionLine(point1=(-10.0, 0.0), point2=(30.0, 0.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.ConstructionLine(point1=(-10.0, 0.0), point2=(-10.0, 10.0))
    s.VerticalConstraint(entity=g[4], addUndoState=False)

    session.viewports['Viewport: 1'].view.setValues(width=166.737, height=74.4681, 
        cameraPosition=(0.606833, -0.812636, 188.562), cameraTarget=(0.606833, 
        -0.812636, 0))
    s.FixedConstraint(entity=g[3])
    s.FixedConstraint(entity=g[4])
    s.delete(objectList=(c[6], ))
    s.DistanceDimension(entity1=g[4], entity2=g[2], textPoint=(-4.49737644195557, 
        13.0144510269165), value=50.0)
    s.ConstructionLine(point1=(-10.0, 5.0), point2=(-10.0, -12.5))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=169.492, 
        farPlane=207.631, width=241.694, height=107.945, cameraPosition=(
        2.39755, -2.6459, 188.562), cameraTarget=(2.39755, -2.6459, 0))
    s.DistanceDimension(entity1=g[5], entity2=g[2], textPoint=(-2.80901718139648, 
        9.18838691711426), value=10.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=169.492, 
        farPlane=207.631, cameraPosition=(1.18446, -2.45651, 188.562), 
        cameraTarget=(1.18446, -2.45651, 0))
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=166.98, 
        farPlane=210.143, width=273.533, height=122.165, cameraPosition=(
        2.59231, -3.67305, 188.562), cameraTarget=(2.59231, -3.67305, 0))
    s.delete(objectList=(d[0], ))
    s.Line(point1=(-10.0, 10.0), point2=(-10.0, -9.78905487060547))
    s.VerticalConstraint(entity=g[6], addUndoState=False)
    s.ParallelConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[5], addUndoState=False)
    s.CoincidentConstraint(entity1=v[1], entity2=g[5], addUndoState=False)
    s.Line(point1=(-10.0, -9.78905487060547), point2=(-15.0, -15.0))
    s.Line(point1=(-15.0, -15.0), point2=(-50.0, -15.0))
    s.HorizontalConstraint(entity=g[8], addUndoState=False)
    s.CoincidentConstraint(entity1=v[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(-50.0, -15.0), point2=(-50.0, 15.1394424438477))
    s.VerticalConstraint(entity=g[9], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
    s.Line(point1=(-50.0, 15.1394424438477), point2=(-15.0, 15.1394424438477))
    s.HorizontalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.Line(point1=(-15.0, 15.1394424438477), point2=(-10.0, 10.0))
    s.ConstructionLine(point1=(0.0, 0.0), point2=(-10.0, 15.2942886352539))
    s.ConstructionLine(point1=(0.0, 0.0), point2=(8.75, 13.75))
    s.Spot(point=(0.0, 0.0))
    s.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=290.993, height=129.963, 
        cameraPosition=(2.76058, -3.90531, 188.562), cameraTarget=(2.76058, 
        -3.90531, 0))
    s.FixedConstraint(entity=v[6])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.49, 
        farPlane=206.634, width=229.055, height=102.3, cameraPosition=(
        0.967042, -3.13519, 188.562), cameraTarget=(0.967042, -3.13519, 0))
    s.AngularDimension(line1=g[12], line2=g[3], textPoint=(5.77148580551147, 
        3.80152797698975), value=120.0)
    s.AngularDimension(line1=g[13], line2=g[3], textPoint=(4.99238729476929, 
        -3.84830570220947), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=186.489, 
        farPlane=190.634, width=23.2098, height=10.3659, cameraPosition=(
        0.726994, -1.60515, 188.562), cameraTarget=(0.726994, -1.60515, 0))
    s.CoincidentConstraint(entity1=v[6], entity2=g[12])
    s.CoincidentConstraint(entity1=g[13], entity2=v[6])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=172.396, 
        farPlane=204.727, width=204.887, height=91.5065, cameraPosition=(
        -18.5572, 4.20901, 188.562), cameraTarget=(-18.5572, 4.20901, 0))
    s.ParallelConstraint(entity1=g[12], entity2=g[11])
    s.SymmetryConstraint(entity1=g[10], entity2=g[8], symmetryAxis=g[3])
    s.SymmetryConstraint(entity1=g[11], entity2=g[7], symmetryAxis=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.22, 
        farPlane=202.904, width=160.62, height=71.7359, cameraPosition=(
        -26.8492, -1.11687, 188.562), cameraTarget=(-26.8492, -1.11687, 0))
    s.DistanceDimension(entity1=g[5], entity2=g[2], textPoint=(-5.72458457946777, 
        22.1131954193115), value=5.0)
    s.undo()
    s.VerticalDimension(vertex1=v[0], vertex2=v[1], textPoint=(-6.27091026306152, 
        2.11079168319702), value=12.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=163.531, 
        farPlane=213.592, width=317.244, height=141.687, cameraPosition=(
        -38.8357, -7.26876, 188.562), cameraTarget=(-38.8357, -7.26876, 0))
    s.DistanceDimension(entity1=g[5], entity2=g[2], textPoint=(-5.56468200683594, 
        19.5781574249268), value=10.0)
    s.DistanceDimension(entity1=g[4], entity2=g[2], textPoint=(-10.7801361083984, 
        25.683801651001), value=50.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.22, 
        farPlane=202.904, width=160.62, height=71.7359, cameraPosition=(
        -28.9425, -3.40621, 188.562), cameraTarget=(-28.9425, -3.40621, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='d', expression=d_k)
    s.Parameter(name='r', path='dimensions[4]', expression='d/2', 
        previousParameter='d')
    s.Parameter(name='a', path='dimensions[3]', expression='(2*sin(60))*d', 
        previousParameter='r')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=175.889, 
        farPlane=201.235, width=160.62, height=71.7359, cameraPosition=(
        -24.9983, 0.140408, 188.562), cameraTarget=(-24.9983, 0.140408, 0))
    s.undo()
    s.delete(objectList=(c[36], ))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='dimensions_3', path='dimensions[3]', 
        expression='2*sin(60)*d', previousParameter='r')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=177.9, 
        farPlane=199.224, width=135.13, height=60.3518, cameraPosition=(
        -22.6131, 3.56374, 188.562), cameraTarget=(-22.6131, 3.56374, 0))
    s.undo()
    s.ObliqueDimension(vertex1=v[5], vertex2=v[0], textPoint=(-10.0, 
        11.7865829467773), value=8.0)
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='yanshen', path='dimensions[6]', expression=yanshen_k, 
        previousParameter='r')
    s.Parameter(name='a', path='dimensions[3]', expression='d*2*sin(60)', 
        previousParameter='yanshen')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.738, 
        farPlane=202.386, width=175.211, height=78.2525, cameraPosition=(
        -23.4497, 5.57697, 188.562), cameraTarget=(-23.4497, 5.57697, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='gunfeng', expression=gunfeng_k, previousParameter='yanshen')
    s.parameters['a'].setValues(expression='d*2*sin(60)-2*gunfeng')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=175.407, 
        farPlane=201.717, width=166.728, height=74.4638, cameraPosition=(
        -22.7899, 4.39622, 188.562), cameraTarget=(-22.7899, 4.39622, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='Dh', expression=Dh_k, previousParameter='a')
    s.Parameter(name='Rh', path='dimensions[5]', expression='Dh/2', 
        previousParameter='Dh')
    s=mdb.models['Model-1'].sketches['__profile__']
    s.parameters['d'].setValues(expression=d_k)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=166.981, 
        farPlane=210.142, width=273.518, height=122.158, cameraPosition=(
        -9.7136, 14.8237, 188.562), cameraTarget=(-9.7136, 14.8237, 0))
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[4])
    p = mdb.models['Model-1'].Part(name=partname_k, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts[partname_k]
    p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname_k]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=181.285, 
        farPlane=339.569, width=218.28, height=97.488, viewOffsetX=0.0339117, 
        viewOffsetY=0.00637436)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.094, 
        farPlane=335.578, width=226.479, height=101.15, cameraPosition=(140.33, 
        46.0308, 173.848), cameraUpVector=(-0.334236, 0.861972, -0.38117), 
        cameraTarget=(-48.6091, -2.78358, 1.39141), viewOffsetX=0.0351855, 
        viewOffsetY=0.00661379)
    p = mdb.models['Model-1'].parts[partname_k]
    p.ReferencePoint(point=(-float(Dh_k)/2, 0.0, 0.0))
    #创建坐标系,PZG1平三角轧辊
    r = p.referencePoints
    p.DatumCsysByThreePoints(origin=r[2], name='PZG1', coordSysType=CARTESIAN, 
    point1=(0.0, 0.0, 0.0), point2=(5.0, 0.0, -1.0))

    # 去除实体，保留壳体
    p = mdb.models['Model-1'].parts[partname_k]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts[partname_k]
    c1 = p.cells
    p.RemoveCells(cellList = c1[0:1])



