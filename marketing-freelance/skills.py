#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:59:01 2018

@author: tatianakurilo
"""

import pandas as pd, numpy as np

skills = pd.read_csv('skills.csv', sep='\t')

# =============================================================================
# RangeIndex: 1710 entries, 0 to 1709
# Data columns (total 4 columns):
# skill        1710 non-null object
# frequency    1710 non-null int64
# mean         1710 non-null float64
# std          1268 non-null float64
# dtypes: float64(2), int64(1), object(1)
# =============================================================================

skills = skills.sort_values('frequency', ascending=False)

#print(skills.head(30))

### Explore possible skill groups ###
group = '3d' # Try to change group 
skills_in_group = []
price_in_group = []
for index, row in skills.iterrows():
  if group in row['skill']:
    skills_in_group.append((row['skill'], row['frequency'], row['mean']))
    price_in_group.append(row['mean'])

print(group, round(np.mean(price_in_group), 2))
print()
print("Skills in group:")
skills_in_group.sort(key = lambda x: x[1], reverse=True) 
for x in skills_in_group:
  print("{}, {}, {}".format(x[0], x[1], round(x[2], 2)))