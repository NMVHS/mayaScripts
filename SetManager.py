#set manager
#shawn - March 2018
import maya.cmds as cm

def main():
    #----ui---------------
    newWin = "SetManager"
    if cm.window(newWin,exists=True):
        cm.deleteUI(newWin,window=True)
    
    cm.window(newWin,title="Set Manager",width=200,height=200)
    baseLayout= cm.columnLayout(rowSpacing=2)
    
    cm.button("Create New Set",height=50,width=200,command = newSet)
    cm.button("Add to Selected",height=50,width=200,command = addToSet)
    cm.button("Select Set Name Only",height=50,width=200,command = selectSet)
    cm.button("Select Set Members",height=50,width=200,command = selectSetMembers)
    
    cm.showWindow(newWin)

def selectSetMembers(*args):
    sel = cm.ls(sl=True)
    cm.select(clear=True)
    for each in sel:
        if cm.objectType(each) == "objectSet":
            cm.select(each,add=True)
        else:
            belongSets = cm.listSets(object=each)
            cm.select(belongSets)
                
def newSet(*args):
    sel = cm.ls(sl=True,flatten=True)
    result = cm.promptDialog(title='Create New Name',message='Set Name:',button=['OK','Cancel'],
                                defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')

    if result == 'OK':
    	setName = cm.promptDialog(query=True,text=True)
    	cm.sets(name=setName,empty=True)
    	cm.sets(sel,add=setName)
    	
def addToSet(*args):
    sel = cm.ls(sl=True,flatten=True)
    if cm.objectType(sel[-1]) == "objectSet":
        cm.sets(sel[:-1],add=sel[-1])
    else:
        belongSets = cm.listSets(object=sel[-1])
        for eachSet in belongSets:
            cm.sets(sel[:-1],add=eachSet)

def selectSet(*args):
    sel = cm.ls(sl=True,flatten=True)
    for each in sel:
        if cm.objectType(each) != "objectSet":
            belongSets = cm.listSets(object=each)
            cm.select(belongSets,noExpand=True)

if __name__ == "__main__":
    main()