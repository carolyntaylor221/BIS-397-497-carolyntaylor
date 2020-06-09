#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:03:44 2020

@author: carolyntaylor
"""

import statistics as stats

import numpy as np

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, counts = np.unique(responses, return_counts=True)
values = list(values)
counts = list(counts)

print('Reponses:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')

print(f'Minumum: {values[counts.index(min(counts))]}')
print(f'Maximum: {values[counts.index(max(counts))]}')
print(f'Range: {min(counts)}-{max(counts)}')
print(f'Mean: {stats.mean(counts)}')
print(f'Median: {stats.mean(counts)}')
print(f'Mode: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')

