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

    cm.textScrollList ("dispLayerTree",width=200)
    updateDispLayers()
    cm.button("Add to Layer",height=30,width=200,command = addToDispLayer)
    cm.button("Export Display Layer Data",height=30,width=200, command = exportDispLayerData)


    cm.showWindow(newWin)

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

    print "Layer Data exported."
