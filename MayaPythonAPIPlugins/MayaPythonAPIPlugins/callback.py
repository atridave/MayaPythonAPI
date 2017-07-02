'''
Created on Dec 23, 2016

@author: Atri
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
from random import randint
import maya.cmds as cmds



nodeName =  "CVG"
nodeID  = OpenMaya.MTypeId(0x100fff)

class CVG(OpenMayaMPx.MPxNode):
    idCallBack = []
    joint1 =  OpenMaya.MObject()
    joint2 =  OpenMaya.MObject()
    joint3 =  OpenMaya.MObject()
    
    activeEffector = OpenMaya.MObject()
    activeHandle = OpenMaya.MObject()
    activePoleVector = OpenMaya.MObject()
    activePoleVectorCtrl = OpenMaya.MObject()
    
    

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
        self.idCallBack.append(OpenMaya.MEventMessage.addEventCallback('SelectionChanged',self.callbackFunc))
        self.idCallBack.append(OpenMaya.MDGMessage.addNodeRemovedCallback(self.remove,'dependNode'))
        
    def callbackFunc(self,*args):
        print 'callback func'
        cmds.spaceLocator( p=(randint(0,100), randint(0,100),randint(0,100)) )

        
        
    def remove(self,*args):
        try:
            OpenMaya.MSelectionList.add(self.thisMObject())
        except:
            for i in xrange(len(self.idCallBack)):
                try:
                    OpenMaya.MEventMessage.removeCallback(self.idCallBack[i])
                except:
                    pass
                try:
                    OpenMaya.MDGMessage.removeCallback(self.idCallBack[i])
                except:
                    pass
        
        
        
    def compute(self,plug,dataBlock):
        pass
      
        

        
        
        

def nodeCreator():
    return OpenMayaMPx.asMPxPtr(CVG())
        

def nodeInitializer():
    pass

    
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri Dave','1.0')
    try:
        mplugin.registerNode( nodeName, nodeID,nodeCreator,nodeInitializer,OpenMayaMPx.MPxNode.kDependNode )
    except:
        sys.stderr.write( "Failed to register command: %s\n" % nodeName )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeID )
    except:
        sys.stderr.write( "Failed to unregister command: %s\n" % nodeName )
