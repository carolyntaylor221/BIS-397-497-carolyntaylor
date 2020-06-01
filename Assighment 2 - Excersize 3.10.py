#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:12:14 2020

@author: carolyntaylor
"""


p = 1000
r = .07
for n in range(1,31):
    a = p*(1+r)**n
    print (f'Amount after {n:>2} years: {a:>10.2f}')
    
