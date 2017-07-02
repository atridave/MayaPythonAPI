'''
Created on Dec 23, 2016

@author: Atri
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaAnim as OpenMayaAnim

nodeName =  "speedNode"
nodeID  = OpenMaya.MTypeId(0x100fff)

class speedNode(OpenMayaMPx.MPxNode):
    
    startFrame =  OpenMaya.MObject()
    endFrame =  OpenMaya.MObject()
    realTime  = OpenMaya.MObject()
    speed =  OpenMaya.MObject()
    sTx = OpenMaya.MObject()
    sTy = OpenMaya.MObject()
    sTz = OpenMaya.MObject()
    outTx = OpenMaya.MObject()
    outTy = OpenMaya.MObject()
    outTz = OpenMaya.MObject()
    vecAttrIn =  OpenMaya.MVector()
    vecAttrOut =  OpenMaya.MVector()
    
    
    
    
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self,plug,dataBlock):
        #print self.thisMObject().apiType()
        #print self.thisMObject().apiTypeStr()
        depNodeFn = OpenMaya.MFnDependencyNode( self.thisMObject() )
        attrObject = depNodeFn.attribute( 'sTx' )
        plug = OpenMaya.MPlug( self.thisMObject(), attrObject )
        
        #print plug.name()
        #print plug.asDouble()
        
        time = OpenMayaAnim.MAnimControl.currentTime()              
        
        value_curr = plug.asDouble(OpenMaya.MDGContext(time))
        print 'Values in time %d ---> %d' % (time.value() ,value_curr)
        
        value_10 = plug.asDouble(OpenMaya.MDGContext(time+10))
        print 'Values in time %d ---> %d' % ((time.value()+10) ,value_10)
        
        value_20 = plug.asDouble(OpenMaya.MDGContext(time+20))
        print 'Values in time %d ---> %d' % ((time.value()+20) ,value_20)
        
        if plug == speedNode.realTime:
            dataHandletimeSVal =  dataBlock.inputValue(speedNode.startFrame)
            timeSVal = dataHandletimeSVal.asFloat()
            dataHandletimeEVal =  dataBlock.inputValue(speedNode.endFrame)
            timeEVal = dataHandletimeEVal.asFloat()
            
            timeFrameS =  ((timeEVal-timeSVal)/30.00)
            
            dataHandtimeVal = dataBlock.outputValue(speedNode.realTime)
            dataHandtimeVal.setFloat(timeFrameS)
            dataBlock.setClean(plug)
            
        if plug == speedNode.vecAttrOut:
            print 'Hello'
            dataBlock.setClean(plug)
            
        if plug ==  speedNode.outTx or speedNode.outTy or speedNode.outTz:
            dataHandleInTxVal =  dataBlock.inputValue(speedNode.sTx)
            txVal =  dataHandleInTxVal.asFloat()
            dataHandleInTyVal =  dataBlock.inputValue(speedNode.sTy)
            tyVal =  dataHandleInTyVal.asFloat()
            dataHandleInTzVal =  dataBlock.inputValue(speedNode.sTz)
            tzVal =  dataHandleInTzVal.asFloat()
            
            newTxVal =  (txVal*2)
            newTyVal =  (tyVal*2)
            newTzVal =  (tzVal*2)
            
            dataHandleOutTxVal = dataBlock.outputValue(speedNode.outTx)
            dataHandleOutTxVal.setFloat(newTxVal)
            dataHandleOutTyVal = dataBlock.outputValue(speedNode.outTy)
            dataHandleOutTyVal.setFloat(newTyVal)
            dataHandleOutTzVal = dataBlock.outputValue(speedNode.outTz)
            dataHandleOutTzVal.setFloat(newTzVal)
            dataBlock.setClean(plug)     

        
        

def nodeCreator():
    return OpenMayaMPx.asMPxPtr(speedNode())



 

def nodeInitializer():
    

    
    mFnAttr =  OpenMaya.MFnNumericAttribute()
    cAttr = OpenMaya.MFnCompoundAttribute()
    
    
    speedNode.startFrame = mFnAttr.create("startFrame",'st',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    speedNode.endFrame = mFnAttr.create("EndFrame",'ed',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    speedNode.speed = mFnAttr.create("speed",'spd',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0)
    
    speedNode.realTime = mFnAttr.create("time",'ti',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0)
    
    speedNode.sTx = mFnAttr.create("sTx",'stx',OpenMaya.MFnNumericData.kVectorArray,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)

    
    speedNode.sTy = mFnAttr.create("sTy",'sty',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)

    
    speedNode.sTz = mFnAttr.create("sTz",'stz',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
 
    
    speedNode.outTx = mFnAttr.create("outTx",'otx',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0)
    
    speedNode.outTy = mFnAttr.create("outdTy",'dty',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0)
    
    
    speedNode.outTz = mFnAttr.create("outdTz",'dtz',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0)
    
    
    speedNode.vecAttrIn = cAttr.create("vectorIn", "vecIn")
     
    speedNode.vecAttrInX = mFnAttr.create("vectorInX",'vecInX',OpenMaya.MFnNumericData.kFloat)
    speedNode.vecAttrInY = mFnAttr.create("vectorInY",'vecInY',OpenMaya.MFnNumericData.kFloat)
    speedNode.vecAttrInZ = mFnAttr.create("vectorInZ",'vecInZ',OpenMaya.MFnNumericData.kFloat)    
    cAttr.setArray(1)
    cAttr.addChild(speedNode.vecAttrInX)
    cAttr.addChild(speedNode.vecAttrInY)
    cAttr.addChild(speedNode.vecAttrInZ)
    cAttr.setReadable(1)
    cAttr.setStorable(1)
    cAttr.setWritable(1)
    cAttr.setKeyable(1)   
    
    
    
    speedNode.vecAttrOut = cAttr.create("vectorOut", "vecOut")
    speedNode.vecAttrOutX = mFnAttr.create("vectorOutX",'vecOX',OpenMaya.MFnNumericData.kFloat)
    speedNode.vecAttrOutY = mFnAttr.create("vectorOutY",'vecOY',OpenMaya.MFnNumericData.kFloat)
    speedNode.vecAttrOutZ = mFnAttr.create("vectoroutZ",'vecOZ',OpenMaya.MFnNumericData.kFloat)
    
    cAttr.setArray(1)
    cAttr.addChild(speedNode.vecAttrOutX)
    cAttr.addChild(speedNode.vecAttrOutY)
    cAttr.addChild(speedNode.vecAttrOutZ)
    cAttr.setReadable(1)
   
    
  
    

    

    
    
    
    
    
    speedNode.addAttribute(speedNode.startFrame)
    speedNode.addAttribute(speedNode.endFrame)
    speedNode.addAttribute(speedNode.speed)
    speedNode.addAttribute(speedNode.sTx)
    speedNode.addAttribute(speedNode.sTy)
    speedNode.addAttribute(speedNode.sTz)
    speedNode.addAttribute(speedNode.outTx)
    speedNode.addAttribute(speedNode.outTy)
    speedNode.addAttribute(speedNode.outTz)
    speedNode.addAttribute(speedNode.vecAttrIn)
    speedNode.addAttribute(speedNode.vecAttrOut)

    speedNode.addAttribute(speedNode.realTime)
    
    speedNode.attributeAffects(speedNode.startFrame,speedNode.realTime)
    speedNode.attributeAffects(speedNode.endFrame,speedNode.realTime)
    speedNode.attributeAffects(speedNode.vecAttrIn,speedNode.vecAttrOut)
        
    speedNode.attributeAffects(speedNode.sTx,speedNode.outTx)
    speedNode.attributeAffects(speedNode.sTy,speedNode.outTy)
    speedNode.attributeAffects(speedNode.sTz,speedNode.outTz)
     
    



def getVector():
    mSel = OpenMaya.MSelectionList()
    mDagPath =  OpenMaya.MDagPath()
    OpenMaya.MGlobal.getActiveSelectionList(mSel)
    mSel.getDagPath(0,mDagPath)
    obj = mDagPath.fullPathName()
    print obj
    mTrans = OpenMaya.MFnTransform(mDagPath)
    trans =  OpenMaya.MVector()
    trans = mTrans.getTranslation(OpenMaya.MSpace.kWorld)
    print trans.x , trans.y,trans.z
    mMtrix =  OpenMaya.MMatrix()
    mMtrix = mTrans.transformationMatrix()
    mMtrix.matrix
    return trans
    print 'Hellow will compute'


    





    
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri Dave','1.0')
    try:
        mplugin.registerNode( nodeName, nodeID,nodeCreator,nodeInitializer )
    except:
        sys.stderr.write( "Failed to register Node: %s\n" % nodeName )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeID )
    except:
        sys.stderr.write( "Failed to unregister Node: %s\n" % nodeName )