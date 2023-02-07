# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 07:38:49 2023

@author: RobertGatt-TDF
"""

# This Sieve of Eratosthenes is a method of giving a list of all the prime numbers
# up to a given number. You start by writing out all the numbers between 2 and
# n. You cross out all of the multiples of 2 (but not 2 itself). Then you cross out
# all of the multiples of 3 (but not 3 itself). And you carry on like that until you
# removed multiples of all numbers up to √
# n. What is left not crossed out is
# precisely the set of prime numbers up to n.
# Try this by hand with n  25.
# Write a program which implements this algorithm. Use it to list all the prime
# numbers up to 10, 000, and to state how many there are.


n = 10000
numbers = list(range(2, n+1))
index = 0
squareRootOfN = n**(1/2)
squareRootOfNList = list(range(2, int(squareRootOfN) + 1))

for numberOfSquare in squareRootOfNList:
    for number in numbers:
        if(number % numberOfSquare == 0 and number != numberOfSquare):
            numbers.remove(numbers[index])
        
        index = index + 1
    index = 0
        

print(numbers)
print("\nThere were",len(numbers), "prime number up to",n)