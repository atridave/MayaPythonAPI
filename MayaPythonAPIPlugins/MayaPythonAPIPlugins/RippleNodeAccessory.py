'''
Created on Dec 24, 2016

@author: Admin
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import math



nodeName = 'RippleDeformer'
nodeID  =  OpenMaya.MTypeId(0xBEEF9)

import maya.cmds as cmds
kApiVersion = cmds.about(apiVersion=True)
if kApiVersion < 201600:
        kInput = OpenMayaMPx.cvar.MPxDeformerNode_input
        kInputGeom = OpenMayaMPx.cvar.MPxDeformerNode_inputGeom
        kOutputGeom = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
        kEnvelope = OpenMayaMPx.cvar.MPxDeformerNode_envelope
else:
        kInput = OpenMayaMPx.cvar.MPxGeometryFilter_input
        kInputGeom = OpenMayaMPx.cvar.MPxGeometryFilter_inputGeom
        kOutputGeom = OpenMayaMPx.cvar.MPxGeometryFilter_outputGeom
        kEnvelope = OpenMayaMPx.cvar.MPxGeometryFilter_envelope


class RippleNode(OpenMayaMPx.MPxDeformerNode):
    
    mObjAmplitude =  OpenMaya.MObject()
    mObjDisplace =  OpenMaya.MObject()
    mObjMatrix =  OpenMaya.MObject()
    
    def __init__(self):
        OpenMayaMPx.MPxDeformerNode.__init__(self)
        
        
    def deform(self, pDataBlock, pGeometryIterator, pLocalToWorldMatrix, pGeometryIndex):
        
        envelopeAttribute = kEnvelope
        envelopeValue = pDataBlock.inputValue( envelopeAttribute ).asFloat()
        
        AmplitudeValue =  pDataBlock.inputValue(RippleNode.mObjAmplitude).asFloat()
        
        DisplaceValue =  pDataBlock.inputValue(RippleNode.mObjDisplace).asFloat()
        
        MtrixAttribute =  pDataBlock.inputValue(RippleNode.mObjMatrix).asMatrix()
        
        mTranceMatrix =  OpenMaya.MTransformationMatrix(MtrixAttribute)
        translationVal = mTranceMatrix.getTranslation(OpenMaya.MSpace.kObject)
        
        inputGeometryObject = self.getDeformerInputGeometry(pDataBlock, pGeometryIndex)    
        
                
        mFloatVectorArrayNormal  = OpenMaya.MFloatVectorArray()
        mFnMesh = OpenMaya.MFnMesh(inputGeometryObject)
        mFnMesh.getVertexNormals(False,mFloatVectorArrayNormal,OpenMaya.MSpace.kObject)
        
        
        while (not pGeometryIterator.isDone()):
            pointsPosition =  pGeometryIterator.position()
            weight =  self.weightValue(pDataBlock, pGeometryIndex, pGeometryIterator.index())
            pointsPosition.x = pointsPosition.x + math.sin(pGeometryIterator.index()+DisplaceValue+translationVal[0])*AmplitudeValue *mFloatVectorArrayNormal[pGeometryIterator.index()].x *envelopeValue *weight
            pointsPosition.Y = pointsPosition.y + math.sin(pGeometryIterator.index()+DisplaceValue+translationVal[0])*AmplitudeValue *mFloatVectorArrayNormal[pGeometryIterator.index()].y *envelopeValue * weight
            pointsPosition.z = pointsPosition.z + math.sin(pGeometryIterator.index()+DisplaceValue+translationVal[0])*AmplitudeValue *mFloatVectorArrayNormal[pGeometryIterator.index()].z *envelopeValue * weight
            
            pGeometryIterator.setPosition(pointsPosition)
            
            
            pGeometryIterator.next()
            
       

            
    def getDeformerInputGeometry(self, pDataBlock, pGeometryIndex):
        
        '''
        Obtain a reference to the input mesh. This mesh will be used to compute our bounding box, and we will also require its normals.
        
        We use MDataBlock.outputArrayValue() to avoid having to recompute the mesh and propagate this recomputation throughout the 
        Dependency Graph.
        
        OpenMayaMPx.cvar.MPxDeformerNode_input and OpenMayaMPx.cvar.MPxDeformerNode_inputGeom (for pre Maya 2016) and 
        OpenMayaMPx.cvar.MPxGeometryFilter_input and OpenMayaMPx.cvar.MPxGeometryFilter_inputGeom (Maya 2016) are SWIG-generated 
        variables which respectively contain references to the deformer's 'input' attribute and 'inputGeom' attribute.   
        '''
        inputAttribute = OpenMayaMPx.cvar.MPxGeometryFilter_input
        inputGeometryAttribute = OpenMayaMPx.cvar.MPxGeometryFilter_inputGeom
        
        inputHandle = pDataBlock.outputArrayValue(inputAttribute)
        inputHandle.jumpToElement(pGeometryIndex)
        inputGeometryObject = inputHandle.outputValue().child(inputGeometryAttribute).asMesh()
        
        return inputGeometryObject
    
    def accessoryNodeSetup(self, MDagModifier):
        mObjLoc = MDagModifier.createNode('locator')
        mFnDependLoc =  OpenMaya.MFnDependencyNode(mObjLoc)
        mPlugMatrix = mFnDependLoc.findPlug('worldMatrix')
        mObjWorldAttr = mPlugMatrix.attribute() 
        
        MDagModifier.connect(mObjLoc,mObjWorldAttr,self.thisMObject(),RippleNode.mObjMatrix)
    
    def accessoryAttribute(self):
        return RippleNode.mObjMatrix
        

        
        




def nodeCreator():
    nodePtr = OpenMayaMPx.asMPxPtr(RippleNode())
    return nodePtr
    

def nodeInitializer():
    
    numericAttributeFn = OpenMaya.MFnNumericAttribute()
    
    RippleNode.mObjAmplitude =  numericAttributeFn.create('Amplitude','amp',OpenMaya.MFnNumericData.kFloat ,0.0)
    numericAttributeFn.setMin(0.0)
    numericAttributeFn.setMax(1.0)
    numericAttributeFn.setKeyable(1)    
    RippleNode.addAttribute(RippleNode.mObjAmplitude)
    
    RippleNode.mObjDisplace =  numericAttributeFn.create('Displace','dis',OpenMaya.MFnNumericData.kFloat ,0.0)
    numericAttributeFn.setMin(0.0)
    numericAttributeFn.setMax(10.0)
    numericAttributeFn.setKeyable(1)    
    RippleNode.addAttribute(RippleNode.mObjDisplace)
    
    
    mFnMatrixAttr =  OpenMaya.MFnMatrixAttribute()
    RippleNode.mObjMatrix = mFnMatrixAttr.create('MtrixAttribute','matAttr')
    mFnMatrixAttr.setStorable(0)
    mFnMatrixAttr.setConnectable(1)
    RippleNode.addAttribute(RippleNode.mObjMatrix)
    
    
    
    print dir(OpenMayaMPx.cvar)
    
    RippleNode.attributeAffects(RippleNode.mObjAmplitude,kOutputGeom)
    RippleNode.attributeAffects(RippleNode.mObjDisplace,kOutputGeom)
    RippleNode.attributeAffects(RippleNode.mObjMatrix,kOutputGeom)
    cmds.makePaintable(nodeName, 'weights', attrType='multiFloat', shapeMode='deformer')
    
   


def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri Dave','1.0')
    try:
        mplugin.registerNode(nodeName, nodeID,nodeCreator,nodeInitializer,OpenMayaMPx.MPxNode.kDeformerNode )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % nodeName )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeID )
    except:
        sys.stderr.write( "Failed to deregister node: %s\n" % nodeID )
