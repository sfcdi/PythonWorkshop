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
	viewList = list()
	
	for view in views:
		if view.IsTemplate == True:
			viewList.append(view)
	return viewList
	
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
out = []

# apply view template to views. 
for v in viewList:
	if v.Name == 'Level 1' or v.Name == 'Level 2':
		TransactionManager.Instance.EnsureInTransaction(doc)
		v.ViewTemplateId = viewTemp[0].Id
		TransactionManager.Instance.TransactionTaskDone()
