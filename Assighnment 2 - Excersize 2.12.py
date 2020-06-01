#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:33:43 2020

@author: carolyntaylor
"""


p = 1000
r = .07
for n in [10, 20, 30]:
    a = p*(1+r)**n
    print ('The amount on deposit after', n, 'years is:', a)
        
        