# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#import RevitAPI

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# The inputs to this node will be stored as a list in the IN variables.
familytype = UnwrapElement(IN[0])
output = []

# Place your code below this line
#Assign Document
doc = DocumentManager.Instance.CurrentDBDocument

#Start Transaction
TransactionManager.Instance.EnsureInTransaction(doc)


for x in range (0,100,10):
	fam = doc.Create.NewFamilyInstance(XYZ(x,x,0), familytype,Structure.StructuralType.NonStructural)
	output.append(fam)
	
#End Transaction
TransactionManager.Instance.TransactionTaskDone()
	
# Assign your output to the OUT variable.
OUT = output