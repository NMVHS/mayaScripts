#A tricky one, rsProxy node is hidden under the shape node
#shawn - June 2018

import maya.cmds as cm

sel = cm.ls(sl=True)

for each in sel:
    shape = cm.listRelatives(each)[0]
    source = cm.listConnections(shape+".inMesh",source=True)[0]
    print source

    cm.setAttr(source+".displayMode",1)
    cm.setAttr(source+".displayPercent",50)
