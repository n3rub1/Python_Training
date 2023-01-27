# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:15:56 2023

"""

#input and if else statements
# x= int(input("Check if number is even or odd: "))
# if(x % 2 == 1):
#     print("number is odd")
# elif(x == 0):
#     print("invalid number")
# else:
#     print("number is even")
    
#types
# y = "hello"
# print(type(y))
# print(len(y))

# x = 2
# print(type(x))
# x = str(x)
# print(type(x))

# x = print(len(str(2**100)))
# y = "Hello"
# print (y[-1])   #-1 is the last character,0 is the first character
# print(y[2:4])   #this is ll
# print(y[:3])    #this is Hel
# print(y[2:])    #this is llo

# #you can also do the slice and any operation directly on a string
# print("Robert"[0])

#for loop
# y = "hello world"

# for x in range(2,9): #x is the index, and goes from 2 -- 8 (9-1)
#     print(y[x], end=":")
    
for n in range(1,10):
    if(n == 1):
        for k in range(0,10):
            if(k==0):
                print("* |", end="\t")
            else:
                print (k, end="\t")
                if(k==9):
                    print()
                    print("-"*40)
    for i in range(1,10):
        if(i==1):
            print(i*n, "|", end=" ")
        print(i*n, end="\t")
    print()