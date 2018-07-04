import maya.cmds as cm

sel = cm.ls(sl=True)

lights = []
objs = []
for each in sel:
    shape = cm.listRelatives(each)[0]
    if "Light" in cm.objectType(shape):
        #this is a light
        lights.append(shape)
    else:
        objs.append(shape)
    

for eachLight in lights:
    #break light links
    currLinkedObjs = cm.lightlink(light=eachLight,q=True)
    cm.lightlink(light=eachLight,object=currLinkedObjs,b=True)
    
    #relink
    cm.lightlink(light=eachLight,object=objs,m=True)
    print eachLight + " ====linked to==== ",objs
    
    

            
        