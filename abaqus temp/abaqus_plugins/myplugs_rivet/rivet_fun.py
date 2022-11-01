# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def rivet_function(partname, d1, d2, h1, h2):
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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s.FixedConstraint(entity=g[2])
    s.Line(point1=(0.0, 27.5), point2=(17.5, 27.5))
    s.HorizontalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
    s.Line(point1=(17.5, 27.5), point2=(17.5, 21.25))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(17.5, 21.25), point2=(11.25, 21.25))
    s.HorizontalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(11.25, 21.25), point2=(11.25, -7.5))
    s.VerticalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(11.25, -7.5), point2=(16.25, -7.5))
    s.HorizontalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s.Line(point1=(16.25, -7.5), point2=(16.25, -20.0))
    s.VerticalConstraint(entity=g[8], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s.Line(point1=(16.25, -20.0), point2=(0.0, -20.0))
    s.HorizontalConstraint(entity=g[9], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    s.CoincidentConstraint(entity1=v[7], entity2=g[2], addUndoState=False)
    s.Line(point1=(0.0, -20.0), point2=(0.0, 27.5))
    s.VerticalConstraint(entity=g[10], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    s.ConstructionLine(point1=(-35.0, 0.0), point2=(8.75, 0.0))
    s.HorizontalConstraint(entity=g[11], addUndoState=False)
    s.SymmetryConstraint(entity1=g[3], entity2=g[9], symmetryAxis=g[11])
    s.SymmetryConstraint(entity1=g[5], entity2=g[7], symmetryAxis=g[11])
    s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(3.24306488037109, 
        32.9594383239746), value=30.0)
    s.DistanceDimension(entity1=g[6], entity2=g[2], textPoint=(1.91029357910156, 
        13.7072219848633), value=18.5)
    s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(35.6736831665039, 
        24.6197700500488), value=10.0)
    s.ObliqueDimension(vertex1=v[3], vertex2=v[4], textPoint=(35.6736831665039, 
        8.20658874511719), value=40.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=165.509, 
        farPlane=211.615, width=303.944, height=130.495, cameraPosition=(
        -26.4527, -7.32222, 188.562), cameraTarget=(-26.4527, -7.32222, 0))
    s.EqualLengthConstraint(entity1=g[8], entity2=g[4])
    s.EqualLengthConstraint(entity1=g[9], entity2=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=165.509, 
        farPlane=211.615, cameraPosition=(-25.449, -6.16117, 188.562), 
        cameraTarget=(-25.449, -6.16117, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='D1', path='dimensions[0]', expression=d1)
    s.Parameter(name='D2', path='dimensions[1]', expression=d2, 
        previousParameter='D1')
    s.Parameter(name='H1', path='dimensions[3]', expression=h1, 
        previousParameter='D2')
    s.Parameter(name='H2', path='dimensions[2]', expression=h2, 
        previousParameter='H1')
    s=mdb.models['Model-1'].sketches['__profile__']
    s.sketchOptions.setValues(constructionGeometry=ON)
    s.assignCenterline(line=g[2])
    p = mdb.models['Model-1'].Part(name=partname, dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts[partname]
    p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


