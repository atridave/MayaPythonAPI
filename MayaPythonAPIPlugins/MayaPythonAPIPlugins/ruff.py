# import the OpenMaya module
import maya.OpenMaya as OpenMaya

# function that returns a node object given a name
def nameToNode( name ):
    selectionList = OpenMaya.MSelectionList()
    selectionList.add( name )
    node = OpenMaya.MObject()
    selectionList.getDependNode( 0, node )
    return node

# function that finds a plug given a node object and plug name
def nameToNodePlug( attrName, nodeObject ):
    depNodeFn = OpenMaya.MFnDependencyNode( nodeObject )
    attrObject = depNodeFn.attribute( attrName )
    plug = OpenMaya.MPlug( nodeObject, attrObject )
    return plug

# Find the persp camera node
print "Find the persp camera"
perspNode = nameToNode( "persp" )
print "APItype %d" % perspNode.apiType()
print "APItype string %s" % perspNode.apiTypeStr()

# Print the translateX value
translatePlug = nameToNodePlug( "translateX", perspNode )
print "Plug name: %s" % translatePlug.name()
print "Plug value %g" % translatePlug.asDouble()