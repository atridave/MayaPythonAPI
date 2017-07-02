'''
Created on Dec 19, 2016

@author: Admin
'''



import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaFX as OpenMayaFX

kPluginCmdName = "fxCommand"
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
        
        print 'I have passed line 46'
        print mDagPath.fullPathName()
        mPointArray = OpenMaya.MPointArray()
        mFnMesh.getPoints(mPointArray,OpenMaya.MSpace.kWorld)
        print 'I have passed 49'
        mFnParticle =  OpenMayaFX.MFnParticleSystem()
        self.mObj_particle = mFnParticle.create()
        mFnParticle =  OpenMayaFX.MFnParticleSystem(self.mObj_particle)
        
        counter = 0
        for i in xrange(mPointArray.length()):
            if i%self.sparse == 0:
                mFnParticle.emit(mPointArray[i])
                counter+=1
        print "Total Points : " + str(counter)
        mFnParticle.saveInitialState()
        
        
        
    # Invoked when the command is run.
    def doIt(self,argList):
        self.argumentParser(argList)
        print "Hello Worldaaa!"
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