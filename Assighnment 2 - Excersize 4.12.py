#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:16:50 2020

@author: carolyntaylor
"""

import random

race_end = 70

def tortoise_position(tortoise):
    """tortoise new position next second"""
    tortoise_i = random.randrange(1,11)
    
    
    if 1 <= tortoise_i <= 5:
        tortoise += 3
    elif 6 <= tortoise_i <= 7 :
        tortoise -= 6
    else:
        tortoise += 1


    if tortoise < 1:
        tortoise = 1
    elif tortoise > race_end:
        tortoise = race_end
    
    return tortoise 

def hare_position(hare):
    """Hare new position next second"""
    hare_i = random.randrange(1,11)
    
    if 1 <= hare_i <= 2:
        hare += 0
    elif 3 <= hare_i <= 4:
        hare += 9
    elif hare_i == 5:
        hare -= 12
    elif 6 <= hare_i <= 8:
        hare += 1
    elif hare_i > 8:
        hare -= 2
        
    if hare < 1:
        hare = 1
    elif hare > race_end:
        hare = race_end
        
    return hare 

def print_positions(tortoise, hare):
    """print position of tortoise and hare on line for 70 squares. Print H/
    for hare position and T for tortoise position."""
    for count in range(1, race_end + 1):
        if count == tortoise and count == hare:
            print('OUCH!!!', end='')
        elif count == hare:
            print('H', end='')
        elif count == tortoise:
            print('T', end='')
        else:
            print(' ', end='')
            
    print()
            
tortoise = 1 
hare = 1
timer = 0 

print('BANG !!!!!')
print("AND THEY'RE OFF !!!!!")

while tortoise < race_end and hare < race_end:
    tortoise = tortoise_position(tortoise)
    hare = hare_position(hare)
    print_positions(tortoise, hare)
    timer += 1
    
if tortoise > hare:
    print('TORTOISE WINS!!! YAY!!!')
elif hare > tortoise :
    print('Hare wins. Yuch')
else:
    print("It's a tie.")
    
print(f'TIME ELAPSED = {timer} seconds')
    
      
