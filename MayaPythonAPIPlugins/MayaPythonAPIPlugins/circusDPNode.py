'''
Created on Mar 4, 2017

@author: Admin
'''
import math,sys
import maya.OpenMaya as OM
import maya.OpenMayaMPx as MPx
import maya.OpenMayaAnim as Anim

nodeName = "circusDPNode"
nodeId = OM.MTypeId(0x00032331)

class circusDPNode(MPx.MPxNode):

    aInTargetMatrices = OM.MObject()
    aTargetSelector = OM.MObject()
    aInConstraintMatrix = OM.MObject()
    aOutOffsetTranslate = OM.MObject()
    aOutOffsetTranslateX = OM.MObject()
    aOutOffsetTranslateY = OM.MObject()
    aOutOffsetTranslateZ = OM.MObject()
    aOutOffsetRotate = OM.MObject()
    aOutOffsetRotateX = OM.MObject()
    aOutOffsetRotateY = OM.MObject()
    aOutOffsetRotateZ = OM.MObject()

    def compute(self,plug,data):

        if (plug == self.aOutOffsetTranslate or plug == self.aOutOffsetRotate):

            selector = data.inputValue(self.aTargetSelector)
            parentIndex = selector.asInt()
            thisNode = self.thisMObject()
            plugArray = OM.MPlug(self.aInTargetMatrices)
            outRotArray = OM.MPlug(self.aOutOffsetRotate)
            outTransArray = OM.MPlug(self.aOutOffsetTranslate)
            numInPlugs = plugArray.numElements()
            numOutRot = outRotArray.numElements()
            numOutTrans = outTransArray.numElements()
            if parentIndex > -1:
                if numINPlugs in range(parentIndex):

                    parent = data.inputArrayValue(self.aInTargetMatrices)
                    parent = data.jumpToElement(parentIndex)
                    parentMatrixValue = parent.inputValue()
                    parentMatrix = parentMatrixValue.asMatrix()
                    constraint = data.inputValue(self.aInConstraintMatrix)
                    constraintMatrix = constraint.asMatrix()
                    mOutMatrix = OM.MTransformationMatrix(parentMatrix.inverse() * constraintMatrix)
                    vOutPos = OM.MVector(mOutMatrix.getTranslation(OM.MSpace.kTransform))
                    vOutRot = OM.MEulerRotation(mOutMatrix.eulerRotation())
                    vTargetAxis *= parentMatrix
                    vConstraintAxiz *= constraintMatrix
                    vToTarget = OM.MVector(
                        parentMatrix(3,0) - constraintMatrix(3,0), 
                        parentMatrix(3,1) - constraintMatrix(3,1), 
                        parentMatrix(3,2) - constraintMatrix(3,2))
                    outputHandle = data.outputArrayValue(self.aOutOffsetTranslate)
                    outputHandle.jumpToElement(parentIndex)
                    outputHandle.set3Double(vOutPos.x,vOutPos.y,vOutPos.z)
                    outputHandle = data.outputArrayValue(self.aOutOffsetRotate)
                    outputHande.jumpToElement(parentIndex)
                    outputHandle.set3Double(math.degrees(vOutRot.x),math.degrees(vOutRot.y),math.degrees(vOutRot.z))
                    data.setClean(self.aOutOffsetRotate)
                    data.setClean(self.aOutOffsetTranslate)

                else:                    
                    OM.MGloabl.displayWarning("Not enough targets or outputs")

            else:
                return OM.MStatus()

        else:
            return OM.kUnknownParameter

        return OM.MStatus.kSuccess

    @classmethod
    def createNode(cls):
        return MPx.asMPxPtr(cls())

    @classmethod
    def initializeNode(cls):

        mAttr = OM.MFnMatrixAttribute()
        nAttr = OM.MFnNumericAttribute()
        pAttr = OM.MFnMatrixAttribute()
        oAttr = OM.MFnNumericAttribute()
        uAttr = OM.MFnUnitAttribute()
        cls.aInConstraintMatrix = mAttr.create("inConstraintMatrix","icm")
        mAttr.setAffectsWorldSpace(True)
        cls.aInTargetMatrices = pAttr.create("inTargetMatrix","itm")
        pAttr.setArray(True)
        pAttr.setUsesArrayDataBuilder(True)
        pAttr.setAffectsWorldSpace(True)
        cls.aTargetSelector = nAttr.create("parentSelector","ps",OM.MFnNumericData.kInt,0)
        nAttr.setMin(-1)
        nAttr.setDefault(-1)
        cls.aOutOffsetTranslateX = oAttr.create("outOffsetTranslateX","ootx",OM.MFnNumericData.kDouble,0.0)
        cls.aOutOffsetTranslateY = oAttr.create("outOffsetTranslateY","ooty",OM.MFnNumericData.kDouble,0.0)
        cls.aOutOffsetTranslateZ = oAttr.create("outOffsetTranslateZ","ootz",OM.MFnNumericData.kDouble,0.0)
        cls.aOutOffsetTranslate = oAttr.create("outOffsetTranslate","oot",cls.aOutOffsetTranslateX,cls.aOutOffsetTranslateY,cls.aOutOffsetTranslateZ)
        oAttr.setArray(True)
        oAttr.setUsesArrayDataBuilder(True)
        cls.aOutOffsetRotateX = uAttr.create("outOffsetRotateX","oorx",OM.MFnUnitAttribute.kAngle,0.0)
        cls.aOutOffsetRotateY = uAttr.create("outOffsetRotateY","oory",OM.MFnUnitAttribute.kAngle,0.0)
        cls.aOutOffsetRotateZ = uAttr.create("outOffsetRotateZ","oorz",OM.MFnUnitAttribute.kAngle,0.0)
        cls.aOutOffsetRotate = oAttr.create("outOffsetRotate","oor",cls.aOutOffsetRotateX,cls.aOutOffsetRotateY,cls.aOutOffsetRotateZ)
        oAttr.setArray(True)
        oAttr.setUsesArrayDataBuilder(True)
        cls.addAttribute(cls.aInConstraintMatrix)
        cls.addAttribute(cls.aInTargetMatrices)
        cls.addAttribute(cls.aTargetSelector)
        cls.addAttribute(cls.aOutOffsetTranslate)
        cls.addAttribute(cls.aOutOffsetRotate)
        cls.attributeAffects(cls.aTargetSelector,cls.aOutOffsetTranslate)
        cls.attributeAffects(cls.aTargetSelector,cls.aOutOffsetRotate)

def initializePlugin(mobject):

    mplugin = MPx.MFnPlugin(mobject)

    try:

        mplugin.registerNode(nodeName,nodeId,circusDPNode.createNode,circusDPNode.initializeNode)

    except:

        sys.stderr.write("registerNode failed")   
        raise   

def uninitializePlugin(mobject):

    mplugin = MPx.MFnPlugin(mobject)

    try:

        mplugin.deregisterNode(nodeId)

    except:

        sys.stderr.write("deregisterNode failed")   
        raise 