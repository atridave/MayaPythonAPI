'''
Created on Jan 31, 2017

@author: Admin
'''
import maya.cmds as cmds

cmds.select('L_heelVeloRef_loc','L_ballVeloRef_loc')

def makeSpeedNode():
    sel =  cmds.ls(sl=1)

    if len(sel) > 0:
        for i in range(0,len(sel)):            
#             spNode = cmds.createNode('speedNode',n = (sel[i]+'_spNode'))
            dNode = cmds.createNode('decomposeMatrix',n=(sel[i]+'_dmn'))
            cmds.connectAttr((sel[i]+'.worldMatrix'),(dNode+'.inputMatrix'),f=1)
#             cmds.connectAttr((dNode+'.outputTranslateX'),(spNode+'.sTx'),f=1)
#             cmds.connectAttr((dNode+'.outputTranslateY'),(spNode+'.sTy'),f=1)
#             cmds.connectAttr((dNode+'.outputTranslateZ'),(spNode+'.sTz'),f=1)            
            
    else:
        cmds.error('Please select one object')
    
makeSpeedNode()