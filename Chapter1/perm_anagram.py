#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:41:47 2020

@author: dikshasharma
"""
def permutations(str1,str2):
    if len(str1)!=len(str2):
        return False
    if  sorted(str1)==sorted(str2):
           return True      
    else:
           return False

print(permutations('geeksforr','orfgeeks'))
    