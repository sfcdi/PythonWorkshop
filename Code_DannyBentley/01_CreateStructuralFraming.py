# Enable Python support and load DesignScript library
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Function to get family type
def getFamilyType(name, familySymbols):
	for i in familySymbols:
		if Autodesk.Revit.DB.Element.Name.GetValue(i) == name:
			return i
# Function to get leve by name	
def getlevel(name, levels):
	for l in levels:
		if l.Name == name:
			return l
#Current document
doc = DocumentManager.Instance.CurrentDBDocument
# data from CSV file
CSVdata = IN[0]

out = []
# collect all level in project
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
# use function to get level in project.
level_1 = getlevel("LEVEL 01", levels)

# collect all structural fframing types
familySymbols = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).OfClass(FamilySymbol).ToElements()

# loop over CSV data 
for f in CSVdata[1:]:
	sx = float(f.Start_X)
	sy = float(f.Start_Y)
	sz = float(f.Start_Z)
	ex = float(f.End_X)
	ey = float(f.End_Y)
	ez = float(f.End_Z)
	# create Revit points and lines. 
	point_S = XYZ(sx, sy, sz)
	point_E = XYZ(ex, ey, ez)
	line = Autodesk.Revit.DB.Line.CreateBound(point_S, point_E)
	# get familly type using function.
	type = getFamilyType(f.designType, familySymbols)
	
	# start transaction to create elements. 
	TransactionManager.Instance.EnsureInTransaction(doc)
	if type.IsActive == False:
		type.Activate()
		doc.Regenerate()
	new_framing = doc.Create.NewFamilyInstance(line, type, level_1, Structure.StructuralType.Beam)
	TransactionManager.Instance.TransactionTaskDone()

	# set parameter Id to update element in future. 
	TransactionManager.Instance.EnsureInTransaction(doc)
	doc.Regenerate()
	p = new_framing.LookupParameter('id')
	p.Set(f.id)
	TransactionManager.Instance.TransactionTaskDone()
	out.append(framing)

	# Help visualize in Dynamo using Dynamo. 
	#point_I = Autodesk.DesignScript.Geometry.Point.ByCoordinates(sx, sy, sz)
	#point_J = Autodesk.DesignScript.Geometry.Point.ByCoordinates(ex, ey, ez)
	#line = Autodesk.DesignScript.Geometry.Line.ByStartPointEndPoint(point_I, point_J)	
	#out.append(line)

OUT = out