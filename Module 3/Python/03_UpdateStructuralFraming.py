# Enable Python support and load DesignScript library
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Function to get family type
def getFamilyType(name, familySymbols):
	for i in familySymbols:
		if Element.Name.GetValue(i) == name:
			return i
			
# Function to get leve by name
def getlevel(name, levels):
	for l in levels:
		if l.Name == name:
			return l
			
# Function dictionary key parameter id and value element
def dictStrucFraming(elements):
	dict = {}
	for i in elements:
		key = i.LookupParameter('id').AsString()
		dict.Add(key, i) 
	return dict

# get the current document
doc = DocumentManager.Instance.CurrentDBDocument

CSVdata = IN[0]

# collect all structural fframing elements 
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
# Use function to create dictionary of elements 
dictStruc = dictStrucFraming(elements)
# Collect all family types of structural framing.
familySymbols = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).OfClass(FamilySymbol).ToElements()

# Loop over CSV information to update
for i in CSVdata[1:]:
	designType = i.designType
	element = dictStruc[i.id]
	
	if element.Name != designType:
		type = getFamilyType(i.designType, familySymbols)	
		TransactionManager.Instance.EnsureInTransaction(doc)
		element.Symbol = type		
		TransactionManager.Instance.TransactionTaskDone()
	