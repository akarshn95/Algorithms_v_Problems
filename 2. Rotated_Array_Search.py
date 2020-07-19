#!/usr/bin/env python
# coding: utf-8

# In[14]:


def find_pivot(input_list):
    start=0
    end=len(input_list)-1
    
    while start<=end:
        mid=(start+end)//2
        if input_list[mid]>input_list[mid+1]:
            return mid+1
        if input_list[start]<input_list[mid]:
            start=mid+1
        else:
            end=mid-1
    

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start=0
    end=len(input_list)-1
    ans=-1
    
    pivot=find_pivot(input_list)
    if input_list[pivot]==number:
        return pivot
    if number<input_list[pivot]:
        return ans
    elif input_list[pivot]<number<input_list[end]:
        ans=binary_search(input_list,pivot,end,number)
    elif number>input_list[pivot] and number<=input_list[pivot-1]:
        ans=binary_search(input_list,start,pivot-1,number)
    return ans
    
def binary_search(input_list,start,end,num):
    
    while start<=end:
        mid=(start+end)//2
        if num==input_list[mid]:
            return mid
        if num>input_list[mid]:
            start=mid+1
        else:
            end=mid-1
    
    return -1
   
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

