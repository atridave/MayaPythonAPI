'''
Created on Dec 19, 2016

@author: Admin
'''


import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginCmdName = "printScen"

# Command
class scriptedCommand(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        
    # Invoked when the command is run.
    def doIt(self,argList):
        print "Hello World!"
        mitDag =  OpenMaya.MItDag(OpenMaya.MItDag.kDepthFirst,OpenMaya.MFn.kInvalid)
        dagNode =  OpenMaya.MFnDagNode()
        while (not mitDag.isDone()):
            currentObj =  mitDag.currentItem()
            depth = mitDag.depth()
            dagNode.setObject(currentObj)
                
            name  =  dagNode.name()
            type =  currentObj.apiTypeStr()
            path =  dagNode.fullPathName()
                
                
                
            printOut = ""
            for i in range(0,depth):
                printOut +=  '----->'
                
            printOut +=  name + ' : ' + type
                
            print printOut
                        
            mitDag.next()
        

# Creator
def cmdCreator():
    return OpenMayaMPx.asMPxPtr( scriptedCommand() )
    
# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand( kPluginCmdName, cmdCreator )
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

