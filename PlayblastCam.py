import maya.cmds as cm
import os

def main():
    cam = cm.modelPanel(cm.getPanel(withFocus=True),q=True,cam=True);

    workDir = cm.workspace(rootDirectory=True,q=True)
    blastPath = workDir + "playblasts"

    filename = os.path.basename(cm.file(q=True,sceneName=True))
    filename = os.path.splitext(filename)[0]

    currRenderLayer = cm.editRenderLayerGlobals(currentRenderLayer=True,q=True)

    folderName = filename + "__" + cam + "__" + currRenderLayer

    savingPath = blastPath + "\\" + folderName + "\\" + folderName

    imageWidth = cm.getAttr("defaultResolution.width")
    imageHeight = cm.getAttr("defaultResolution.height")

    cm.playblast(filename=savingPath,format="image",width=imageWidth,height=imageHeight,percent=100,offScreen=True,showOrnaments=False,compression="png")

    print "playblast done"
