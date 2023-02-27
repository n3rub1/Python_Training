# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:13:01 2023

@author: RobertGatt-TDF
"""

# x = [[1,2,3], [4,5,6]]
# print(x[0][0])

import matplotlib.pyplot as plt
import math
import numpy as np

def simplePlot():
    x_values = [0,1,2,3,4]
    y_values = [0,4,3,4,3.5]
    y_values_2 = [2,0,-1,4,2.5]
    
    plt.plot(x_values, y_values, color="red", marker="o", linestyle="--")
    plt.plot(x_values, y_values_2)
    
    plt.show()

# simplePlot()

def sinplot(xMin, intervals):
    x_min = xMin
    x_max = 2 * math.pi
    NO_OF_INTERVALS = intervals
        
    x_values = []
    y_values = []
        
    for i in range(NO_OF_INTERVALS + 1):
        x = x_min + i * (x_max - x_min)/ NO_OF_INTERVALS
        x_values.append(x)
        y_values.append(math.sin(x))
            
    plt.plot(x_values, y_values)
    
# sinplot(0, 20)

def testingNumpy():
    array_1 = np.array([1.1,2.2,3.3])
    print(array_1)
    
    list_1 = [1.1,2.2,3.3]
    print(list_1)
    
    print(list_1 + list_1)
    print(list_1 * 5)
    
    print(array_1 + array_1)
    print(array_1 * 5)
    
    #generate linearly
    x=np.linspace(-50,50, 10000)
    print(x)
    
    #this way it goes through the array and caluclate on each one
    # y=np.exp(-x/10)*np.sin(x*2)
    # y_1 = np.exp(-x/10)
    # y_2 = np.sin(x*2)
    
    # plt.plot(x,y)
    # plt.plot(x,y_1)
    # plt.plot(x,y_2)
    
    # y= abs(np.exp(-x/5)*np.sin(x))
    # plt.loglog(x,y)
    # plt.show()
    
    # theta = np.linspace(0, 10*np.pi, 1000)
    # plt.axes().set_aspect("equal")
    # # plt.plot(np.cos(theta), np.sin(theta))
    # # plt.plot(2 * np.cos(theta), 2 * np.sin(theta))
    # plt.plot(theta * np.cos(theta), theta * np.sin(theta))
    # plt.show()
    
    theta = np.linspace(0, 2*np.pi, 200)
    for k in range(2,7):
        plt.axes().set_aspect("equal")
        plt.plot(1.5 * np.cos(theta) - np.cos(k * theta), 1.5 * np.sin(theta) - np.sin(k.theta))

    plt.show()

testingNumpy()




