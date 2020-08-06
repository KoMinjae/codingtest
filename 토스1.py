# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(nums):
    if nums[-1] == "1":
        return False
    for i in range(len(nums)-1):
        if nums[i]=="1":
            if nums[i+1]=="1":
                return False
        if nums[i]=="2":
            continue
    return True

nums = input()
solution(nums)