#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:02:31 2020

@author: carolyntaylor
"""


def display_table(twoD_list, column_width):
   
    indent = len(str(len(twoD_list)))
    print(f'{"":{indent}}', end='')

    for col in range(len(twoD_list[0])):
        print(f'{col:>{column_width}}', end='')

    print()

    for i, row in enumerate(twoD_list):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{column_width}}', end='')

        print()
        
list1 = [list(range(10,20)), list(range(20,30))]

display_table(list1, 2)

