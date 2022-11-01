from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class BeamMaxValueDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Max Value',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='Strees or U ?', opts=FRAME_GROOVE)
        VAligner_1 = AFXVerticalAligner(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=VAligner_1, text='Max Mises     ', tgt=form.fieldKw1, sel=7)
        FXRadioButton(p=VAligner_1, text='Max U           ', tgt=form.fieldKw1, sel=8)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        fileName = os.path.join(thisDir, 'beamMaxValue.PNG')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=self, text='', ic=icon)
