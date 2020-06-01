#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:47:33 2020

@author: carolyntaylor
"""


def fahrenheit(celsius):
    """Calculate the fahrenheit equivalent of a celsius temperature"""
    return (9/5)*celsius+32

print(f'Fahrenheit{"Celsius":>10}')

for celsius in range(101):
    print(f'{celsius:>10}{fahrenheit(celsius):>10.1f}')
    
    
