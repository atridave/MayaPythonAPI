'''
Created on Feb 1, 2017

@author: Atri Dave
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
# import maya.OpenMayaAnim as OpenMayaAnim
import math

nodeName =  "velocityNode"
nodeID  = OpenMaya.MTypeId(0x7ffff)

class velocityNode(OpenMayaMPx.MPxNode):
    
    velocity =  OpenMaya.MObject()
    inPutCurrentX = OpenMaya.MObject()
    inPutCurrentY = OpenMaya.MObject()
    inPutCurrentZ = OpenMaya.MObject()
    inPutPastX = OpenMaya.MObject()
    inPutPastY = OpenMaya.MObject()
    inPutPastZ = OpenMaya.MObject()
    inPutFutureX = OpenMaya.MObject()
    inPutFutureY = OpenMaya.MObject()
    inPutFutureZ = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self,plug,dataBlock):                           
          
        if plug == velocityNode.velocity:
#             plugX = OpenMaya.MPlug( self.thisMObject(), OpenMaya.MFnDependencyNode(self.thisMObject()).attribute('inPutCurrentX'))
#             plugY = OpenMaya.MPlug( self.thisMObject(), OpenMaya.MFnDependencyNode(self.thisMObject()).attribute('inPutY'))
#             plugZ = OpenMaya.MPlug( self.thisMObject(), OpenMaya.MFnDependencyNode(self.thisMObject()).attribute('inPutZ'))
#             time = OpenMayaAnim.MAnimControl.currentTime()
#             valXPast = plugX.asDouble(OpenMaya.MDGContext(time-1))
#             valYPast = plugY.asDouble(OpenMaya.MDGContext(time-1))
#             valZPast = plugZ.asDouble(OpenMaya.MDGContext(time-1))
#             valXcurr = plugX.asDouble(OpenMaya.MDGContext(time))
#             valYcurr = plugY.asDouble(OpenMaya.MDGContext(time))
#             valZcurr = plugZ.asDouble(OpenMaya.MDGContext(time))
#             valXNext = plugX.asDouble(OpenMaya.MDGContext(time+1))
#             valYNext = plugY.asDouble(OpenMaya.MDGContext(time+1))
#             valZNext = plugZ.asDouble(OpenMaya.MDGContext(time+1))
                     
#             
#             velocityVal =  (( (math.sqrt(((valXNext-valXcurr)*( valXNext-valXcurr))+(( valYNext-valYcurr)*(valYNext-valYcurr))+(( valZNext-valZcurr)*(valZNext-valZcurr))) +
#                     math.sqrt(((valXcurr-valXPast)*(valXcurr-valXPast))+((valYcurr-valYPast)*(valYcurr-valYPast))+((valZcurr-valZPast)*(valZcurr-valZPast))))*0.5 ) *30)

            
            valXcurr =  dataBlock.inputValue(velocityNode.inPutCurrentX).asFloat()
            valYcurr =  dataBlock.inputValue(velocityNode.inPutCurrentY).asFloat()
            valZcurr =  dataBlock.inputValue(velocityNode.inPutCurrentZ).asFloat()
            valXPast =  dataBlock.inputValue(velocityNode.inPutPastX).asFloat()
            valYPast =  dataBlock.inputValue(velocityNode.inPutPastY).asFloat()
            valZPast =  dataBlock.inputValue(velocityNode.inPutPastZ).asFloat()
            valXNext =  dataBlock.inputValue(velocityNode.inPutFutureX).asFloat()
            valYNext =  dataBlock.inputValue(velocityNode.inPutFutureY).asFloat()
            valZNext =  dataBlock.inputValue(velocityNode.inPutFutureZ).asFloat()
#             velocityVal = valXcurr+valYcurr+valZcurr
            

            velocityVal =  (( (math.sqrt(((valXNext-valXcurr)*( valXNext-valXcurr))+(( valYNext-valYcurr)*(valYNext-valYcurr))+(( valZNext-valZcurr)*(valZNext-valZcurr))) +
                     math.sqrt(((valXcurr-valXPast)*(valXcurr-valXPast))+((valYcurr-valYPast)*(valYcurr-valYPast))+((valZcurr-valZPast)*(valZcurr-valZPast))))*0.5 ) *30)

            
            dataHandlevelocityVal =  dataBlock.outputValue(velocityNode.velocity)
            dataHandlevelocityVal.setFloat(velocityVal)            
            dataBlock.setClean(plug)
        else :
            return OpenMaya.kUnknownParameter                  
            
            
def nodeCreator():
    return OpenMayaMPx.asMPxPtr(velocityNode())


def nodeInitializer():
    
    mFnAttr =  OpenMaya.MFnNumericAttribute()
    velocityNode.velocity = mFnAttr.create("velocity",'velo',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0) 

    velocityNode.inPutCurrentX = mFnAttr.create("inPutCurrentX",'incX',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
         
    velocityNode.inPutCurrentY = mFnAttr.create("inPutCurrentY",'incY',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
     
    velocityNode.inPutCurrentZ = mFnAttr.create("inPutCurrentZ",'incZ',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    velocityNode.inPutPastX = mFnAttr.create("inPutPastX",'inpX',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
         
    velocityNode.inPutPastY = mFnAttr.create("inPutPastY",'inpY',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
     
    velocityNode.inPutPastZ = mFnAttr.create("inPutPastZ",'inpZ',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    
    velocityNode.inPutFutureX = mFnAttr.create("inPutFutureX",'infX',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
         
    velocityNode.inPutFutureY = mFnAttr.create("inPutFutureY",'infY',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
     
    velocityNode.inPutFutureZ = mFnAttr.create("inPutFutureZ",'infZ',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
   
   
            
    velocityNode.addAttribute(velocityNode.velocity)
    velocityNode.addAttribute(velocityNode.inPutCurrentX)
    velocityNode.addAttribute(velocityNode.inPutCurrentY)
    velocityNode.addAttribute(velocityNode.inPutCurrentZ)
    velocityNode.addAttribute(velocityNode.inPutPastX)
    velocityNode.addAttribute(velocityNode.inPutPastY)
    velocityNode.addAttribute(velocityNode.inPutPastZ)
    velocityNode.addAttribute(velocityNode.inPutFutureX)
    velocityNode.addAttribute(velocityNode.inPutFutureY)
    velocityNode.addAttribute(velocityNode.inPutFutureZ)
         
    velocityNode.attributeAffects(velocityNode.inPutCurrentX,velocityNode.velocity)
    velocityNode.attributeAffects(velocityNode.inPutCurrentY,velocityNode.velocity)
    velocityNode.attributeAffects(velocityNode.inPutCurrentZ,velocityNode.velocity)


    
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri Dave','1.0')
    try:
        mplugin.registerNode( nodeName, nodeID,nodeCreator,nodeInitializer )
    except:
        sys.stderr.write( "Failed to register Node: %s\n" % nodeName )
        raise

def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeID )
    except:
        sys.stderr.write( "Failed to unregister Node: %s\n" % nodeName )