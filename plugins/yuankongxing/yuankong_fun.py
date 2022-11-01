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

# alf取值为40°~30°
# 轧辊直径 Dh_k
# 扩张圆角
# 弧长半径R:
# gunfeng_k辊缝宽度
# yanshen_k延伸长度

def yuankong(partname_k, Dh_k, yanshen_k, gunfeng_k, alf_k, R_k):
   
    gunfeng_k = str(float(gunfeng_k)/2)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=172.438, 
        farPlane=292.172, width=119.396, height=53.3247, viewOffsetX=14.9994, 
        viewOffsetY=0.635175)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.ConstructionLine(point1=(-15.0, 0.0), point2=(33.75, 0.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.HorizontalConstraint(entity=g[3])
    session.viewports['Viewport: 1'].view.setValues(width=166.737, height=74.4681, 
        cameraPosition=(1.07188, 0.0877759, 188.562), cameraTarget=(1.07188, 
        0.0877759, 0))
    s.FixedConstraint(entity=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.636, 
        farPlane=206.487, width=227.192, height=101.468, cameraPosition=(
        -2.45205, -2.94078, 188.562), cameraTarget=(-2.45205, -2.94078, 0))
    s.Spot(point=(0.0, 0.0))
    s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.486, 
        farPlane=197.637, width=101.638, height=45.3934, cameraPosition=(
        -1.17088, -2.24684, 188.562), cameraTarget=(-1.17088, -2.24684, 0))
    s.Spot(point=(0.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=180.165, 
        farPlane=196.959, width=106.429, height=47.5333, cameraPosition=(
        -0.360306, -3.52082, 188.562), cameraTarget=(-0.360306, -3.52082, 0))
    s.undo()
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=176.139, 
        farPlane=200.985, width=157.456, height=70.3228, cameraPosition=(
        -3.84569, -2.96179, 188.562), cameraTarget=(-3.84569, -2.96179, 0))
    s.Spot(point=(0.0, 0.0))
    s.FixedConstraint(entity=v[0])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=160.136, 
        farPlane=216.988, width=360.285, height=160.91, cameraPosition=(
        0.960329, -14.2277, 188.562), cameraTarget=(0.960329, -14.2277, 0))
    s.ConstructionLine(point1=(0.0, 0.0), point2=(-15.0, 15.0))
    s.CoincidentConstraint(entity1=v[0], entity2=g[4], addUndoState=False)
    s.ConstructionLine(point1=(0.0, 0.0), point2=(30.0, 13.75))
    s.CoincidentConstraint(entity1=v[0], entity2=g[5], addUndoState=False)
    s.undo()
    s.AngularDimension(line1=g[4], line2=g[3], textPoint=(14.8488788604736, 
        6.88025856018066), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=172.935, 
        farPlane=204.188, width=198.057, height=88.456, cameraPosition=(
        6.64477, -6.1702, 188.562), cameraTarget=(6.64477, -6.1702, 0))
    s.ConstructionLine(point1=(0.0, 0.0), point2=(12.5, 15.0))
    s.CoincidentConstraint(entity1=v[0], entity2=g[5], addUndoState=False)
    s.AngularDimension(line1=g[5], line2=g[3], textPoint=(15.7392196655273, 
        -2.19024229049683), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=167.491, 
        farPlane=209.633, width=267.064, height=119.276, cameraPosition=(
        -4.77716, -7.47175, 188.562), cameraTarget=(-4.77716, -7.47175, 0))
    s.ConstructionLine(point1=(0.0, 0.0), point2=(-16.25, 12.5))
    s.CoincidentConstraint(entity1=v[0], entity2=g[6], addUndoState=False)
    s.AngularDimension(line1=g[6], line2=g[4], textPoint=(-11.7414112091064, 
        15.4310064315796), value=35.0)
    s.ArcByCenterEnds(center=(0.0, 0.0), point1=(-16.25, 20.0), point2=(-16.25, 
        -20.0), direction=COUNTERCLOCKWISE)
    s.SymmetryConstraint(entity1=v[1], entity2=v[2], symmetryAxis=g[3])
    s.CoincidentConstraint(entity1=v[1], entity2=g[6])
    s.Line(point1=(-23.3550170954494, 10.890623327949), point2=(-16.8981303091641, 
        24.7374617260648))
    s.TangentConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.Line(point1=(-16.8981303091641, 24.7374617260648), point2=(-27.5, 38.75))
    s.Line(point1=(-23.3550170954494, -10.890623327949), point2=(-17.9102683257079, 
        -22.566924745086))
    s.TangentConstraint(entity1=g[7], entity2=g[10], addUndoState=False)
    s.Line(point1=(-17.9102683257079, -22.566924745086), point2=(-27.5, -36.25))
    s.PerpendicularConstraint(entity1=g[8], entity2=g[6])
    s.SymmetryConstraint(entity1=g[8], entity2=g[10], symmetryAxis=g[3])
    s.SymmetryConstraint(entity1=g[9], entity2=g[11], symmetryAxis=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=169.145, 
        farPlane=207.979, width=246.095, height=109.911, cameraPosition=(
        -7.54493, -0.730781, 188.562), cameraTarget=(-7.54493, -0.730781, 0))
    s.ParallelConstraint(entity1=g[9], entity2=g[4])
    s.DistanceDimension(entity1=g[9], entity2=g[4], textPoint=(-26.3787269592285, 
        40.4334678649902), value=2.0)
    s.RadialDimension(curve=g[7], textPoint=(-30.9825401306152, 7.97570514678955), 
        radius=15.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=163.591, 
        farPlane=213.533, width=316.493, height=141.352, cameraPosition=(
        -24.4088, -6.8028, 188.562), cameraTarget=(-24.4088, -6.8028, 0))
    s.ConstructionLine(point1=(-60.0, 0.0), point2=(-60.0, 33.9545364379883))
    s.VerticalConstraint(entity=g[12], addUndoState=False)
    s.VerticalConstraint(entity=g[12])
    s.Line(point1=(-24.3037612511618, 38.095349302036), point2=(-60.0, 
        38.0953493020429))
    s.HorizontalConstraint(entity=g[13], addUndoState=False)
    s.CoincidentConstraint(entity1=v[8], entity2=g[12], addUndoState=False)
    s.Line(point1=(-60.0, 38.0953493020429), point2=(-60.0, -37.885871887207))
    s.VerticalConstraint(entity=g[14], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
    s.CoincidentConstraint(entity1=v[9], entity2=g[12], addUndoState=False)
    s.Line(point1=(-60.0, -37.885871887207), point2=(-24.3037612511618, 
        -38.095349302036))
    s.SymmetryConstraint(entity1=g[13], entity2=g[15], symmetryAxis=g[3])
    session.viewports['Viewport: 1'].view.setValues(width=336.695, height=150.374, 
        cameraPosition=(-25.0043, -10.1819, 188.562), cameraTarget=(-25.0043, 
        -10.1819, 0))
    s.DistanceDimension(entity1=g[12], entity2=g[2], textPoint=(-15.2585144042969, 
        46.3161010742188), value=60.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=169.77, 
        farPlane=207.354, width=210.45, height=93.9909, cameraPosition=(
        -32.0228, 5.99952, 188.562), cameraTarget=(-32.0228, 5.99952, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='alf', path='dimensions[2]', expression=alf_k)
    s.Parameter(name='R', path='dimensions[4]', expression=R_k, 
        previousParameter='alf')
    s.Parameter(name='gunfeng_half', path='dimensions[3]', expression=gunfeng_k, 
        previousParameter='R')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=164.493, 
        farPlane=212.631, width=269.549, height=120.386, cameraPosition=(
        -36.1437, 8.09458, 188.562), cameraTarget=(-36.1437, 8.09458, 0))
    s.ObliqueDimension(vertex1=v[5], vertex2=v[4], textPoint=(-10.9308013916016, 
        29.3794708251953), value=8.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=162.957, 
        farPlane=214.167, width=286.754, height=128.07, cameraPosition=(
        -46.2245, 6.88906, 188.562), cameraTarget=(-46.2245, 6.88906, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='yanshen', path='dimensions[6]', expression=yanshen_k, 
        previousParameter='gunfeng_half')
    s.parameters['alf'].setValues(expression=alf_k)
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='Dh', expression=Dh_k, previousParameter='yanshen')
    s.Parameter(name='Rh', path='dimensions[5]', expression='Dh/2', 
        previousParameter='Dh')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=165.937, 
        farPlane=211.187, cameraPosition=(-46.2245, 6.97496, 188.562), 
        cameraTarget=(-46.2245, 6.97496, 0))
    s.sketchOptions.setValues(constructionGeometry=ON)
    session.viewports['Viewport: 1'].view.setValues(width=269.549, height=120.386, 
        cameraPosition=(-47.5413, 7.39861, 188.562), cameraTarget=(-47.5413, 
        7.39861, 0))
    s.assignCenterline(line=g[12])
    p = mdb.models['Model-1'].Part(name=partname_k, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts[partname_k]
    p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname_k]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=190.751, 
        farPlane=348.154, width=216.975, height=96.9053, viewOffsetX=2.89655, 
        viewOffsetY=0.170354)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=197.768, 
        farPlane=348.183, width=224.957, height=100.47, cameraPosition=(
        179.496, 7.80443, 147.686), cameraUpVector=(-0.367144, 0.921705, 
        -0.125158), cameraTarget=(-47.2072, -4.7538, 2.58939), 
        viewOffsetX=3.0031, viewOffsetY=0.17662)
    p = mdb.models['Model-1'].parts[partname_k]
    p.ReferencePoint(point=(-float(Dh_k)/2, 0.0, 0.0))
    #创建坐标系，YZG1圆轧辊
    r = p.referencePoints
    p.DatumCsysByThreePoints(origin=r[2], name='YZG1', coordSysType=CARTESIAN, 
    point1=(0.0, 0.0, 0.0), point2=(5.0, 0.0, -1.0))

    # 去除实体，保留壳体
    p = mdb.models['Model-1'].parts[partname_k]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts[partname_k]
    c1 = p.cells
    p.RemoveCells(cellList = c1[0:1])


