import maya.cmds as cm
import random as rand
import math

def main():
    #----ui here--------------
    newWin = "clonerSwapper"
    if cm.window(newWin,exists=True):
        cm.deleteUI(newWin,window=True)
    
    cm.window(newWin,title="Cloner Swapper",width=200,height=150)
    baseLayout= cm.columnLayout("base",rowSpacing=2)
    cm.button("Swap",height=50,width=200,command = lambda x: worker("swap"))
    cm.button("Replace",height=50,width=200,command = lambda x: worker("replace"))
    
    cm.showWindow(newWin)


def worker(option,*args):
    #----do the job-----------
    newMeshList = cm.ls(sl=True)[:-1]
    firstCopy = {}
    
    for each in newMeshList:
        firstCopy[each] = True
    
    oldMeshGrp = cm.listRelatives(cm.ls(sl=True)[-1],children=True)
    
    for oldMesh in oldMeshGrp:
        #copy new mesh and delete old mesh
        oldMeshPos = cm.xform(oldMesh,q=True,t=True,ws=True)
        
        if option == "swap":
            oldMeshRot = cm.xform(oldMesh,q=True,ro=True,ws=True)
            
            if firstCopy[newMeshList[0]]:
                newMeshDup = newMeshList[0]
                firstCopy[newMeshList[0]] = False
            else:
                newMeshDup = cm.duplicate(newMeshList[0],inputConnections=True)[0]
                
            cm.xform(newMeshDup,t=oldMeshPos,ws=True)
            cm.xform(newMeshDup,ro=oldMeshRot,ws=True)
            cm.delete(oldMesh)
            
        else:
            dice = int(math.floor(rand.uniform(0,len(newMeshList)+1)))
            if dice < len(newMeshList):
                if firstCopy[newMeshList[dice]]:
                    newMeshDup = newMeshList[dice]
                    firstCopy[newMeshList[dice]] = False
                else:
                    newMeshDup = cm.duplicate(newMeshList[dice],inputConnections=True)[0]
                    
                cm.xform(newMeshDup,t=oldMeshPos,ws=True)
                    
                cm.delete(oldMesh)

if __name__=="__main__":
    main()