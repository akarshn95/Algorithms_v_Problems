#!/usr/bin/env python
# coding: utf-8

# In[7]:


def sort_012(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero=0
        two=len(nums)-1
        
        i=0
        while i<=two:
            if nums[i]==0:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero+=1
            elif nums[i]==2:
                nums[i],nums[two]=nums[two],nums[i]
                two-=1
                # to perform a check to the swapped element
                i-=1
            i+=1
        return nums


# In[8]:


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

