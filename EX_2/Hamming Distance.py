# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:27:06 2023

@author: RobertGatt
"""

# 3. The Hamming distance is a way of measuring how similar two strings are.
# It is used in DNA research amongst other things. Given two strings of equal
# length it counts how many places the strings differ. For instance the Hamming
# distance between "string" and "strong" is 1; whereas the distance between
# "string" and "gnirts" is 6.
# Write a program which inputs two strings and outputs their Hamming distance.
# You can assume that the two strings are the same length.
# If you are feeling adventurous, modify your program so that it can cope with
# strings of different lengths.

#Not adventurous
firstString = str(input("Enter first string"))
secondString = str(input("Enter second string"))
numberOfDifferences = 0

for x in range(0, len(firstString)):
    if(firstString[x] != secondString[x]):
        numberOfDifferences = numberOfDifferences + 1

print (numberOfDifferences)
    
#adventurous
firstString = str(input("Enter first string"))
secondString = str(input("Enter second string"))
numberOfDifferences = 0
stringTest = ""

if(len(firstString) <= len(secondString)):
    stringTest = firstString
    numberOfDifferences = numberOfDifferences + (len(secondString) - len(firstString))
    
else:
    stringTest = secondString
    numberOfDifferences = numberOfDifferences + (len(firstString) - len(secondString))


for x in range(0, len(stringTest)):
    if(firstString[x] != secondString[x]):
        numberOfDifferences = numberOfDifferences + 1

print (numberOfDifferences)