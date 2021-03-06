#display layer manager
#shawn - April 2018
#written when I almost fell asleep
import maya.cmds as cm
import json
import os.path

def main():
    #----ui---------------
    newWin = "DispLayerManager"
    if cm.window(newWin,exists=True):
        cm.deleteUI(newWin,window=True)

    cm.window(newWin,title="Dispay Layer Manager",width=200,height=200)
    baseLayout= cm.columnLayout(rowSpacing=2)

    layerRow = cm.rowLayout(numberOfColumns=2)
    cm.textScrollList ("dispLayerTree",width=160,parent=layerRow)
    layerCtrlColumn = cm.columnLayout(rowSpacing=2,parent=layerRow)
    cm.button("V",height=30,width=30,command=layerVisSwitch)

    btnColumns = cm.columnLayout(rowSpacing=2,parent=baseLayout)
    cm.button("Add to Layer",height=30,width=200,command = addToDispLayer)
    cm.button("Export Display Layer Data",height=30,width=200, command = exportDispLayerData)
    cm.button("Load Display Layer Data",height=30,width=200, command = loadDispLayerData)

    updateDispLayers()

    cm.showWindow(newWin)

def layerVisSwitch(*args):
    selLayer = getDispLayerSel()[0]
    currVis = cm.getAttr(selLayer + ".visibility")
    if currVis:
        cm.setAttr(selLayer + ".visibility",False)
    else:
        cm.setAttr(selLayer + ".visibility",True)

def addToDispLayer(*args):
    #which layer is selected
    selLayer = getDispLayerSel()
    sel = cm.ls(sl=True)
    cm.editDisplayLayerMembers(selLayer,sel,noRecurse=True)
    exportDispLayerData()

def getDispLayerSel():
    selLayer = cm.textScrollList("dispLayerTree",q=True,selectItem=True)
    return selLayer

def updateDispLayers():
    dispLayers= cm.ls(type="displayLayer")
    dispLayers.remove("defaultLayer")
    cm.textScrollList("dispLayerTree",edit=True,removeAll=True)
    cm.textScrollList ("dispLayerTree",edit=True,append=dispLayers)

def exportDispLayerData(*args):
    currSel = cm.textScrollList("dispLayerTree",q=True,selectItem=True)
    updateDispLayers()
    selLayers = cm.textScrollList("dispLayerTree",q=True,allItems=True)

    layerData = {}
    for eachLayer in selLayers:
        layerMembers = cm.editDisplayLayerMembers(eachLayer,q=True)
        layerData[eachLayer] = layerMembers

    savePath = os.path.splitext(cm.file(query=True,sn=True))[0] + "_DisplayLayerData.json"

    with open(savePath,"w") as outData:
        json.dump(layerData, outData,indent=4)

    cm.textScrollList("dispLayerTree",e=True,selectItem=currSel)

    print "Display Layer Data exported."

def loadDispLayerData(*args):
    savePath = os.path.splitext(cm.file(query=True,sn=True))[0] + "_DisplayLayerData.json"

    if os.path.isfile(savePath):
        with open(savePath,"r") as inData:
            dispLayerData = json.load(inData)

    if cm.confirmDialog(title="Overwrite",button=['Yes','No'],message="Overwrite existing display layer data?",
                        defaultButton='No', cancelButton='No', dismissString='No' ) == "Yes":
        for eachLayer in dispLayerData:
            if cm.objExists(eachLayer):
                #check objects in existing members
                existLayerMembers = cm.editDisplayLayerMembers(eachLayer,q=True)
                for eachMember in dispLayerData[eachLayer]:
                    if not eachMember in existLayerMembers:
                        #if not, add to this layer
                        cm.editDisplayLayerMembers(eachLayer,eachMember,noRecurse=True)

            else:
                #layer doesn't exist, add new layer and add all the members
                cm.createDisplayLayer(name=eachLayer,empty=True)
                cm.editDisplayLayerMembers(eachLayer,dispLayerData[eachLayer],noRecurse=True)

        print "Display Layer Data loaded."
    else:
        print "Loading Display Layer Data aborted."
