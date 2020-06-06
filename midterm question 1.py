#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:34:12 2020

@author: carolyntaylor
"""


## dice can be rolleed up to three time in a turn
# program one turn with three dice rolls
# virtually roll five six sided dies
## print results like 1 2 3 4 5
## user input which dice they would like to roll again using -99 to indicate 
#they are done
## choose dice based on position (index)

## re roll chossen dice
# choose again
# final dice displayed

import random


def roll_dice():
    """Roll five dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    die3 = random.randrange(1, 7)
    die4 = random.randrange(1,7)
    die5 = random.randrange(1,7)
    return (die1, die2, die3, die4, die5)

def display_dice(dice):
    """Display one roll of five dice."""
    die1, die2, die3, die4, die5 = dice 
    print(die1, die2, die3, die4, die5)
    
die_values = roll_dice()
display_dice(die_values)

dielist = list(die_values)

def roll_again(list):
    """select position of die to roll again, -99 to end"""
    while x != -99:
        dielist[x-1] = random.randrange(1,7)
        x = int(input('Enter position of die to roll again: '))
    return (die1, die2, die3, die4, die5)


die_values = roll_dice()
display_dice(die_values)

dielist = list(die_values)

x = int(input('Enter position of die to roll again: '))
roll_again(dielist)
        
        
roll_again(dielist)

for i in range(2):
    

roll_again()
        
    indexpositions = int
    input(dielist.index
    

    

    


