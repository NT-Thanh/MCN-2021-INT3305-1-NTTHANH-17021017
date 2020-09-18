#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np

def prob(n, p):
    return ((1-p)**(n-1))*p
# prob(3, 0.25)


# In[15]:


def infoMeasure(n, p):
    return -np.log2(prob(n, p))
# infoMeasure(2,0.25)


# In[10]:


def sumProb(N, p):
    """
    Hàm cho ra kết quả 
    sumProb(5, 0.5) = 0.9375
    sumProb(10, 0.5) = 0.998046875
    sumProb(20, 0.5) = 0.9999980926513672
    Gần tiến tới 1
    vậy hàm có thể kiểm chứng tổng xác suất phân bố geometric bằng 1
    """
    sumP = 0.0
    for i in range(1, N):
        sumP += prob(i, p)
    return sumP
# sumProb(20, 0.5)


# In[13]:


def approxEntropy(N, p):
    """
    Hàm cho ra kết quả 
    sumProb(5, 0.5) = 1.625
    sumProb(10, 0.5) = 1.978515625
    sumProb(20, 0.5) = 1.999959945678711
    Gần tiến tới 2
    vậy hàm tính xấp xỉ entropy của nguồn tin geometric
    """
    h = 0
    for i in range(1, N):
        h += prob(i, p) * np.log2(prob(i, p))
    return -h
#print(approxEntropy(20,0.5))


# %%
