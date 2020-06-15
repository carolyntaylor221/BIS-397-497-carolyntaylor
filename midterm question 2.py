#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:34:32 2020

@author: carolyntaylor
"""
# Score: 23/25
# Forgot to import random


import random # Added by TAA
import statistics

def descriptive(list):
    """find mean, median, sample and population standard deviation"""
    return print('mean is:',statistics.mean(list), 'median is:',
                 statistics.median(list), 'sample standard deviation is:',
                 statistics.stdev(list), 'population standard deviation is:',
                 statistics.pstdev(list))

list1 = []

for i in range(10):
    i = random.randrange(0,10) 
    list1.append(i)
    
descriptive(list1)