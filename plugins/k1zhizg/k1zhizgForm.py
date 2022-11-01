from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class K1zhizgForm(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='k1_zhizg',
            objectName='plugins.k1zhizg.pingzgk1script', registerQuery=False)
        pickedDefault = ''
        self.partname_kKw = AFXStringKeyword(self.cmd, 'partname_k', True, '')
        self.Dh_kKw = AFXStringKeyword(self.cmd, 'Dh_k', True, '')
        self.d_kKw = AFXStringKeyword(self.cmd, 'd_k', True, '')
        self.yanshen_kKw = AFXStringKeyword(self.cmd, 'yanshen_k', True, '')
        self.gunfeng_kKw = AFXStringKeyword(self.cmd, 'gunfeng_k', True, '')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import k1zhizgDB
        return k1zhizgDB.K1zhizgDB(self)

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

