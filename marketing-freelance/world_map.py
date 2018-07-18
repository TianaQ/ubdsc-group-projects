#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:00:02 2018

@author: tatianakurilo
"""

import plotly
plotly.offline.init_notebook_mode(connected=True)

import pandas as pd

COUNTRY_CODES_DF = pd.read_csv('country_codes.csv')

def make_world_map_html(country_codes, country_data, file_name, map_title, legend_title, tick_pref = ''):
    data_text = []
    for code in country_codes:
        data_text.append(COUNTRY_CODES_DF[COUNTRY_CODES_DF['ISO'] == code]['Country Name'].to_string(index=False))
    
    data = [ dict(
            type = 'choropleth',
            locations = country_codes,
            z = country_data,
            text = data_text,
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
                tickprefix = tick_pref,
                title = legend_title),
          ) ]
    
    layout = dict(
        title = map_title,
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )
    
    fig = dict( data=data, layout=layout )
    plotly.offline.plot(fig, validate=False, filename=file_name + '.html')
    
