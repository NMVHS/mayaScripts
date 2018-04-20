import maya.cmds as cm
import json

def main():
    uiWindow = "offsetKeyWindow"

    if cm.window(uiWindow,exists=True):
        cm.deleteUI(uiWindow,window=True)

    win = cm.window(uiWindow,width = 100,height = 50, title = "Offset Keyframe")
    cm.columnLayout("columns")
    cm.rowLayout(numberOfColumns=8,parent="columns")
    offsetAutoNegBtn = cm.button(label = "50<<", width = 50, command = lambda x: offsetKey("manual",-50))
    offsetAutoNegBtn = cm.button(label = "20<<", width = 50, command = lambda x: offsetKey("manual",-20))
    offsetNeg2Btn = cm.button(label = "<<", width = 50, command = lambda x: offsetKey("manual",-2))
    offsetNeg1Btn = cm.button(label = "<", width = 50, command = lambda x: offsetKey("manual",-1))
    offsetPos1Btn = cm.button(label = ">", width = 50, command = lambda x: offsetKey("manual",1))
    offsetPos2Btn = cm.button(label = ">>", width = 50, command = lambda x: offsetKey("manual",2))
    offsetAutoPosBtn = cm.button(label = ">>20", width = 50, command = lambda x: offsetKey("manual",20))
    offsetAutoPosBtn = cm.button(label = ">>50", width = 50, command = lambda x: offsetKey("manual",50))

    cm.rowLayout(numberOfColumns=5,parent="columns")
    exportKeys = cm.button(label="Export Keys",width=80,command = lambda x: exportKeys())
    cm.text(label="New NameSpace")
    cm.textField("newNameSpace",width=80)
    cm.checkBox("useNewNameSpace",label="Use New NameSpace")
    importKays = cm.button(label="Import Keys",width=80,command = lambda x: importKeys())

    cm.showWindow(win)


def offsetKey(mode, dir):

    animCurves = cm.keyframe(sl=True,name=True,q=True)

    cnt = 1
    if mode == "manual":
        offsetAmount = dir
    else:
        offsetAmount = dir * cnt

    for eachCurve in animCurves:
         keyIndex = cm.keyframe(eachCurve,sl=True,indexValue=True,q=True)
         for eachIndex in keyIndex:
             cm.keyframe(eachCurve,index = (eachIndex,eachIndex), timeChange = offsetAmount, relative = True)


def exportKeys():
    animCurves = cm.keyframe(sl=True,name=True,q=True)

    curveDataList = []
    for eachCurve in animCurves:
        attribName = cm.listConnections(eachCurve,plugs=True)[0]
        curveData = {"attribName":attribName}
        keyIndex = cm.keyframe(eachCurve,sl=True,indexValue=True,q=True)
        keyTimes = cm.keyframe(eachCurve,sl=True,timeChange=True,q=True)
        keyValues = cm.keyframe(eachCurve,sl=True,valueChange=True,q=True)
        keyDataList = []
        for i in range(0,len(keyIndex)):
            keyData = [keyIndex[i],keyTimes[i],keyValues[i]]
            keyDataList.append(keyData)

        curveData['keys'] = keyDataList
        curveDataList.append(curveData)

    sceneName = cm.file(q=True,sceneName=True).split(".")[0]
    with open(sceneName+'.json','w') as outputData:
        json.dump(curveDataList,outputData,indent=4)

    print "Keys exported successfully"

def importKeys():
    dataFileName = cm.fileDialog2(fileFilter="*.json",dialogStyle=2,setProjectBtnEnabled=False,caption="Select the json file",okCaption="Accept")[0]

    with open(dataFileName,'r') as inputData:
        curveDataList = json.load(inputData)

    for eachCurveData in curveDataList:
        objectName,attribName = eachCurveData["attribName"].split('.')
        useNewNameSpace =  cm.checkBox("useNewNameSpace",q=True,value=True)

        if useNewNameSpace:
            #If useNewNameSpace checked, replace or add new namespace
            newNameSpace = cm.textField("newNameSpace",q=True,tx=True)

            if ':' in objectName:
                #object has a nameSpace
                oriNameSpace,oriObjName = objectName.split(':')

                if newNameSpace == "":
                    #new name space is blank, then remove the original namespace
                    objectName = oriObjName
                else:
                    objectName = newNameSpace + ':' + oriObjName
            else:
                #object doesn't have a nameSpace
                objectName = newNameSpace + ":" + objectName

        curveKeys = eachCurveData["keys"]

        for eachKey in curveKeys:
            cm.setKeyframe(objectName,attribute=attribName,time=eachKey[1],value=eachKey[2])

    print "Keys imported successfully"

if __name__ == "__main__":
    main()
