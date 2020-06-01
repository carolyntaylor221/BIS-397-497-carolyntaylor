#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:19:49 2020

@author: carolyntaylor
"""

numberlist = []
length = len(numberlist)
for count in range(10):
    value = int(input('Enter a number: '))
    numberlist.append(value)
sortedlist = sorted(numberlist)
print('Second largest number is: ', sortedlist[length-2])
print('Largest number number is: ', max(numberlist))
    
