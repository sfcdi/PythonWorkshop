# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('System')
from System.Collections.Generic import *

# Get current document.
doc = DocumentManager.Instance.CurrentDBDocument
# collect all structural elements. 
elements = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
# create angle and axis point to rotate around. 
angle = 45
origin = XYZ(0,0,0)
offset = XYZ(0,0,1)
rot_axis = Line.CreateBound(origin, offset)
# List of element ids 
Ids = List[ElementId]()

# Add all element ids to list. 
for e in elements:
	Ids.Add(e.Id)
	
TransactionManager.Instance.EnsureInTransaction(doc)
# Rotate list of elements. 
ElementTransformUtils.RotateElements(doc, Ids, rot_axis, angle)
TransactionManager.Instance.TransactionTaskDone()
	