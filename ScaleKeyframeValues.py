#useful when the scale of an object with keyframe needs to be changed 
#shawn - May 2018

import maya.cmds as cm

animCurves = cm.keyframe(sl=True,name=True,q=True)


for eachCurve in animCurves:
     keyIndex = cm.keyframe(eachCurve,sl=True,indexValue=True,q=True)
     for eachIndex in keyIndex:
         currV = cm.keyframe(eachCurve,index=(eachIndex,eachIndex),valueChange=True,q=True)
         newV = currV[0] * 200
         cm.keyframe(eachCurve,index = (eachIndex,eachIndex), valueChange = newV)
