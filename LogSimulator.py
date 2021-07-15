#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on 06/03/2021

@author: Sergei Akopov
"""

import csv
import time
import sys

sourceDataFile = "OnlineRetail.csv"
placeholder = "LastLine.txt"

def GetLineCount():
    with open(sourceDataFile) as srcFile:
        for lineCnt, l in enumerate(srcFile):
            pass
    return lineCnt

def GenerateLog(startLine, numLinesToGenerate):
   # destLogFile = time.strftime("/var/log/varietygifts/%Y%m%d-%H%M%S.log")
    destLogFile = time.strftime("var\\log\\varietygifts\\%Y%m%d-%H%M%S.log")
    with open(sourceDataFile, 'r') as sourceCsvfile:
        with open(destLogFile, 'w') as dstCsvfile:
            reader = csv.reader(sourceCsvfile)
            writer = csv.writer(dstCsvfile)
            next (reader) #ignore header
            inputRow = 0
            numOfLinesWritten = 0
            for row in reader:
                inputRow += 1
                if (inputRow > startLine):
                    writer.writerow(row)
                    numOfLinesWritten += 1
                    if (numOfLinesWritten >= numLinesToGenerate):
                        break
            return numOfLinesWritten
        
    
numOfLinesToGenerate = 100
startLine = 0            
if (len(sys.argv) > 1):
    numOfLinesToGenerate = int(sys.argv[1])
    
try:
    with open(placeholder, 'r') as f:
        for line in f:
             startLine = int(line)
except IOError:
    startLine = 0

print("Writing " + str(numOfLinesToGenerate) + " lines starting at line " + str(startLine) + "\n")

totalLinesWritten = 0
linesInFile = GetLineCount()

while (totalLinesWritten < numOfLinesToGenerate):
    linesWritten = GenerateLog(startLine, numOfLinesToGenerate - totalLinesWritten)
    totalLinesWritten += linesWritten
    startLine += linesWritten
    if (startLine >= linesInFile):
        startLine = 0
        
print("Wrote " + str(totalLinesWritten) + " lines.\n")
    
with open(placeholder, 'w') as f:
    f.write(str(startLine))