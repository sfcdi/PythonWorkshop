# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitNodes')
from Revit.Elements import*

# The inputs to this node will be stored as a list in the IN variables.
family = IN[0]
level = IN[1]
output = []

for x in range(0,100,10):
	point = Point.ByCoordinates(x,0,0)
	columns = FamilyInstance.ByPointAndLevel(family,point,level)
	output.append(columns)

# Place your code below this line

# Assign your output to the OUT variable.
OUT = output