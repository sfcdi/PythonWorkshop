# Enable Python support and load DesignScript library
import clr
import System

# Object class for CSV file data
class framing:
	def __init__(self, row):
		self.id = row[0]
		self.designType = row[1]
		self.End_X = row[2]
		self.End_Y = row[3]
		self.End_Z = row[4]
		self.Start_X = row[5]
		self.Start_Y = row[6]
		self.Start_Z = row[7]
		
# read file from path
filepath = "E:/SFDUG/PythonWorkshop/CSV_files/framing.csv"
filereader = System.IO.StreamReader(filepath)

out = []

# loop over items in CSV file. 
while filereader.Peek() > -1:
	line = filereader.ReadLine()
	row = line.Split(",")
	obj = framing(row)
	out.append(obj)
	
# close file
filereader.Close()
	
OUT = out