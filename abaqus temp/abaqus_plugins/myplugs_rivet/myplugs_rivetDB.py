from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class Myplugs_rivetDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'create_rivet',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        fileName = os.path.join(thisDir, 'rivet.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=self, text='', ic=icon)
        AFXTextField(p=self, ncols=12, labelText='PartName:', tgt=form.partnameKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='D1:', tgt=form.d1Kw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='D2:', tgt=form.d2Kw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='H1:', tgt=form.h1Kw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='H2', tgt=form.h2Kw, sel=0)
