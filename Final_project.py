#! /bin/usr/python3


####	Usage:
####	Script takes in a fastq file (1)
####	trims it according to quality score line (2)
####	and outputs a fasta file (3)

#### 	Input the name of fastq file on line 37
####	Input the name of output file on line 22


#import sys
import re

#import iterator
#head -n 128 chogra01_chondestes_grammacus_nk276103-READ1.fastq > practice_file_2.fastq

#InFile = ("Test_file.fasta")

#	create outfile and open it for writing
OutFileName = ("Test_file_2.fasta")
OutFile = open(OutFileName, 'w')

#		InFileName.strip(".txt")
#		print(InFile)

#	Set line number counter and a new list to write to
LineNumber = 1
TempFastq = []

#	Loop that opens the fastq file, reads it in, and trims the end of the quality score line
#	based on the presence of >, <, =, ;, and :
# 	The regular expression can be changed depending on how the user wants to trim the quality score
#	Results of the loop are written to a list: TempFastq

for Line in open("Test_file.fastq",'r'):
	if LineNumber % 4 == 0:
		Line = Line.strip("\n")
		Find = '(\S+)[\>\<\=\;\:]\S+'
		Result = re.search(Find, Line)	
#		print(Result)	
		Replace = r'\1'
		Quality = re.sub(Find, Replace, Line)
		TempFastq.append(Quality)

	else:
		Line = Line.strip("\n")
		TempFastq.append(Line)
		LineNumber += 1
	
#print(TempFastq)

#	New variable to count number of lines in the TempFastq list
#	Allows the script to work with multiple files, rather than if I'd hard-coded the number of lines in the fastq file

FileCount = 0

for Line in TempFastq:
	FileCount += 1
#print(FileCount)

#	Initiate new list and new line count

Outputstring = []
LineNumber_cats = 1

#	Loop that counts the length of the trimmed quality score line and outputs to Outputstring list
#	(Probably not necessary to nest in a while loop for number of lines in the file, but I did)

while LineNumber_cats <= FileCount:
	for Line in TempFastq:
		if LineNumber_cats % 4 == 0:
#			Line = Line.strip('\n')			loop originally used the input fasta to do this; don't need this line if using a list
			Length = len(Line)
			Outputstring.append(Length)	
#			print(Line)
		LineNumber_cats +=1

#print(Outputstring)
#print(FileCount)

#	Set new line number variables and new empty list

LineNumber2 = 1
LineNumber4 = 1
Quality_removed = []

#	Loop that deletes the quality score line and saves the rest of the lines to Quality_removed list
###	Interesting problem/solution deleting the quality line	###

while LineNumber2 <= FileCount:
	for Line in TempFastq:
		if LineNumber2 % 4 == 0:
#			Line = Line.strip('\n')
			del Line # remove line code
#			print(Line)
		else:
#			Line = Line.strip('\n')
			Quality_removed.append(Line)			
		LineNumber2 += 1
		
#print(Quality_removed)

#	Set new empty list

Plus_removed = []

#	Loop that deletes the plus sign line and saves the rest of the lines to Plus_removed list

for Line in Quality_removed:
	if LineNumber4 % 3 == 0:
		del Line
	else:
		Plus_removed.append(Line)
	LineNumber4 += 1
	
#print(len(Plus_removed))

#	Set new line number variables and new empty list
###	Interesting problem/solution using AlsoCount	###

LineCounter_compare = 1
AlsoCount = 0
NewLine = []

#print(Plus_removed)

#	Loop that takes every DNA line in the Plus_removed list, checks the length against
#	the corresponding length in the Outputstring list, and removes the trailing base pairs
#	if the list lengths do not correspond
#	It adds the DNA ID line and the new DNA base pair line to a list: NewLine

#	I kept some print statements in the final version so there is peace of mind when the script is run

for Line in Plus_removed:
	if LineCounter_compare % 2 == 0:
#		print(Line)
		AlsoCount += 1
		DNA_match = Outputstring
#		print(Line)
#		Line = Line.strip('\n')
		if len(Line) == DNA_match[AlsoCount-1]:
			print("Trimming Sequences...")
		else:
			Line[:DNA_match[AlsoCount-1]]
			print("Old line length:", (len(Line)))
			print("New Line length:", (len(Line[:DNA_match[AlsoCount-1]])))

			NewLine.append(Line)
#		Plus_removed1 = str(Plus_removed)
	else:
		NewLine.append(Line)
	LineCounter_compare += 1

NewLine_string = str(NewLine)
#OutFile.write(NewLine_string)		Outfile.write writes the list as a single line to a file. BAD.

#	Loop that I googled adds each list element to a single line in a text file

with open(OutFileName, mode="w") as outfile:
    for s in NewLine:
        outfile.write("%s\n" % s)

