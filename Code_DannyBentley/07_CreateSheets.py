# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Get Current document 
doc = DocumentManager.Instance.CurrentDBDocument
# make a array of sheet number and sheet names.
sheetNum = ['S1.01', 'S1.02']
sheetName = ['level 01', 'level 02']
# Send in title block family 
titleblock = UnwrapElement(IN[0])

# Crete sheets and apply sheet number and name
TransactionManager.Instance.EnsureInTransaction(doc)

for i in range(len(sheetNum)):
	newsheet = ViewSheet.Create(doc, titleblock.Id)
	newsheet.SheetNumber = sheetNum[i]
	newsheet.Name = sheetName[i]
	
TransactionManager.Instance.TransactionTaskDone()
