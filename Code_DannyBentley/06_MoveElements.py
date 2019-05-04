import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("System")
from System.Collections.Generic import *

# Get current document 
doc = DocumentManager.Instance.CurrentDBDocument
# Collect all structural framing elements 
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
# List of elements ids 
Ids = List[ElementId]()
# New location to move all elements. 
newLocation = XYZ(10, 10, 0)
# Add element ids to list.
for e in elements:
	Ids.Add(e.Id)

TransactionManager.Instance.EnsureInTransaction(doc)
# Move list of elements. 
ElementTransformUtils.MoveElements(doc, Ids, newLocation)
TransactionManager.Instance.TransactionTaskDone()
