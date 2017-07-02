'''
 Created on Feb 1, 2017

@author: Admin
'''
import maya.cmds as cmds
velohook =  ('L_heelVeloRef_loc','L_ballVeloRef_loc','R_heelVeloRef_loc','R_ballVeloRef_loc')
# cmds.select('src:LeftHeel','src:LeftToeBase','src:RightHeel','src:RightToeBase')
#cmds.select('L_LeftHeel','L_toe_jnt','R_LeftHeel','R_toe_jnt')
cmds.select('Def_L_Tarsel_jnt','Def_L_Toe_jnt','Def_R_Tarsel_jnt','Def_R_Toe_jnt')


def makeVelocityNode():
  
    sel =  cmds.ls(sl=1)
    if len(sel) > 0:
        for i in range(0,len(sel)):
            node = cmds.createNode('velocityNode',n = (sel[i]+'_velocityNode')) 
            pmm =  cmds.createNode('pointMatrixMult',n =  (sel[i]+'_pmm'))
            cmds.connectAttr('%s.translate' % sel[i],'%s.inPoint' % pmm)
            cmds.connectAttr('%s.parentMatrix[0]' % sel[i],'%s.inMatrix' % pmm)
            attrLoc =  cmds.spaceLocator(n = node+'attrHolder_loc')
            pmmAddAttrs = ('outputPastX','outputPastY','outputPastZ','outputFutureX','outputFutureY','outputFutureZ')  
            cmds.select(attrLoc)
            for j in range(0,len(pmmAddAttrs)):                
                cmds.addAttr(ln = pmmAddAttrs[j],dv = 0,at = 'float',k=1)
            
            frameAttr =  ('_XframeCache','_YframeCache','_ZframeCache')
            pmmAttr = ('.outputX','.outputY','.outputZ')
            pastAttr = ('.outputPastX','.outputPastY','.outputPastZ')  
            futureAttr = ('.outputFutureX','.outputFutureY','.outputFutureZ')  
            
            for k in range(0,len(frameAttr)):
                frameCNode =  cmds.createNode('frameCache',n = (pmm+frameAttr[k]))
                cmds.setAttr('%s.varyTime'  % frameCNode, 1)
                cmds.setAttr('%s.past[1]'   % frameCNode, 1)
                cmds.setAttr('%s.future[1]' % frameCNode, 1)
                cmds.connectAttr(pmm+pmmAttr[k],'%s.stream' % frameCNode)
                cmds.connectAttr('%s.past[1]' % frameCNode,attrLoc[0]+pastAttr[k])
                cmds.connectAttr('%s.future[1]' % frameCNode,attrLoc[0]+futureAttr[k])               

                
                                 
            cmds.connectAttr('%s.outputX' % pmm,'%s.inPutCurrentX' % node)
            cmds.connectAttr('%s.outputY' % pmm,'%s.inPutCurrentY' % node)
            cmds.connectAttr('%s.outputZ' % pmm,'%s.inPutCurrentZ' % node)
            cmds.connectAttr('%s.outputPastX' % attrLoc[0],'%s.inPutPastX' % node)
            cmds.connectAttr('%s.outputPastY' % attrLoc[0],'%s.inPutPastY' % node)
            cmds.connectAttr('%s.outputPastZ' % attrLoc[0],'%s.inPutPastZ' % node)  
            cmds.connectAttr('%s.outputFutureX' % attrLoc[0],'%s.inPutFutureX' % node)
            cmds.connectAttr('%s.outputFutureY' % attrLoc[0],'%s.inPutFutureY' % node)
            cmds.connectAttr('%s.outputFutureZ' % attrLoc[0],'%s.inPutFutureZ' % node)            
    else:
        cmds.error('Please select one object')
    
makeVelocityNode()

#connectAttr -f src:RightToeBase.velocity src:PlaneWeightRight.translateZ;
#R_heelVeloRef_loc_velocityNode
#connectAttr -f src:RightHeel.velocity src:PlaneWeightRight.translateY;

#connectAttr -f src:LeftToeBase.velocity src:PlaneWeightLeft.translateZ;
#R_heelVeloRef_loc_velocityNode
#connectAttr -f src:LeftHeel.velocity src:PlaneWeightLeftt.translateY;