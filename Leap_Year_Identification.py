#!/usr/bin/env python
# coding: utf-8

# In[107]:


def is_leap(year):
    leap = False
    if year%4==0:
        leap = True
        if(year%100==0):
            leap = False
            if(year%100==0 and year%400==0):
                leap = True
    else:
        return leap
    return leap

