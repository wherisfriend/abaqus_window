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


def zhisanjiaokong(partname, d,  Dh, yanshen ):
    r = str(float(d)/2)
    Rh = str(float(Dh)/2) 
    
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.ConstructionLine(point1=(-15.0, 0.0), point2=(22.5, 0.0))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.ConstructionLine(point1=(35.0, 0.0), point2=(35.0, 7.5))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.ConstructionLine(point1=(45.0, 0.0), point2=(45.0, 8.75))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.FixedConstraint(entity=g[3])
    s.CircleByCenterPerimeter(center=(50.0, 0.0), point1=(50.0, -5.0))
    s.CoincidentConstraint(entity1=v[0], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[5])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.567, 
        farPlane=202.557, width=177.38, height=79.2214, cameraPosition=(
        0.491597, -0.122718, 188.562), cameraTarget=(0.491597, -0.122718, 0))
    s.Line(point1=(35.0, 10.0), point2=(35.0, -10.0128374099731))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.ParallelConstraint(entity1=g[4], entity2=g[7], addUndoState=False)
    s.CoincidentConstraint(entity1=v[2], entity2=g[4], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=166.737, height=74.4681, 
        cameraPosition=(3.00147, 0.452617, 188.562), cameraTarget=(3.00147, 
        0.452617, 0))
    s.RadialDimension(curve=g[6], textPoint=(56.0988960266113, 6.65477418899536), 
        radius=5.0)
    s.VerticalDimension(vertex1=v[2], vertex2=v[3], textPoint=(31.9253044128418, 
        -7.80588436126709), value=20.0)
    s.SymmetryConstraint(entity1=v[2], entity2=v[3], symmetryAxis=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=176.196, 
        farPlane=200.928, width=156.733, height=70, cameraPosition=(7.26973, 
        0.921748, 188.562), cameraTarget=(7.26973, 0.921748, 0))
    s.DistanceDimension(entity1=g[4], entity2=g[5], textPoint=(46.8084297180176, 
        16.6695308685303), value=15.0)
    d[2].setValues(value=5, )
    session.viewports['Viewport: 1'].view.setValues(nearPlane=178.907, 
        farPlane=198.217, width=122.369, height=54.6524, cameraPosition=(
        13.5748, -0.171626, 188.562), cameraTarget=(13.5748, -0.171626, 0))
    s.Line(point1=(35.0, 10.0), point2=(30.0, 15.0))
    s.Line(point1=(30.0, 15.0), point2=(0.0, 15.0))
    s.HorizontalConstraint(entity=g[9], addUndoState=False)
    s.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, 15.0), point2=(0.0, -14.9603357315063))
    s.VerticalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, -14.9603357315063), point2=(30.0, -14.9603357315063))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
    s.Line(point1=(30.0, -14.9603357315063), point2=(35.0, -10.0))
    s.AngularDimension(line1=g[9], line2=g[8], textPoint=(29.391206741333, 
        13.0931882858276), value=120.0)
    s.AngularDimension(line1=g[12], line2=g[11], textPoint=(28.2812824249268, 
        -13.7135124206543), value=120.0)
    s.EqualLengthConstraint(entity1=g[8], entity2=g[12])
    session.viewports['Viewport: 1'].view.setValues(width=115.027, height=51.3733, 
        cameraPosition=(14.7943, -0.93011, 188.562), cameraTarget=(14.7943, 
        -0.93011, 0))
    s.ObliqueDimension(vertex1=v[4], vertex2=v[2], textPoint=(35.0, 
        13.2317266464233), value=8.0)
    s.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(22.7496891021729, 
        20.5242614746094), value=40.0)
    session.viewports['Viewport: 1'].view.setValues(width=122.369, height=54.6524, 
        cameraPosition=(13.2584, -2.08342, 188.562), cameraTarget=(13.2584, 
        -2.08342, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='r', path='dimensions[2]', expression=r)
    s.Parameter(name='Rh', path='dimensions[6]', expression=Rh, 
        previousParameter='r')
    s.Parameter(name='a', path='dimensions[1]', expression='4*r*sin(60)', 
        previousParameter='Rh')
    session.viewports['Viewport: 1'].view.setValues(width=130.18, height=58.1409, 
        cameraPosition=(11.3102, -2.41723, 188.562), cameraTarget=(11.3102, 
        -2.41723, 0))
    s.delete(objectList=(g[6], ))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='yanshen', path='dimensions[5]', expression=yanshen, 
        previousParameter='a')
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[2])
    p = mdb.models['Model-1'].Part(name=partname, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts[partname]
    p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=161.507, 
        farPlane=293.753, width=187.919, height=83.928, viewOffsetX=2.54336, 
        viewOffsetY=1.18946)
    p = mdb.models['Model-1'].parts[partname]
    p.ReferencePoint(point=(0.0, 0.0, 0.0))
