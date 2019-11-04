#! /usr/bin/env python3

# This takes a fasta file and shortens the information line to just the species name and sequence ID

'''
Pseudocode:
#import regex package
import re

#Open file for reading
InFileName = "regex.practice1.fasta"
InFile = open(InFileName, 'r')

#Set up regex and find the thing
Find = '(>\S) {'
Result = re.search(Find, InFile)
Replace = "Homo sapiens: \1"
NewString = re.sub(Find, Replace, InFileName)

#Write final string to outfile
OutFileName = "regex.practice1_out.fasta"
OutFile = open(OutFileName, 'w')
OutFile.write(NewString)
InFile.close()


'''


import re

InFileName = "regex.practice1.fasta"
OutFileName = "regex.practice1_out.fasta"

InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w')


LineNumber = 0

for Line in InFile:
	if LineNumber >= 0:
		Line = Line.strip('\n') #"strip" takes things out of lines
		ElementList = Line.split('\s')
#		print(ElementList[0])
#				search pattern
		SearchStr = '^>(\S+) {.+}'
#the pattern first, and then the thing you're searching in:
		Result = re.search(SearchStr, ElementList[0])
#		print(Result.groups())
		Replace = r">Homo sapiens: \1 "
		OutputString = re.sub(SearchStr, Replace, ElementList[0])
#		print(OutputString)
		OutFile.write(OutputString + "\n")
		LineNumber = LineNumber + 1



InFile.close()