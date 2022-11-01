from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class YuankongxingDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '\xd4\xb2\xbf\xd7\xd0\xcd\xbd\xa8\xc4\xa3v1',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        fileName = os.path.join(thisDir, 'yuankong.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=self, text='', ic=icon)
        AFXTextField(p=self, ncols=12, labelText='\xce\xc4   \xbc\xfe    \xc3\xfb:', tgt=form.partname_kKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='\xc0\xa9\xd5\xc5\xd4\xb2\xbd\xc7 \xa6\xc1 :', tgt=form.alf_kKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='\xbb\xa1\xb3\xa4\xb0\xeb\xbe\xb6 R :', tgt=form.R_kKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='\xd4\xfe\xb9\xf5\xd6\xb1\xbe\xb6Dh:', tgt=form.Dh_kKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='\xb9\xf5\xb7\xec\xbf\xed\xb6\xc8 M:', tgt=form.gunfeng_kKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='\xd1\xd3\xc9\xec\xb3\xa4\xb6\xc8 L :', tgt=form.yanshen_kKw, sel=0)
