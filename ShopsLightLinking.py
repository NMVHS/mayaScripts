#used on a archvis job where lights for lots of shops need to be light linked
#shawn - June 2018

import maya.cmds as cm

shopsGrpName = "SHOPS"
shops = cm.listRelatives(shopsGrpName,path=True,children=True)
print shops

shopLightsGrpsName = "SHOPS_LIGHTS"
shopLightsGrps = cm.listRelatives(shopLightsGrpsName,path=True,children=True)

for eachShopLightsGrp in shopLightsGrps:
    #find target shop
    targetShop = ""
    for eachShop in shops:
        if eachShopLightsGrp in eachShop:
            targetShop = eachShop
            break

    if targetShop == "":
        continue

    #break light links first/ have to break every objects
    shopLights = cm.listRelatives(eachShopLightsGrp,path=True,children=True)

    for eachLight in shopLights:
        currLinkedObjs = cm.lightlink(light=eachLight,q=True)
        cm.lightlink(light=eachLight,object=currLinkedObjs,b=True)


        cm.lightlink(light=eachLight,object=targetShop,m=True)
        print eachLight,"=====linked to====" + targetShop

print "All Done"
