# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 08:55:04 2023

@author: RobertGatt-TDF
"""

# 3. Write a program which defines the factorial() function as above and a new
# function binomial() which takes two parameters n and k and returns the
# binomial coefficient (nk)
# . The program asks the user for a number and prints
# out that many rows of Pascal’s triangle. So if ‘5’ were entered, you would get
# something like the following.
#              1
#          1      1
#    1             2           1
#   1        3        3           1
# 1     4       6           4           1


#Example 1
# def function_1(s):
#     """First mystery function."""
#     for i in range(len(s)):
#         if i % 3 == 0:
#             print(s[i].upper(), end="")
#         else:
#             print(s[i].lower(), end="")
#         print("!")
    
        
# function_1("elephantine")


# def function_2(s):
#     """Second mystery function."""
#     v = 0
#     for i in range(len(s)):
#         if s[i] in "aeiou":
#             v = v + 1
#     return v
# print(function_2("Spain") * function_2("oceanic"))


def factorial(n):
    """Factorial function"""
    value = 1
    
    
    if(n == 0):
        return value
    
    while(n > 0):
        value = value * n
        n = n - 1
        factorial(n)
    
    return value
    
x = factorial(5) #120
print("x" , x)

def binomial(n, k):
    """Binomial Function n!/(k!(n-k)!)"""
    numerator = factorial(n)
    denominatorPartOne = factorial(k)
    denominatorPartTwo = factorial(n-k)
    denominator = denominatorPartOne * denominatorPartTwo
    value = numerator / denominator
    
    return value

y = binomial(15,5)  #252
print("y" , y)   
        
        

def pascalTriangle(n):
    """Pascals Triangle"""
    startIndex = 0
    startNumber = 2**startIndex  #calculate the binary starting at 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    