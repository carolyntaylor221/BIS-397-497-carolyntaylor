#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:05:45 2020

@author: carolyntaylor
"""

sentence = ('A trial sentence for question six'
            'Another trial sentence for question six assighnment three')

word_counts = {}

for x in sentence.split():
    if x in word_counts: 
        word_counts[x] += 1  
    else:
        word_counts[x] = 1  

print(f'{"word":<12}count')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')
