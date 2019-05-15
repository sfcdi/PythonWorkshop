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

# Function to get all view templates. 
def GetViewTemplate():
	views = FilteredElementCollector(doc).OfClass(View)
	viewTemp = list()
	
	for i in views:
		if i.IsTemplate == True:
			viewTemp.append(i)
	return viewTemp
	
# Function to collect all view in project. 
def GetViews():
	views = FilteredElementCollector(doc).OfClass(View)
	return views

# Get Current document 
doc = DocumentManager.Instance.CurrentDBDocument
# use function to view 
viewList = GetViews()
# use function to get view templates 
viewTemp = GetViewTemplate()

# apply view template to views. 
for i in viewList:
	if i.Name == 'Level 1' or i.Name == 'Level 2':
		TransactionManager.Instance.EnsureInTransaction(doc)
		i.ViewTemplateId = viewTemp[0].Id
		TransactionManager.Instance.TransactionTaskDone()
