# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:46:35 2023

@author: RobertGatt
"""

# 4. (Optional) In Python the in comparison operator can be used to test if a
# character is contained in a string. So "a" in "spam" gives True, whereas
# "i" in "team" gives False.
# In the game Fizz Buzz you count out loud, but when a number is reached
# that is divisible by five, or contains the number five, you say ‘fizz’ whereas if a
# number is reached that is divisible by seven or contains the number seven you
# say ‘buzz’. If both of the conditions are met you say ‘fizz buzz’. For instance,
# counting in this way begins as follows.
# 1, 2, 3, 4, fizz, 6, buzz, 8, 9, fizz, 11, . . .
# Write a program which counts upwards from one to a specified number, using
# the rules of Fizz Buzz.

userNumber = int(input("Enter the maximum number to count"))

for index in range (1, userNumber + 1):
    if(index % 3 == 0 and index % 5 == 0):
        print("!fizz buzz!")
    elif(index % 3 == 0 or ("3" in str(userNumber-1))):
        print("fizz")
    elif(index % 5 == 0  or ("5" in str(userNumber-1))):
        print("buzz")
    else:
        print(index)