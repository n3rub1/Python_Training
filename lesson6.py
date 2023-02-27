# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:07:49 2023

@author: RobertGatt-TDF
"""

with open("characters.txt", mode="w") as out_file:
    out_file.write("Some characters:\n\n")
    for order in range(65, 128):
        out_file.write(chr(order))
        if order % 16 == 0:
            out_file.write("\n")
            

infile_name = "C:/Users/RobertGatt-TDF/Desktop/Characters.txt"            

with open(infile_name, mode="r") as infile:
    text = infile.read()
    for character in text:
        print(character, end=(""))


my_dict = {"name": "Robert", "surname": "Gatt"}
print()
print(my_dict["name"])

my_dict["address"] = "Xghajra"
print(my_dict)

my_dict.pop("name")
print(my_dict)


x = my_dict.popitem()
print(x)

number_dict = {1: 2, 2: 4, 3: 8, 4: 16, 6:64, 5: 32}

for i in number_dict:
    print(i)  #this is the key
    print(number_dict[i])  #this is the value

print(len(number_dict))
print(all(number_dict))
print(sorted(number_dict))


people = {1: {"name": "Robert", "surname": "Gatt"}, 
          2:{"name": "Claudia", "surname": "Villani"}}

print(people[1]["name"])