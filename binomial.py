#!/usr/bin/env python
# coding: utf-8

# In[93]:


import matplotlib.pyplot as plt
import numpy as np

def prob(n, p, N):
    return (np.math.factorial(N) / (np.math.factorial(n) * np.math.factorial(N - n))) * ((p) ** n) * ((1 - p) ** (N - n))
prob(7, 0.5, 10)


# In[94]:


def infoMeasure(n, p, N):
    return -np.log2(prob(n, p, N))
infoMeasure(5, 0.5, 10)


# In[95]:


def sumProb(N, p):
    """
    Hàm cho ra kết quả 
    sumProb(5, 0.5) = 0.96875
    sumProb(10, 0.5) = 0.9990234375
    sumProb(20, 0.5) = 0.9999990463256836
    Gần tiến tới 1
    vậy hàm có thể kiểm chứng tổng xác suất phân bố binomial bằng 1
    """
    sumP = 0.0
    for i in range(0, N):
        sumP += prob(i, p, N)
    return sumP
sumProb(5, 0.5)


# In[96]:


def approxEntropy(N, p):
    """
    Hàm tính xấp xỉ entropy của nguồn tin binomial
    """
    h = 0
    for i in range(0, N):
        h += prob(i, p, N) * np.log2(prob(i, p, N))
    return -h

approxEntropy(10, 0.5)

