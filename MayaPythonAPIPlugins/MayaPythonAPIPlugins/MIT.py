'''
Created on Dec 19, 2016

@author: Admin
'''

import maya.cmds as cmds
import maya.OpenMaya as om

mitDag =  om.MItDag(om.MItDag.kDepthFirst,om.MFn.kInvalid)
dagNode =  om.MFnDagNode()
while (not mitDag.isDone()):
    currentObj =  mitDag.currentItem()
    depth = mitDag.depth()
    dagNode.setObject(currentObj)
    
    name  =  dagNode.name()
    type =  currentObj.apiTypeStr()
    path =  dagNode.fullPathName()
    
    
    
    printOut = ""
    for i in range(0,depth):
        printOut +=  '----->'
    
    printOut +=  name + ' : ' + type
    
    print printOut
            
    mitDag.next()