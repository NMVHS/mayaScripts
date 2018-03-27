import maya.cmds as cm
import random as rand

sel = cm.ls(sl = True)

def main():
    #----ui---------------
    newWin = "Randomizer"
    if cm.window(newWin,exists=True):
        cm.deleteUI(newWin,window=True)
    
    cm.window(newWin,title="Randomizer",width=200,height=200)
    baseLayout= cm.columnLayout(rowSpacing=2)
    
    rotLayout = cm.rowLayout(parent=baseLayout,numberOfColumns=3)
    cm.button("<",height=50,width=50,command = lambda x: adjustRot("<"))
    cm.button("Random Rotation",height=50,width=100,command = lambda x: adjustRot("?"))
    cm.button(">",height=50,width=50,command = lambda x: adjustRot(">"))
    
    scaleLayout = cm.rowLayout(parent=baseLayout,numberOfColumns=3)
    cm.button("<",height=50,width=50,command = lambda x: adjustScale("<"))
    cm.button("Random Scale",height=50,width=100,command = lambda x: adjustScale("?"))
    cm.button(">",height=50,width=50,command = lambda x: adjustScale(">"))
    
    randSelLayout = cm.rowLayout(parent=baseLayout,numberOfColumns=1)
    cm.button("Random Select",height=50,width=203,command = randomSelect)
    
    cm.showWindow(newWin)

def randomSelect(*args):
    sel = getSelection()
    
    for each in sel:
        childrenList = cm.listRelatives(each,children=True,type="transform")
        if childrenList == None:
            childrenList = cm.listRelatives(cm.listRelatives(each,parent=True)[0],children=True,type="transform")
        
        cm.select(clear=True)
        for eachChild in childrenList:
            dice = rand.uniform(0,1)
            
            if dice >= 0.5:
                cm.select(eachChild,add=True)


def getSelection():
    sel = cm.ls(sl=True)
    return sel

def adjustRot(option):
    sel=getSelection()
    
    incremental = 10
    for each in sel:
        curr = cm.getAttr(each + ".ry")
        
        if option == "<":
            randVal = curr - incremental
        elif option == ">":
            randVal = curr + incremental
        else:
            randVal = rand.uniform(-180,180)
        
        cm.rotate(0,randVal,0,each)
        
def adjustScale(option):
    
    sel = getSelection()
    for each in sel:
        currY = cm.getAttr(each + ".sy")
        currX = cm.getAttr(each + ".sx")
        currZ = cm.getAttr(each + ".sz")
        randVal = rand.uniform(0,currY*0.20)
        
        if option == "<":
            dir = -1
        
        elif option == ">":
            dir = 1
            
        else:
            posNeg = rand.uniform(0,1)
            if posNeg >= 0.5:
                dir = 1
            else:
                dir = -1
                
        cm.scale(currX + dir * randVal,currY + dir * randVal,currZ + dir * randVal,each)
        
if __name__ == "__main__":
    main()