from abaqus import *
from abaqusConstants import *
from caeModules import *

def beamLoad(pickFaceFix, pickFaceLoad, loadMag):
	a = mdb.models['Model-1'].rootAssembly
	fs = a.instances['Part-1-1'].faces
	f1 = fs[pickFaceFix.index : pickFaceFix.index+1]
	region = regionToolset.Region(faces=f1)
	mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1', 
	    region=region, localCsys=None)

	f2 = fs[pickFaceLoad.index : pickFaceLoad.index+1]
	region = regionToolset.Region(side1Faces=f2)
	mdb.models['Model-1'].SurfaceTraction(name='Load-1', createStepName='Step-1', 
	    region=region, magnitude=loadMag, directionVector=((0.0, 0.0, 0.0), (0.0, 
	    -1.0, 0.0)), distributionType=UNIFORM, field='', localCsys=None)