'''
Created on Dec 4, 2016

@author: Admin
'''
import maya.cmds as cmds
import maya.OpenMaya as om


sel = cmds.ls(sl=1)

mSel =  om.MSelectionList()
for i in range(0,len(sel)):
    mSel.add(sel[i])

mObj =  om.MObject()
mDagPath =  om.MDagPath()


mSel.getDependNode(0,mObj)
mSel.getDagPath(0,mDagPath)

print mDagPath.fullPathName()

mFnMesh =  om.MFnMesh(mDagPath)
print mFnMesh.fullPathName()

mFnDependNode  = om.MFnDependencyNode(mObj)
print mFnDependNode.name()

mPlugArray =  om.MPlugArray()
mFnMesh.getConnections(mPlugArray)
print mPlugArray[1].name()
mPlugArray1 =  om.MPlugArray()

mPlugArray[1].connectedTo(mPlugArray1,1,0)
print mPlugArray1.length()
print mPlugArray1[0].name()
mObj2 =  mPlugArray1[0].node()
mFnDependNode2  = om.MFnDependencyNode(mObj2)
print mFnDependNode2.name()
print mFnDependNode2.absoluteName()


width=  mFnDependNode2.findPlug("width")

print width.asInt()
width.setInt(20)