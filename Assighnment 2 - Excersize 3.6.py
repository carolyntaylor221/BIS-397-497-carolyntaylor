#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:52:30 2020

@author: carolyntaylor
"""

question1= input('What is your problem? ')
question2= input('Have you had this problem before (yes or no)? ')
if question2 == 'yes':
    print('Well, you have it again.')
elif question2 == 'no':
    print('Well, you have it now.')

# This conversation would not convince the user that the entity has intelligent
# behavior because it follows the same sequence of questions and answers for 
# every user. The system is not able to modify its assistance based on the 
# users unique case. 
    