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
			
# Function dictionary key parameter id and value element
def dictStructuralFraming(structuralFraming):
	dict = {}
	for s in structuralFraming:
		key = s.LookupParameter('id').AsString()
		dict.Add(key, s) 
	return dict

# get the current document
doc = DocumentManager.Instance.CurrentDBDocument

CSVdata = IN[0]

out = []
# collect all level in project
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()
# use function to get level in project.
level_1 = getlevel("LEVEL 01", levels)
# collect all structural fframing elements 
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
# Use function to create dictionary of elements 
dictStruc = dictStructuralFraming(elements)
# Collect all family types of structural framing.
familySymbols = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).OfClass(FamilySymbol).ToElements()

# Loop over CSV information to update
for f in CSVdata[1:]:
	designType = f.designType
	RevitElement = dictStruc[f.id]
	
	if RevitElement.Name != designType:
		type = getFamilyType(f.designType, familySymbols)	
		TransactionManager.Instance.EnsureInTransaction(doc)
		RevitElement.Symbol = type		
		TransactionManager.Instance.TransactionTaskDone()
	
OUT = out