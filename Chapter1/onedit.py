#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:16:42 2020

@author: dikshasharma
"""
flag=0
def oneditaway(str1,str2):
    if len(str1)==len(str2):
        return oneplaceedit(str1,str2)
    elif len(str1)-1==len(str2):
        return oneplaceinsert(str2,str1)
    elif len(str1)+1== len(str2):
        return oneplaceinsert(str1,str2)
    return False
def oneplaceedit(str1,str2):
    for c,d in zip(str1,str2):
        if c==d:
            flag=0
        else:
            flag=1
    return True 
            
    
    
    
def oneplaceinsert(str1,str2):
    i=0
    j=0
    insert1=False
    while i<len(str1) and j<len(str2):
        if str1[i]!=str2[j]:
            if insert1:
                return False
            
            insert1=True
            j+=1
        else:
            i+=1
            j+=1
    return True
            
        
      
print(oneditaway('pae','bale'))  
    
    