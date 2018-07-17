#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:52:37 2018

@author: tatianakurilo
"""
import plotly
plotly.offline.init_notebook_mode(connected=True)

import pandas as pd

freelancers = pd.read_csv('freelancers.csv')

COUNTRY_CODES_LIST = list(freelancers['iso_code'].unique())

country_pph = []

for CODE in COUNTRY_CODES_LIST:
    country_subset = freelancers[freelancers['iso_code'] == CODE]
    if country_subset.shape[0] > 5:
        country_pph_mean = country_subset['dollars_ph'].mean()
        country_pph.append((CODE, country_pph_mean))
    else:
        country_pph.append((CODE, 0))

country_pph_df = pd.DataFrame(country_pph, columns=['code', 'mean_price_ph'])
 
data = [ dict(
        type = 'choropleth',
        locations = country_pph_df['code'],
        z = country_pph_df['mean_price_ph'],
        text = country_pph_df['code'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '$',
            title = 'US$'),
      ) ]

layout = dict(
    title = 'Price Per Hour by Country (6+ freelancers in country)',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
plotly.offline.plot(fig, validate=False, filename='mean_pph-world-map.html')