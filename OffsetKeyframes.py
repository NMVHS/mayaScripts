import maya.cmds as cm


def offsetKey(mode, dir):
    selKeyNames = cm.keyframe(sl=True,q=True,name=True)
    selKeyIds = cm.keyframe(sl=True,q=True,indexValue=True)
    
    
    cnt = 0
    for i in range(0,len(selKeyNames)):
        
        if mode == "manual":
            offsetAmount = dir
        else:
            offsetAmount = dir * cnt
        
        

        cm.keyframe(selKeyNames[i], index = selKeyIds[i], timeChange = offsetAmount, relative = True)
        
        cnt += 1
    


def main():
    win = cm.window(width = 100,height = 50, title = "Offset Keyframe")
    
    cm.rowLayout(numberOfColumns=8)
    offsetAutoNegBtn = cm.button(label = "<<-|", width = 50, command = 'offsetKey("auto",-2)')
    offsetAutoNegBtn = cm.button(label = "<-|", width = 50, command = 'offsetKey("auto",-1)')
    offsetNeg2Btn = cm.button(label = "<<", width = 50, command = 'offsetKey("manual",-2)')
    offsetNeg1Btn = cm.button(label = "<", width = 50, command = 'offsetKey("manual",-1)')
    offsetPos1Btn = cm.button(label = ">", width = 50, command = 'offsetKey("manual",1)')
    offsetPos2Btn = cm.button(label = ">>", width = 50, command = 'offsetKey("manual",2)')
    offsetAutoPosBtn = cm.button(label = "|->", width = 50, command = 'offsetKey("auto",1)')
    offsetAutoPosBtn = cm.button(label = "|->>", width = 50, command = 'offsetKey("auto",2)')
    
    cm.showWindow(win)
    


if __name__ == "__main__":
    main()