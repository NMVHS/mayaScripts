#Convert mesh to rsMeshLight

import maya.cmds as cm

def main():
    sel = cm.ls(sl = True)
    
    #check if selection is valid
    if len(sel) == 0: return    
    
    for each in sel:
        
        objXform = each
        objShape = cm.listRelatives(sel[0], fullPath = True)[0]
        
        #store original mesh's transformation
        objWpos = cm.xform(objXform,query = True,translation = True, ws = True)
        objWrot = cm.xform(objXform,query = True,rotation = True, ws = True)
        objWscale = cm.xform(objXform,query = True,scale = True, ws = True)
        
        #create a rsPhysicalLight and move it to the obj's position
        rsLight = cm.shadingNode("RedshiftPhysicalLight", asLight = True)
        rsLightShape = cm.listRelatives(rsLight)[0]

        cm.setAttr(rsLight + ".areaShape",4)
        cm.xform(rsLight,translation = objWpos,worldSpace = True)
        cm.xform(rsLight,rotation = objWrot,worldSpace = True)
        cm.xform(rsLight,scale = objWscale,worldSpace = True)
        
        #create an instance of the mesh
        rsLightMesh = cm.parent(objShape,rsLight,add = True,shape = True)
        cm.connectAttr(objShape + ".message" , rsLightShape + ".areaShapeObject")
          
        #hide original mesh
        cm.hide(objXform)
        
        #change light name
        cm.rename(rsLight,"rsMeshLight_" + objXform)
    
    
if __name__ == "__main__":
    main()

