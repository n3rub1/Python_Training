# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 08:22:52 2023

@author: RobertGatt-TDF
"""

n = int(input("Enter your n: "))
index = 1
result = 0

while(n >= 1):
    result = result + (1/n**2)
    n = n - 1

print(result)