from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup


def beamCreate(length, width, height, matName, E, Nu):
	session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=71.9949951171875, 
	    height=93.804443359375)
	session.viewports['Viewport: 1'].makeCurrent()
	session.viewports['Viewport: 1'].maximize()
	executeOnCaeStartup()

	s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.rectangle(point1=(-length/2, -width/2), point2=(length/2, width/2))
	p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p = mdb.models['Model-1'].parts['Part-1']
	p.BaseSolidExtrude(sketch=s, depth=height)
	session.viewports['Viewport: 1'].setValues(displayedObject=p)
	del mdb.models['Model-1'].sketches['__profile__']

	mdb.models['Model-1'].Material(name= matName)
	mdb.models['Model-1'].materials[matName].Elastic(table=((E, Nu), ))
	mdb.models['Model-1'].HomogeneousSolidSection(name='Section'+ matName, material=matName , thickness=None) 
	c = p.cells
	region = regionToolset.Region(cells=c)
	p.SectionAssignment(region=region, sectionName='Section'+ matName, offset=0.0, 
	    offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

	a = mdb.models['Model-1'].rootAssembly
	a.Instance(name='Part-1-1', part=p, dependent=ON)
	
	mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
