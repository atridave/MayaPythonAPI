'''
Created on Dec 29, 2016

@author: Admin
'''

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaRender as OpenMayaRender

nodeName =  "leftFoot"
nodeID  = OpenMaya.MTypeId(0x100fff)

glRenderer = OpenMayaRender.MHardwareRenderer.theRenderer()
glFT = glRenderer.glFunctionTable()
        
class LocatorNode(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        OpenMayaMPx.MPxLocatorNode.__init__(self)
    
    def compute(self,plug,dataBlock):
        return OpenMaya.kUnknownParameter
    
    def draw(self,view,path,style,status):
        view.beginGL()
        glFT.glPushAttrib(OpenMayaRender.MGL_CURRENT_BIT)
        glFT.glPushAttrib(OpenMayaRender.MGL_BLEND)
        glFT.glBlendFunc(OpenMayaRender.MGL_SRC_ALPHA,OpenMayaRender.MGL_ONE_MINUS_SRC_ALPHA)
        
        if status == view.kActive:
            glFT.glColor4f(0.2,0.5,0.1,0.3)
        elif status == view.kLead:
            glFT.glColor4f(0.5,0.2,0.1,0.3)
        elif status == view.kDormant:
            glFT.glColor4f(0.1,0.1,0.1,0.3)
            
            
        
        glFT.glBegin(OpenMayaRender.MGL_POLYGON)
        glFT.glVertex3f(-0.031,0,-2.875)
        glFT.glVertex3f(-0.939,0.1,-2.370)
        glFT.glVertex3f(-1.175,0.2,-1.731)
        glFT.glVertex3f(-0.603,0.3,1.060)
        glFT.glVertex3f(0.473,0.3,1.026)
        glFT.glVertex3f(0.977,0.2,-1.731)
        glFT.glVertex3f(0.809,0.1,-2.337)
        glFT.glVertex3f(0.035,0,-2.807)
        glFT.glEnd()
        
        
        
        
        
        if status == view.kActive:
            glFT.glColor4f(0.2,0.5,0.1,1)
        elif status == view.kLead:
            glFT.glColor4f(0.5,0.2,0.1,1)
        elif status == view.kDormant:
            glFT.glColor4f(0.1,0.1,0.1,1)
             
        view.drawText('LeftFoot',OpenMaya.MPoint(0,0,0),view.kLeft)   
        
        
        
        
        
        
        glFT.glDisable(OpenMayaRender.MGL_BLEND)
        glFT.glPopAttrib()
        view.endGL()
        
        
    

 
         
        

def nodeCreator():
    return OpenMayaMPx.asMPxPtr(LocatorNode())
        

def nodeInitializer():
    pass
 


    
    
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri dave','1.0')
    try:
        mplugin.registerNode( nodeName, nodeID,nodeCreator,nodeInitializer,OpenMayaMPx.MPxNode.kLocatorNode )
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