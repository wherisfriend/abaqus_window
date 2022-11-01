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
# d_k = str(float(10))
# Dh_k = str(float(100))
# bate_k = str(float(40)) 100

def husanjiaov22(partname_k, d_k, bate_k, Dh_k, yanshen_k, gunfeng_k):
    gunfeng_k = str(float(gunfeng_k)/2)
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s1.FixedConstraint(entity=g[2])
    s1.ConstructionLine(point1=(-20.0, 0.0), point2=(8.75, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.ConstructionLine(point1=(0.0, 0.0), point2=(-5.0, 5.0))
    s1.ConstructionLine(point1=(0.0, 0.0), point2=(5.0, 5.0))
    s1.FixedConstraint(entity=g[3])
    session.viewports['Viewport: 1'].view.setValues(width=147.329, height=65.8, 
        cameraPosition=(-1.70061, -0.00266144, 188.562), cameraTarget=(
        -1.70061, -0.00266144, 0))
    s1.Spot(point=(0.0, 0.0))
    s1.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=185.19, 
        farPlane=191.934, width=37.7661, height=16.867, cameraPosition=(
        0.304686, -0.341401, 188.562), cameraTarget=(0.304686, -0.341401, 0))
    s1.FixedConstraint(entity=v[0])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=182.301, 
        farPlane=194.823, width=79.3538, height=35.4409, cameraPosition=(
        4.38287, 0.377584, 188.562), cameraTarget=(4.38287, 0.377584, 0))
    s1.AngularDimension(line1=g[4], line2=g[3], textPoint=(4.83272075653076, 
        1.02890586853027), value=120.0)
    s1.AngularDimension(line1=g[5], line2=g[3], textPoint=(3.66310787200928, 
        -1.57638072967529), value=120.0)
    s1.CoincidentConstraint(entity1=v[0], entity2=g[4])
    s1.CoincidentConstraint(entity1=g[5], entity2=v[0])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=175.353, 
        farPlane=201.771, width=147.932, height=66.0692, cameraPosition=(
        -3.98212, 1.38153, 188.562), cameraTarget=(-3.98212, 1.38153, 0))
    s1.ConstructionLine(point1=(-15.0, 20.0), point2=(-15.0, -8.75))
    s1.VerticalConstraint(entity=g[6], addUndoState=False)
    s1.DistanceDimension(entity1=g[6], entity2=g[2], textPoint=(-4.73688220977783, 
        18.2547149658203), value=5.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=182.652, 
        farPlane=194.471, width=66.1796, height=29.5571, cameraPosition=(
        -0.130463, 0.891314, 188.562), cameraTarget=(-0.130463, 0.891314, 0))
    s1.ArcByCenterEnds(center=(15.0, 0.0), point1=(-2.6816029548645, 
        -8.23054313659668), point2=(-1.85623407363892, 7.80294561386108), 
        direction=CLOCKWISE)
    s1.CoincidentConstraint(entity1=v[3], entity2=g[3], addUndoState=False)
    s1.TangentConstraint(entity1=g[6], entity2=g[7])
    s1.Line(point1=(-7.5, 11.25), point2=(-4.08730454636964, 5.9728389526369))
    s1.CoincidentConstraint(entity1=v[5], entity2=g[7], addUndoState=False)
    s1.Line(point1=(-8.00898742675781, -11.7144546508789), point2=(
        -4.15664957668691, -5.74654478761118))
    s1.CoincidentConstraint(entity1=v[7], entity2=g[7], addUndoState=False)
    s1.Line(point1=(-7.5, 11.25), point2=(-20.0, 11.25))
    s1.HorizontalConstraint(entity=g[10], addUndoState=False)
    s1.Line(point1=(-20.0, 11.25), point2=(-20.0, -12.5))
    s1.VerticalConstraint(entity=g[11], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    s1.Line(point1=(-20.0, -12.5), point2=(-8.00898742675781, -11.7144546508789))
    s1.SymmetryConstraint(entity1=g[10], entity2=g[12], symmetryAxis=g[3])
    s1.CoincidentConstraint(entity1=v[2], entity2=v[5])
    s1.CoincidentConstraint(entity1=v[1], entity2=v[7])
    s1.ParallelConstraint(entity1=g[4], entity2=g[8])
    s1.EqualLengthConstraint(entity1=g[8], entity2=g[9])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=181.874, 
        farPlane=195.25, width=84.7643, height=37.8573, cameraPosition=(
        4.64061, 1.9094, 188.562), cameraTarget=(4.64061, 1.9094, 0))
    s1.ConstructionLine(point1=(-23.75, 16.25), point2=(-23.75, -6.25))
    s1.VerticalConstraint(entity=g[13], addUndoState=False)
    s1.TangentConstraint(entity1=g[13], entity2=g[11])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=177.545, 
        farPlane=199.578, width=139.625, height=62.3591, cameraPosition=(
        19.3821, 0.749603, 188.562), cameraTarget=(19.3821, 0.749603, 0))
    s1.CoincidentConstraint(entity1=g[11], entity2=v[8])
    s1.CoincidentConstraint(entity1=v[8], entity2=g[13])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=175.298, 
        farPlane=201.825, width=168.105, height=75.0787, cameraPosition=(
        25.4418, 1.20101, 188.562), cameraTarget=(25.4418, 1.20101, 0))
    s1.DistanceDimension(entity1=g[13], entity2=g[2], textPoint=(-7.14989852905273, 
        22.3733825683594), value=20.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.412, 
        farPlane=197.712, width=102.471, height=45.7656, cameraPosition=(
        11.5918, 3.43103, 188.562), cameraTarget=(11.5918, 3.43103, 0))
    s1.ObliqueDimension(vertex1=v[4], vertex2=v[2], textPoint=(-5.0, 
        10.8846216201782), value=8.0)
    s1.DistanceDimension(entity1=v[4], entity2=g[4], textPoint=(-8.79789161682129, 
        13.6688432693481), value=1.0)
    s1.ConstructionLine(point1=(10.0742601707373, 0.0), point2=(-4.10650001064053, 
        5.11266665971154))
    s1.CoincidentConstraint(entity1=v[3], entity2=g[14], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[2], entity2=g[14], addUndoState=False)
    s1.ConstructionLine(point1=(10.0742601707373, 0.0), point2=(-4.10650001064053, 
        -5.11266665971154))
    s1.CoincidentConstraint(entity1=v[3], entity2=g[15], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[1], entity2=g[15], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=183.573, 
        farPlane=193.551, width=55.8728, height=24.9538, cameraPosition=(
        10.3486, 1.6037, 188.562), cameraTarget=(10.3486, 1.6037, 0))
    s1.AngularDimension(line1=g[14], line2=g[15], textPoint=(7.40294075012207, 
        -0.341372013092041), value=40.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=184.577, 
        farPlane=192.547, width=44.6296, height=19.9324, cameraPosition=(
        4.45748, 1.11528, 188.562), cameraTarget=(4.45748, 1.11528, 0))
    s1.CoincidentConstraint(entity1=v[3], entity2=g[15])
    s1.CoincidentConstraint(entity1=v[3], entity2=g[14])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=180.561, 
        farPlane=196.563, width=101.404, height=45.2887, cameraPosition=(
        -1.27231, 4.79147, 188.562), cameraTarget=(-1.27231, 4.79147, 0))
    s1.RadialDimension(curve=g[7], textPoint=(-8.74536323547363, 4.01657247543335), 
        radius=14.9173979808356)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=183.959, 
        farPlane=193.165, width=58.3414, height=26.0564, cameraPosition=(
        -2.59944, -0.627299, 188.562), cameraTarget=(-2.59944, -0.627299, 0))
    s1.delete(objectList=(c[41], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.696, 
        farPlane=197.428, width=99.2915, height=44.3454, cameraPosition=(
        -4.03639, 2.97676, 188.562), cameraTarget=(-4.03639, 2.97676, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='d', expression=d_k)
    s.Parameter(name='r', path='dimensions[2]', expression='d/2', 
        previousParameter='d')
    s.Parameter(name='bate', path='dimensions[6]', expression=bate_k, 
        previousParameter='r')
    s.Parameter(name='Dh', expression=Dh_k, previousParameter='bate')
    s.Parameter(name='Rh', path='dimensions[3]', expression='Dh/2', 
        previousParameter='Dh')
    s.Parameter(name='yanshen', path='dimensions[4]', expression=yanshen_k, 
        previousParameter='Rh')
    s.Parameter(name='gunfeng', path='dimensions[5]', expression=gunfeng_k, 
        previousParameter='yanshen')
    s.Parameter(name='G', expression='2*sin(60)/3+tan(bate/4)', 
        previousParameter='gunfeng')
    s.Parameter(name='a', expression='d/G', previousParameter='G')
    s.Parameter(name='R', path='dimensions[7]', expression='(a/2)/(sin(bate/2))', 
        previousParameter='a')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.13, 
        farPlane=197.994, width=119.544, height=53.3907, cameraPosition=(
        -1.20055, 3.64741, 188.562), cameraTarget=(-1.20055, 3.64741, 0))
    s1.sketchOptions.setValues(constructionGeometry=ON)
    s1.assignCenterline(line=g[13])
    p = mdb.models['Model-1'].Part(name=partname_k, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts[partname_k]
    p.BaseSolidRevolve(sketch=s1, angle=360.0, flipRevolveDirection=OFF)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname_k]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

    p.ReferencePoint(point=(-float(Dh_k)/2, 0.0, 0.0))
    #创建坐标系，HZG1弧轧辊
    r = p.referencePoints
    p.DatumCsysByThreePoints(origin=r[2], name='HZG1', coordSysType=CARTESIAN, 
    point1=(0.0, 0.0, 0.0), point2=(5.0, 0.0, -1.0))

    # 去除实体，保留壳体
    p = mdb.models['Model-1'].parts[partname_k]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts[partname_k]
    c1 = p.cells
    p.RemoveCells(cellList = c1[0:1])


