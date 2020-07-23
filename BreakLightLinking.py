import maya.cmds as cm

sel = cm.ls(sl=True)

lights = []
objs = []
for each in sel:
    shape = cm.listRelatives(each,fullPath=True)[0]
    if "Light" in cm.objectType(shape):
        #this is a light
        lights.append(shape)
    else:
        allMeshChildren = cm.listRelatives(each,allDescendents=True,fullPath=True,type="mesh")

        objs += allMeshChildren
        #objs.append(shape)
    

for eachLight in lights:
    #break light links
    cm.lightlink(light=eachLight,object=objs,b=True)

    
    

            
        