# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:05:10 2023

@author: RobertGatt-TDF
"""

firstNumber = 0
secondNumber = 1
result = 0
index = 0

userInput = int(input("Enter a number: "))

while(index < userInput):
    firstNumber = secondNumber
    secondNumber = result
    result = firstNumber + secondNumber
    index += 1

print(result)