#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:36:16 2020

@author: carolyntaylor
"""


import random
import numpy as np

value = []
results1 = []
results2 = []
aresults1 = []
aresults2 = []
answer1 = ""
answer2 = ""

for x in range (0,7):
    value.append(10**x)
    store = %timeit -o rolls_list = [random.randrange(1,7) for i in range(0,10**x)]
    results1.append(str(store))
    store2 = %timeit -o rolls_list2 = np.random.randint(1,7, 10**x)
    results2.append(str(store2))


for x in range(0, len(results1)):
    answer1 = ""
    for y in range(0, len(results1[x])):
        if results1[x][y] != 'p':
            answer1 += results1[x][y]
        else:
            break
    aresults1.append(answer1)
    
    answer2 = ""
    for z in range(0, len(results2[x])):
        if results2[x][z] != 'p':
            answer2 += results2[x][z]
        else:
            break
        aresults2.append(answer2)
    
print()
print("%16s %-26s %-30s" %("Number of values", "List of execution times", 
                           "Array average execution time"))
for x in range(0, len(aresults1)):
    print("%-16i %-26s %-30s" % (value[x], aresults1[x], aresults2[x]))
    