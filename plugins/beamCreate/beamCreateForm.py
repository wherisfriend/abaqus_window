from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class BeamCreateForm(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='beamCreate',
            objectName='plugins.beamCreate.beamCreate', registerQuery=False)
        pickedDefault = ''
        self.lengthKw = AFXFloatKeyword(self.cmd, 'length', True, 40.0)
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True, 30)
        self.heightKw = AFXFloatKeyword(self.cmd, 'height', True, 100)
        self.matNameKw = AFXStringKeyword(self.cmd, 'matName', True, 'steel')
        self.EKw = AFXFloatKeyword(self.cmd, 'E', True, 210000)
        self.NuKw = AFXFloatKeyword(self.cmd, 'Nu', True, 0.3)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import beamCreateDB
        return beamCreateDB.BeamCreateDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
