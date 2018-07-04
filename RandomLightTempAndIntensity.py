import maya.cmds as cm
import random

shopLightsGrpsName = "SHOPS_LIGHTS"
shopLightsGrps = cm.listRelatives(shopLightsGrpsName,children=True)

for eachLightGrp in shopLightsGrps:
    lights = cm.listRelatives(eachLightGrp,children=True)
    for eachLight in lights:
        randTemp = random.randrange(0, 400, 100)
        cm.setAttr(eachLight+".temperature",4000+randTemp)
        randIntensity = random.randrange(0, 20, 5)
        cm.setAttr(eachLight+".multiplier",20+randIntensity)
