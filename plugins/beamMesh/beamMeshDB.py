from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class BeamMeshDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Beam Mesh',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='Beam Mesh', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='Approximate size:', tgt=form.sizeKw, sel=0)
        if isinstance(GroupBox_1, FXHorizontalFrame):
            FXVerticalSeparator(p=GroupBox_1, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=GroupBox_1, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        fileName = os.path.join(thisDir, 'beamMeshDB.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_1, text='', ic=icon)
