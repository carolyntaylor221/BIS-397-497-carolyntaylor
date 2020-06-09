#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:58:29 2020

@author: carolyntaylor
"""


alpha = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in alpha:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
           
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

panagram = 'The Quick Brown Fox Jumps Over The Lazy Dog'
summary = summarize_letters(panagram)

for char, count in summary:
    print(f'{char}: {count}')

correct = True

if len(summary) == len(alpha):
    for item in summary:
        if item[0] not in alpha:
            correct = False
            break  
else:
    correct = False

if correct:
    print(f'"{panagram}" contains all the letters in the alphabet')
else:
    print(f'"{panagram}" does not contain all the letters in the alphabet')
    
