# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 18:31:52 2025

@author: Aniket
"""

def find_kth_largest(nums: list, k:int)-> int:
    nums.sort(reverse=True)
    return nums[k-1]
nums=[3,2,1,5,6,4]
k=2
print(find_kth_largest(nums,k))