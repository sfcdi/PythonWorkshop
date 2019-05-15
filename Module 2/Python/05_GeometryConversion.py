# Enable Python Support and load DesignScript Library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#Import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

#Import Manger classes
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#Import DSType method
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

#Inputs to this Node
fam = UnwrapElement(IN[0])
output = []

#Assign Document
doc = DocumentManager.Instance.CurrentDBDocument

#Start Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

for x in range (0,50,10):
	famarray = doc.Create.NewFamilyInstance(XYZ(x,x,0),fam, Structure.StructuralType.NonStructural)
	wrappedfamarray = famarray.ToDSType(False)
	
	xyz = XYZ(x,x,0)
	output.append(xyz.ToPoint())
	


#Assign your output to the OUT variable
OUT = output