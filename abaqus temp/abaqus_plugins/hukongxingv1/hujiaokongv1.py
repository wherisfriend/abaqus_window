# -*- coding: mbcs -*-
# Do not delete the following import lines

# 该文件为弧三角孔型单个生成脚本。  未设置好辊缝

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

# d:孔型内接圆直径；
# bate： β夹角
# Dh: 工作直径
# 孔型向外延伸量
def hujiaokong(partname, d, bate, Dh, yanshen ):

    r = str(float(d)/2)
    Rh = str(float(Dh)/2) 
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    s1.FixedConstraint(entity=g[2])
    s1.ConstructionLine(point1=(-12.5, 0.0), point2=(17.5, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.ConstructionLine(point1=(40.0, 0.0), point2=(40.0, 3.75))
    s1.VerticalConstraint(entity=g[4], addUndoState=False)
    s1.ConstructionLine(point1=(55.0, 0.0), point2=(55.0, 2.5))
    s1.VerticalConstraint(entity=g[5], addUndoState=False)
    s1.FixedConstraint(entity=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=171.712, 
        farPlane=205.412, width=213.561, height=95.3803, cameraPosition=(
        27.7939, 2.49282, 188.562), cameraTarget=(27.7939, 2.49282, 0))
    s1.CircleByCenterPerimeter(center=(63.75, 0.0), point1=(70.0, -5.0))
    s1.CoincidentConstraint(entity1=v[0], entity2=g[3], addUndoState=False)
    s1.RadialDimension(curve=g[6], textPoint=(61.6925048828125, 11.2571754455566), 
        radius=5.0)
    s1.CoincidentConstraint(entity1=v[0], entity2=g[5])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=168.275, 
        farPlane=208.849, width=257.121, height=114.835, cameraPosition=(
        21.5571, 4.48082, 188.562), cameraTarget=(21.5571, 4.48082, 0))
    s1.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(30.1569786071777, 
        22.6012115478516), value=60.0)
    s1.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.49, 
        farPlane=206.634, width=229.055, height=102.3, cameraPosition=(22.4369, 
        5.09857, 188.562), cameraTarget=(22.4369, 5.09857, 0))
    s1.ConstructionLine(point1=(63.75, 0.0), point2=(57.5, 7.5))
    s1.CoincidentConstraint(entity1=v[0], entity2=g[7], addUndoState=False)
    s1.ConstructionLine(point1=(63.75, 0.0), point2=(71.25, 7.5))
    s1.CoincidentConstraint(entity1=v[0], entity2=g[8], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=243.676, height=108.83, 
        cameraPosition=(19.1381, 5.29306, 188.562), cameraTarget=(19.1381, 
        5.29306, 0))
    s1.AngularDimension(line1=g[7], line2=g[3], textPoint=(73.2081604003906, 
        1.40330696105957), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(width=259.229, height=115.777, 
        cameraPosition=(15.7082, 5.96659, 188.562), cameraTarget=(15.7082, 
        5.96659, 0))
    s1.AngularDimension(line1=g[8], line2=g[3], textPoint=(72.0450286865234, 
        -4.15544033050537), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=160.693, 
        farPlane=216.431, width=312.105, height=139.392, cameraPosition=(
        28.1735, 10.6553, 188.562), cameraTarget=(28.1735, 10.6553, 0))
    s1.undo()
    s1.ArcByCenterEnds(center=(80.0, 0.0), point1=(46.25, -40.0), point2=(47.5, 
        42.5), direction=CLOCKWISE)
    s1.CoincidentConstraint(entity1=v[4], entity2=g[3], addUndoState=False)
    s1.SymmetryConstraint(entity1=v[3], entity2=v[2], symmetryAxis=g[3])
    s1.ConstructionLine(point1=(80.0, 0.0), point2=(34.0210646056262, 25.0))
    s1.CoincidentConstraint(entity1=v[4], entity2=g[10], addUndoState=False)
    s1.ConstructionLine(point1=(80.0, 0.0), point2=(27.5, -27.5))
    s1.CoincidentConstraint(entity1=v[4], entity2=g[11], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=332.027, height=148.289, 
        cameraPosition=(24.3789, 11.4165, 188.562), cameraTarget=(24.3789, 
        11.4165, 0))
    s1.AngularDimension(line1=g[11], line2=g[10], textPoint=(89.6925659179688, 
        0.42168140411377), value=40.0)
    s1.SymmetryConstraint(entity1=g[11], entity2=g[10], symmetryAxis=g[3])
    s1.CoincidentConstraint(entity1=v[3], entity2=g[10])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=168.109, 
        farPlane=209.015, width=229.055, height=102.3, cameraPosition=(28.6344, 
        6.78617, 188.562), cameraTarget=(28.6344, 6.78617, 0))
    s1.TangentConstraint(entity1=g[9], entity2=g[4])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.49, 
        farPlane=206.634, width=202.393, height=90.3926, cameraPosition=(
        25.1123, 15.646, 188.562), cameraTarget=(25.1123, 15.646, 0))
    s1.DistanceDimension(entity1=g[4], entity2=g[5], textPoint=(48.4035568237305, 
        22.4626693725586), value=5.0)
    s1.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(24.9975452423096, 
        25.785083770752), value=35.0)
    s1.undo()
    s1.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(31.9964008331299, 
        31.284252166748), value=35.0)
    s1.Line(point1=(33.1511084107942, 17.8708238417814), point2=(27.5, 27.5))
    s1.Line(point1=(27.5, 27.5), point2=(0.0, 27.5))
    s1.HorizontalConstraint(entity=g[13], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=166.803, 
        farPlane=210.32, width=275.776, height=123.167, cameraPosition=(
        15.5849, 22.3021, 188.562), cameraTarget=(15.5849, 22.3021, 0))
    s1.Line(point1=(33.1511084107942, -17.8708238417814), point2=(26.25, -28.75))
    s1.Line(point1=(26.25, -28.75), point2=(0.0, -28.75))
    s1.HorizontalConstraint(entity=g[15], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[8], entity2=g[2], addUndoState=False)
    s1.Line(point1=(0.0, -28.75), point2=(0.0, 27.5))
    s1.VerticalConstraint(entity=g[16], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[15], entity2=g[16], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=178.206, 
        farPlane=198.917, width=115.97, height=51.7945, cameraPosition=(
        16.9998, 26.138, 188.562), cameraTarget=(16.9998, 26.138, 0))
    s1.AngularDimension(line1=g[13], line2=g[12], textPoint=(26.4667587280273, 
        25.2518062591553), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=177.173, 
        farPlane=199.95, width=127.542, height=56.9628, cameraPosition=(
        14.1922, -6.3737, 188.562), cameraTarget=(14.1922, -6.3737, 0))
    s1.AngularDimension(line1=g[15], line2=g[14], textPoint=(25.3991146087646, 
        -26.4803333282471), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.928, 
        farPlane=206.196, width=223.499, height=99.8191, cameraPosition=(
        11.5362, 11.7571, 188.562), cameraTarget=(11.5362, 11.7571, 0))
    s1.SymmetryConstraint(entity1=g[13], entity2=g[15], symmetryAxis=g[3])
    s1.HorizontalConstraint(entity=g[13])
    s1.HorizontalConstraint(entity=g[3])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=173.915, 
        farPlane=203.208, width=185.635, height=82.9081, cameraPosition=(
        13.543, 4.53842, 188.562), cameraTarget=(13.543, 4.53842, 0))
    s1.delete(objectList=(g[6], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=173.915, 
        farPlane=203.208, width=164.027, height=73.2576, cameraPosition=(
        11.4262, 0.493099, 188.562), cameraTarget=(11.4262, 0.493099, 0))
    s1.RadialDimension(curve=g[9], textPoint=(23.8744316101074, 10.3123388290405), 
        radius=19.3969)
    s1.AngularDimension(line1=g[8], line2=g[3], textPoint=(43.9712524414063, 
        -1.87454223632813), value=120.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.928, 
        farPlane=206.196, width=223.499, height=99.8191, cameraPosition=(
        2.35714, 6.00708, 188.562), cameraTarget=(2.35714, 6.00708, 0))
    s1.delete(objectList=(g[7], ))
    session.viewports['Viewport: 1'].view.setValues(width=237.765, height=106.19, 
        cameraPosition=(0.00375366, 7.35163, 188.562), cameraTarget=(
        0.00375366, 7.35163, 0))
    s1.delete(objectList=(g[8], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.794, 
        farPlane=202.33, width=174.497, height=77.9336, cameraPosition=(7.7348, 
        4.27622, 188.562), cameraTarget=(7.7348, 4.27622, 0))
    s1.ObliqueDimension(vertex1=v[5], vertex2=v[3], textPoint=(30.0, 
        14.6970062255859), value=8.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=181.146, 
        farPlane=195.977, width=93.9867, height=41.9762, cameraPosition=(
        23.5704, -2.98996, 188.562), cameraTarget=(23.5704, -2.98996, 0))
    s1.delete(objectList=(d[9], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=168.605, 
        farPlane=208.519, width=223.5, height=99.8191, cameraPosition=(21.1377, 
        -13.1554, 188.562), cameraTarget=(21.1377, -13.1554, 0))
    s1.ObliqueDimension(vertex1=v[5], vertex2=v[3], textPoint=(30.0, 
        10.6924228668213), value=8.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=180.101, 
        farPlane=197.022, width=94.7518, height=42.3179, cameraPosition=(
        -0.75964, 0.634479, 188.562), cameraTarget=(-0.75964, 0.634479, 0))
    s1.delete(objectList=(c[3], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=180.609, 
        farPlane=196.515, width=100.8, height=45.0191, cameraPosition=(5.31622, 
        -1.30267, 188.562), cameraTarget=(5.31622, -1.30267, 0))
    s1.delete(objectList=(d[6], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=158.918, 
        farPlane=218.206, width=331.988, height=148.272, cameraPosition=(
        -33.8433, -13.0038, 188.562), cameraTarget=(-33.8433, -13.0038, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.Parameter(name='r', path='dimensions[3]', expression=r)
    s.Parameter(name='bate', path='dimensions[2]', expression=bate, 
        previousParameter='r')
    s.Parameter(name='G', expression='(2*sin(60))/3+tan(bate/4)', 
        previousParameter='bate')
    s.Parameter(name='a', expression='2*r/G', previousParameter='G')
    s.Parameter(name='R', path='dimensions[7]', expression='(a/2)/sin(bate/2)', 
        previousParameter='a')
    s.Parameter(name='yanshen', path='dimensions[10]', expression=yanshen, 
        previousParameter='R')
    s.Parameter(name='Rh', path='dimensions[4]', expression=Rh, 
        previousParameter='yanshen')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=181.82, 
        farPlane=195.304, width=85.4493, height=38.1633, cameraPosition=(
        20.3469, -1.39445, 188.562), cameraTarget=(20.3469, -1.39445, 0))
    s1.VerticalDimension(vertex1=v[3], vertex2=v[2], textPoint=(31.7169322967529, 
        -1.46990919113159), value=10.0)
    s1.delete(objectList=(d[11], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=179.375, 
        farPlane=197.748, width=116.431, height=52.0004, cameraPosition=(
        17.0301, -1.60802, 188.562), cameraTarget=(17.0301, -1.60802, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.parameters['Rh'].setValues(expression=Rh)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=177.502, 
        farPlane=199.622, width=140.18, height=62.607, cameraPosition=(16.0339, 
        -1.81639, 188.562), cameraTarget=(16.0339, -1.81639, 0))
    s=mdb.models['Model-1'].sketches['__profile__']
    s.parameters['yanshen'].setValues(expression=yanshen)
    s=mdb.models['Model-1'].sketches['__profile__']
    s.parameters['r'].setValues(expression=r)
    s.parameters['bate'].setValues(expression=bate)
    s1.sketchOptions.setValues(constructionGeometry=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=172.53, 
        farPlane=204.594, width=203.198, height=90.7519, cameraPosition=(
        29.0375, 0.98383, 188.562), cameraTarget=(29.0375, 0.98383, 0))
    s1.assignCenterline(line=g[2])
    p = mdb.models['Model-1'].Part(name=partname, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts[partname]
    p.BaseSolidRevolve(sketch=s1, angle=360.0, flipRevolveDirection=OFF)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[partname]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=171.895, 
        farPlane=370.46, width=408.369, height=182.385, cameraPosition=(
        163.287, 162.691, 143.714), cameraTarget=(6.72313, 6.12694, -12.8501))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=167.463, 
        farPlane=367.866, cameraPosition=(219.747, -74.8876, 134.1), 
        cameraUpVector=(-0.114465, 0.988784, 0.0959335), cameraTarget=(6.72313, 
        6.12696, -12.8501))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=173.27, 
        farPlane=362.059, width=318.833, height=142.397, cameraPosition=(
        217.987, -71.0569, 138.764), cameraTarget=(4.96271, 9.9577, -8.18622))
    p = mdb.models['Model-1'].parts[partname]
    p.ReferencePoint(point=(0.0, 0.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=169.52, 
        farPlane=365.809, width=408.369, height=182.385, cameraPosition=(
        223.504, -59.2322, 137.284), cameraTarget=(10.4806, 21.7824, -9.66609))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=184.806, 
        farPlane=367.848, cameraPosition=(254.406, 22.0371, 108.347), 
        cameraUpVector=(-0.391059, 0.919756, 0.0334963), cameraTarget=(10.0751, 
        20.716, -9.28637))



