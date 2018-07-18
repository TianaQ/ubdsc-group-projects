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

freelancers_by_country = []

for CODE in COUNTRY_CODES_LIST:
    country_subset = freelancers[freelancers['iso_code'] == CODE]
    num_freelancers = country_subset.shape[0]
    freelancers_by_country.append((CODE, num_freelancers))

freelancers_by_country_df = pd.DataFrame(freelancers_by_country, columns=['code', 'num_freelancers'])


world_map.make_world_map_html(freelancers_by_country_df['code'], 
                              freelancers_by_country_df['num_freelancers'],
                              file_name = 'num_freelancers-world-map',
                              map_title = 'Number of Freelancers by Country', 
                              legend_title = 'People', 
                              tick_pref = '')
