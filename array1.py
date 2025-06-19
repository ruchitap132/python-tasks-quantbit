# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 18:24:32 2025

@author: Aniket
"""
#find missing values in an array.
def find_missing_number(arr: list) ->int:
    n=len(arr)
    total=(n*(n+1))/2
    return total-sum(arr)
arr=[3,0,1]
print(find_missing_number(arr))
    
    
