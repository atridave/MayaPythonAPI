'''
Created on Dec 19, 2016

@author: Admin
'''



import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx


kPluginCmdName = "testPoly"
kHelpFlag =  "-h"
kHelpLongFlag = "-help"
kSparseFlag = "-s"
kSparseLongFlag = '-sparse'
helpMessage =  "This command is used for testing"

# Command
class scriptedCommand(OpenMayaMPx.MPxCommand):
    
    sparse =  None
    
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        
    def isUndoable(self):
        return True
        
        
    def undoIt(self):
        mFnDagNode  = OpenMaya.MFnDagNode(self.mObj_particle)
        mdagMod =  OpenMaya.MDagModifier()
        mdagMod.deleteNode(mFnDagNode.parent(0))
        mdagMod.doIt() 
        
        
        
    def redoIt(self):
        mSel = OpenMaya.MSelectionList()
        mDagPath =  OpenMaya.MDagPath()
        mFnMesh =  OpenMaya.MFnMesh()
        OpenMaya.MGlobal.getActiveSelectionList(mSel)
        if mSel.length() >= 1:
            try:
                mSel.getDagPath(0,mDagPath)
                mFnMesh.setObject(mDagPath)
            except:
                print 'select a poly mesh'
        else :
            print 'select some poly Object'
        
        
        print mDagPath.fullPathName()
        mPointArray = OpenMaya.MPointArray()
        mFnMesh.getPoints(mPointArray,OpenMaya.MSpace.kWorld)
        print mPointArray[0][0] , mPointArray[0][1], mPointArray[0][2]
        pointList = []
        
        
        for i in range(mPointArray.length()):
            pointList.append([mPointArray[i][0],mPointArray[i][1],mPointArray[i][2]])
                 
        print "Total Points %d :" % (mPointArray.length())        
        return pointList
        
        
        
        
    # Invoked when the command is run.
    def doIt(self,argList):
        self.argumentParser(argList)
        
        if self.sparse != None:
            self.redoIt()
    
    def argumentParser(self,argList):
        syntax = self.syntax()
        parsedArguments = OpenMaya.MArgDatabase(syntax,argList)
        if parsedArguments.isFlagSet(kSparseFlag):
            self.sparse = parsedArguments.flagArgumentDouble(kSparseFlag,0)
            
        if parsedArguments.isFlagSet(kSparseLongFlag):
            self.SparseLong = parsedArguments.flagArgumentDouble(kSparseLongFlag,0)
            
        if parsedArguments.isFlagSet(kSparseFlag):
            self.setResult(helpMessage)
            
        if parsedArguments.isFlagSet(kSparseLongFlag):
            self.setResult(helpMessage)
            
    

# Creator
def cmdCreator():
    return OpenMayaMPx.asMPxPtr( scriptedCommand() )


def syntaxCreator():
    syntax = OpenMaya.MSyntax()
    syntax.addFlag(kHelpFlag,kHelpLongFlag)
    syntax.addFlag(kSparseFlag,kSparseLongFlag,OpenMaya.MSyntax.kDouble)
    
    return syntax
    
    
# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand( kPluginCmdName, cmdCreator,syntaxCreator )
    except:
        sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand( kPluginCmdName )
    except:
        sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )