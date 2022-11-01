from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class BeamCreateDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Beam Create',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_4 = FXGroupBox(p=self, text='Dimension', opts=FRAME_GROOVE)
        VAligner_4 = AFXVerticalAligner(p=GroupBox_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Length:             ', tgt=form.lengthKw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Width:', tgt=form.widthKw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Height', tgt=form.heightKw, sel=0)
        GroupBox_2 = FXGroupBox(p=self, text='Material', opts=FRAME_GROOVE)
        VAligner_3 = AFXVerticalAligner(p=GroupBox_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Material Name:', tgt=form.matNameKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Elastic Modulus:', tgt=form.EKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Poissons ratio:', tgt=form.NuKw, sel=0)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        fileName = os.path.join(thisDir, 'beamCreateDB.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=self, text='', ic=icon)
