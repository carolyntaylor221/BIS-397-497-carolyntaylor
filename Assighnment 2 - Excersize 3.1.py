#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:42:41 2020

@author: carolyntaylor
"""


passes = 0

for students in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    while result != 1 and result != 2 :
        print('invalid input try again')
        result = int(input('Enter result (1=pass, 2=fail): '))


    if result == 1:
        passes = passes + 1
        
        
print('Passed:', passes)
print('failed:', 10-passes)

if passes > 8:
    print('Bonus to instructor')
    
    