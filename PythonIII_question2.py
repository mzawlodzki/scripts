#! /usr/bin/env Python3

#read in file
InFileName = "Bloom_etal_2018_Reduced_Dataset.csv"
InFile = open(InFileName, 'r')

#initiate variables for line count and size

LineNumber = 0
TotalSize = 0.0

#make loop to read through each line
for Line in InFile:
	LineNumber = LineNumber + 1
	if LineNumber > 1:
		Line = Line.strip('\n')
		ElementList = Line.split(',')
#		print(ElementList[1])		

# extract the taxon name and the size and add to print statement
		print("taxon name: ", ElementList[0],", dia size: ", ElementList[1])	 
#		DiaSum = (ElementList[1])
#		print(DiaSum)
# add sizes together
		TotalSize  = TotalSize + float(ElementList[1])

# print final tally of sizes
print("Total size: ",TotalSize)


InFile.close()
