from abaqus import *
from abaqusConstants import *
from caeModules import *

def beamMesh(size):
	p = mdb.models['Model-1'].parts['Part-1']
	p.seedPart(size= size, deviationFactor=0.1, minSizeFactor=0.1)
	p.generateMesh()