#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:33:54 2018

@author: tatianakurilo
"""
import pandas as pd

COUNTRY_CODES_DF = pd.read_csv('country_codes.csv')
country_codes = COUNTRY_CODES_DF['ISO'].tolist()

data_text = []
for code in country_codes:
    data_text.append(COUNTRY_CODES_DF[COUNTRY_CODES_DF['ISO'] == code]['Country Name'].to_string(index=False))

print(data_text)