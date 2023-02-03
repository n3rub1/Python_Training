# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:41:20 2023

"""

#lists and for loop in lists
# print(list(range(1,4,1)))
# print(list(range(2,9,2)))
# print(list(range(-3, -19, -5)))

# DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for index in DAYS_OF_WEEK:
#     print ("The first letter of", index, "is" ,index[0])


# #functions
# def three_greetings():
#     """Say hello three times"""   #this is done to say what the function does
#     for i in range(3):
#         print("(", i,") Hello", sep="" )
# three_greetings()

# def many_greetings(n):
#     """say hello n number of times"""
#     for i in range(n):
#         print("(", i,") Hello", sep="" )

# many_greetings(10)

# def add_numbers(a,b):
#     return a + b

# addedNumbers = add_numbers(5,1)
# print(addedNumbers)

def string_to_vector(stringWithSpaces):
    """Takes an input of string of numbers and return a list of floats"""
    stringToList = stringWithSpaces.split()
    newList= []
    for index in stringToList:
        newList.append(float(index))
    return newList
    
    
x = "1 3 5 5.5 6.786"
y = string_to_vector(x)    

print(y)
    
