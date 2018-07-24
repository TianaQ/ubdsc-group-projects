#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:42:59 2018

@author: tatianakurilo
"""
import pandas as pd, numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('csv/skills_pph_count.csv')


fig, ax = plt.subplots(figsize=(15,15))
plt.pcolor(df, cmap=plt.cm.Spectral)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()
# 
# import seaborn as sns
# 
# fig, ax = plt.subplots(figsize=(20,15))
# sns.heatmap(df, cmap='RdYlGn_r', linewidths=0.5, ax=ax, annot = True, center = 50)
# =============================================================================


def add_price_groups(price):
    start = (price // 10) * 10
    end = start + 9
    return "${}-{}".format(str(start), str(end))
     
labels = ['price'] + list(df.columns)

df.reset_index(inplace = True)

df.columns = labels 
df['price_group'] = df['price'].apply(add_price_groups)

df.to_csv('csv/skills_pph_with_grops.csv')