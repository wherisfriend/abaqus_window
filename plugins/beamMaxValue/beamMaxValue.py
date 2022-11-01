from abaqus import *
from abaqusConstants import *
from caeModules import *

def beamMaxValue(field):
    vp = session.viewports['Viewport: 1']
    odb = vp.displayedObject
    maxValue = 0
    if field == 'Max Mises     ':
        for step in odb.steps.values():
            for frame in step.frames:
                s = frame.fieldOutputs['S']
                for sValue in s.values:
                    if sValue.mises > maxValue:
                        maxValue = sValue.mises
                        maxElem = sValue.elementLabel
        print('Max Mises = {0}, Element Label = {1}'.format(maxValue, maxElem))
    
    elif field == 'Max U           ':
        for step in odb.steps.values():
            for frame in step.frames:
                u = frame.fieldOutputs['U']
                for uValue in u.values:
                    if uValue.magnitude > maxValue:
                        maxValue = uValue.magnitude
                        maxNode = uValue.nodeLabel
        print('Max U = {0}, Node Label = {1}'.format(maxValue, maxNode))
