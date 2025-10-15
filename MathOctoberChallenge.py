#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 13:45:43 2025

@author: 24AkshatM
"""

import matplotlib.pyplot as plt
base = 7
exp  = (1/5)
final = [base**exp]
iList = [0]
for i in range(1, 50):
    if i%2!=0:
        exp+=1
    else:
        exp=exp*(1/5)
    final.append(base**exp)
    iList.append(i)
print(final)
plt.plot(iList, final)
plt.show