from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class BeamMaxValueForm(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='beamMaxValue',
            objectName='plugins.beamMaxValue.beamMaxValue', registerQuery=False)
        pickedDefault = ''
        if not self.radioButtonGroups.has_key('field'):
            self.fieldKw1 = AFXIntKeyword(None, 'fieldDummy', True)
            self.fieldKw2 = AFXStringKeyword(self.cmd, 'field', True)
            self.radioButtonGroups['field'] = (self.fieldKw1, self.fieldKw2, {})
        self.radioButtonGroups['field'][2][7] = 'Max Mises     '
        self.fieldKw1.setValue(7)
        if not self.radioButtonGroups.has_key('field'):
            self.fieldKw1 = AFXIntKeyword(None, 'fieldDummy', True)
            self.fieldKw2 = AFXStringKeyword(self.cmd, 'field', True)
            self.radioButtonGroups['field'] = (self.fieldKw1, self.fieldKw2, {})
        self.radioButtonGroups['field'][2][8] = 'Max U           '

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import beamMaxValueDB
        return beamMaxValueDB.BeamMaxValueDB(self)

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
