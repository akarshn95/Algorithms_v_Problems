#!/usr/bin/env python
# coding: utf-8

# In[8]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return -1
    
    big=ints[0]
    small=ints[0]
    
    for i in ints:
        if i<small:
            small=i
        elif i>big:
            big=i
    
    return (small,big)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

