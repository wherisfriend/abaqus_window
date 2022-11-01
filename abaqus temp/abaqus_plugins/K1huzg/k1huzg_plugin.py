from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class K1huzg_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='k1_huzg',
            objectName='huzgk1script', registerQuery=False)
        pickedDefault = ''
        self.partname_kKw = AFXStringKeyword(self.cmd, 'partname_k', True, '')
        self.Dh_kKw = AFXStringKeyword(self.cmd, 'Dh_k', True, '')
        self.d_kKw = AFXStringKeyword(self.cmd, 'd_k', True, '')
        self.yanshen_kKw = AFXStringKeyword(self.cmd, 'yanshen_k', True, '')
        self.bate_kKw = AFXStringKeyword(self.cmd, 'bate_k', True, '')
        self.gunfeng_kKw = AFXStringKeyword(self.cmd, 'gunfeng_k', True, '')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import k1huzgDB
        return k1huzgDB.K1huzgDB(self)

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='\xbb\xa1\xc8\xfd\xbd\xc7\xbf\xd7\xd0\xcd\xb5\xa5\xb5\xc0\xb4\xce\xbd\xa8\xc4\xa3', 
    object=K1huzg_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import huzgk1script',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
