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

# Function to override an element.
def OverrideElement(element, color, fill):
	i = OverrideGraphicSettings()
	i.SetProjectionFillColor(color)
	i.SetProjectionFillPatternId(fill.Id)
	doc.ActiveView.SetElementOverrides(element.Id, i)
	
# Get the current document. 
doc = DocumentManager.Instance.CurrentDBDocument
# Collect all structural framing elements. 
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
# Create a Revit API color 
red = Autodesk.Revit.DB.Color(255, 0, 0)
# Fill pattern from Dynamo.
fill = UnwrapElement(IN[0])

# Loop over elements and search for type to override.
for i in elements:
	if i.Name == 'HSS6X0.125':
		TransactionManager.Instance.EnsureInTransaction(doc)
		OverrideElement(i, red, fill)
		TransactionManager.Instance.TransactionTaskDone()