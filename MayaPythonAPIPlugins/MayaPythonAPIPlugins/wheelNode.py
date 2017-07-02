'''
Created on Dec 23, 2016

@author: Atri
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

nodeName =  "wheelNode"
nodeID  = OpenMaya.MTypeId(0x100fff)

class wheelNode(OpenMayaMPx.MPxNode):
    
    inRadius =  OpenMaya.MObject()
    inTranslate =  OpenMaya.MObject()
    outRotate =  OpenMaya.MObject()
    
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self,plug,dataBlock):
        '''
        rotate  =  translate/(2*3.14*radius)*(-360)
        '''
        
        if plug ==  wheelNode.outRotate :
            dataHandleTraslate =  dataBlock.inputValue(wheelNode.inTranslate)
            dataHandleRadius =  dataBlock.inputValue(wheelNode.inRadius)
            
            inRadiusVal =  dataHandleRadius.asFloat()
            inTranslateVal = dataHandleTraslate.asFloat()
            
            outRotate =  float(inTranslateVal)/float(2*3.14*inRadiusVal)*(-360)
            dataHandleRotate =  dataBlock.outputValue(wheelNode.outRotate)
            dataHandleRotate.setFloat(outRotate)
            dataBlock.setClean(plug)
            
        else :
            return OpenMaya.kUnknownParameter
        
        
        

def nodeCreator():
    return OpenMayaMPx.asMPxPtr(wheelNode())
        

def nodeInitializer():
    mFnAttr =  OpenMaya.MFnNumericAttribute()
    
    wheelNode.inRadius = mFnAttr.create("radius",'r',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    wheelNode.inTranslate = mFnAttr.create("translate",'t',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    wheelNode.outRotate = mFnAttr.create("rotate",'rot',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0)
    
    
    wheelNode.addAttribute(wheelNode.inRadius)
    wheelNode.addAttribute(wheelNode.inTranslate)
    wheelNode.addAttribute(wheelNode.outRotate)
    
    wheelNode.attributeAffects(wheelNode.inRadius,wheelNode.outRotate)
    wheelNode.attributeAffects(wheelNode.inTranslate,wheelNode.outRotate)
    
    
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri Dave','1.0')
    try:
        mplugin.registerNode( nodeName, nodeID,nodeCreator,nodeInitializer )
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