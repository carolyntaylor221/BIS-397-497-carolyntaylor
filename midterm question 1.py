#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:34:12 2020

@author: carolyntaylor
"""

# Grade: 20/25
    
# Comments: 
# 1. Think it would have worked fine if you had had time

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

##I ran out of time before I was able to finish coding a re roll. Once that 
# is coded i was going to use a for statement to run the reroll 
# twice. Every time you reroll you would update the dielist. Then when all 
# reroll are over you print the final dice. 
        
    

    

    


