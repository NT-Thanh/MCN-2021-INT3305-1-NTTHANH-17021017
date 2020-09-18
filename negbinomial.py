#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def prob(n, p, N, r):
    return (np.math.factorial(n) / (np.math.factorial(n - r + 1) * np.math.factorial(r - 1))) * ((p) ** r) * ((1 - p) ** (n - r))
    # return (np.math.factorial(n) / (np.math.factorial(n - r + 1) * np.math.factorial(r - 1))) * 1/(2**n)
prob(2, 0.5, 0, 2)


# In[2]:


def infoMeasure(n, p, N, r):
    return -np.log2(prob(n, p, N, r))
infoMeasure(5, 0.5, 10, 2)


# In[32]:


def sumProb(N, p, r):
    """
    Hàm cho ra kết quả 
    sumProb(7, 0.5, 7) = 0.20947265625
    sumProb(12, 0.5, 7) = 0.8329315185546875
    sumProb(50, 0.5, 7) = 0.9999999994323807
    Gần tiến tới 1
    vậy hàm có thể kiểm chứng tổng xác suất phân bố negbinomial bằng 1
    """
    sumP = 0.0
    for i in range(r - 1, N):
        sumP += prob(r + i, p, N, r)
    return sumP
sumProb(50, 0.5, 7)


# In[42]:


def approxEntropy(N, p, r):
    """
    Hàm cho ra kết quả 
    với p = 0.5
    approxEntropy(10, 0.5, 3) = 2.4955159217409095
    approxEntropy(50, 0.5, 3) = 2.6700174681491085
    approxEntropy(997, 0.5, 3) = 2.6700174681629694
    bị chặn ở xấp xỉ 2.6700174681629694
    vậy hàm tính xấp xỉ entropy của nguồn tin negbinomial
    """
    h = 0
    for i in range(r - 1, N):
        h += prob(r + i, p, N, r) * np.log2(prob(r + i, p, N, r))
    return -h
approxEntropy(10, 0.5, 3)

