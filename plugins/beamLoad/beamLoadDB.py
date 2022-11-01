from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class BeamLoadDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'BC and Load',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='Encastre', opts=FRAME_GROOVE)
        VAligner_4 = AFXVerticalAligner(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        pickHf = FXHorizontalFrame(p=VAligner_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='Choose a face for fixing:         ' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = BeamLoadDBPickHandler(form, form.pickFaceFixKw, 'Pick an entity', FACES, ONE, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        GroupBox_2 = FXGroupBox(p=self, text='Load', opts=FRAME_GROOVE)
        VAligner_5 = AFXVerticalAligner(p=GroupBox_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        pickHf = FXHorizontalFrame(p=VAligner_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='Choose a face for Loading:' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = BeamLoadDBPickHandler(form, form.pickFaceLoadKw, 'Pick an entity', FACES, ONE, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        AFXTextField(p=VAligner_5, ncols=6, labelText='Magnitude:', tgt=form.loadMagKw, sel=0)
        if isinstance(self, FXHorizontalFrame):
            FXVerticalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=self, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        fileName = os.path.join(thisDir, 'beamLoadDB.PNG')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=self, text='', ic=icon)


###########################################################################
# Class definition
###########################################################################

class BeamLoadDBPickHandler(AFXProcedure):

        count = 0

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def __init__(self, form, keyword, prompt, entitiesToPick, numberToPick, label):

                self.form = form
                self.keyword = keyword
                self.prompt = prompt
                self.entitiesToPick = entitiesToPick # Enum value
                self.numberToPick = numberToPick # Enum value
                self.label = label
                self.labelText = label.getText()

                AFXProcedure.__init__(self, form.getOwner())

                BeamLoadDBPickHandler.count += 1
                self.setModeName('BeamLoadDBPickHandler%d' % (BeamLoadDBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

                return  AFXPickStep(self, self.keyword, self.prompt, 
                    self.entitiesToPick, self.numberToPick, sequenceStyle=TUPLE)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):

                self.label.setText( self.labelText.replace('None', 'Picked') )
                return None

        def deactivate(self):

            AFXProcedure.deactivate(self)
            if  self.numberToPick == ONE and self.keyword.getValue() and self.keyword.getValue()[0]!='<':
                sendCommand(self.keyword.getSetupCommands() + '\nhighlight(%s)' % self.keyword.getValue() )

