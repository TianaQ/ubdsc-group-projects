#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:52:37 2018

@author: tatianakurilo
"""
import world_map

import pandas as pd

freelancers = pd.read_csv('freelancers.csv')

COUNTRY_CODES_LIST = list(freelancers['iso_code'].unique())


## Average Price Per Hour by Country (5+ freelancers in country
country_pph = []

for CODE in COUNTRY_CODES_LIST:
    country_subset = freelancers[freelancers['iso_code'] == CODE]
    if country_subset.shape[0] >= 5:
        country_pph_mean = country_subset['dollars_ph'].mean()
        country_pph.append((CODE, country_pph_mean))
    else:
        country_pph.append((CODE, 0))

country_pph_df = pd.DataFrame(country_pph, columns=['code', 'mean_price_ph'])


world_map.make_world_map_html(country_pph_df['code'], 
                              country_pph_df['mean_price_ph'],
                              'mean_pph-world-map',
                              'Average Price Per Hour by Country (5+ freelancers in country)', 
                              'US$', 
                              tick_pref = '$') 


## Median Price Per Hour by Country (5+ freelancers in country) 
country_median_pph = []

for CODE in COUNTRY_CODES_LIST:
    country_subset = freelancers[freelancers['iso_code'] == CODE]
    if country_subset.shape[0] >= 5:
        country_pph_median = country_subset['dollars_ph'].median()
        country_median_pph.append((CODE, country_pph_median))
    else:
        country_median_pph.append((CODE, 0))

country_pph_median_df = pd.DataFrame(country_median_pph, columns=['code', 'median_price_ph'])


world_map.make_world_map_html(country_pph_median_df['code'], 
                              country_pph_median_df['median_price_ph'],
                              'median_pph-world-map',
                              'Median Price Per Hour by Country (5+ freelancers in country)', 
                              'US$', 
                              tick_pref = '$') 
