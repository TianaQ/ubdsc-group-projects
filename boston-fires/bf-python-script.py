#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 13:02:03 2018

@author: tatianakurilo
"""
import sys, os, pandas as pd

# SET PATH to the directory with csv files
try:
    dir_path = sys.argv[1] # 'data'
except:
    try:
        dir_path = input('Enter path to the data directory: ')
    except:
        raise Exception('No path provided')

if not os.path.exists(dir_path):
    raise FileNotFoundError

# list of column names, address information columns omitted
bf_col_names = ['Incident Number', 'Exposure Number', 'Alarm Date', 'Alarm Time', 
                 'Incident Type', 'Incident Description', 'Estimated Property Loss',
                 'Estimated Content Loss', 'District', 'City Section', 'Neighborhood', 
                 'Zip', 'Property Use', 'Property Description']


def read_csv_data(data_dir, col_names = False):
    """
    Reads csv files from the provided directory and returns a pandas dataframe of all files
    """
    
    # create an empty list to store dataframes of each file
    df_list = []
    
    def read_csv_to_df(csv_file):
        """
        Reads a csv file into a dataframe using only the columns from 
        the list of column names or all, if no columns list provided
        """
        if col_names: 
            df = pd.read_csv(csv_file, usecols=col_names)
        else:
            df = pd.read_csv(csv_file)
        return df
    
    # read each csv file to a dataframe and add it to the list
    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            print('Reading file: ' + str(file))
            df_list.append(read_csv_to_df(os.path.join(data_dir, file)))
        
    # combine all dataframes into one, ignoring row index
    df_all = pd.concat(df_list, ignore_index=True)
    
    return df_all

# Boston fires dataframe for 2017
bf_df = read_csv_data(dir_path, bf_col_names)

bf_df.info()

# =============================================================================
# bf_df.info() output on columns
# Data columns (total 14 columns):
# Incident Number            47355 non-null object
# Exposure Number            47355 non-null int64
# Alarm Date                 47355 non-null object
# Alarm Time                 47355 non-null object
# Incident Type              47355 non-null object
# Incident Description       47355 non-null object
# Estimated Property Loss    47355 non-null float64
# Estimated Content Loss     47355 non-null float64
# District                   47355 non-null object
# City Section               47355 non-null object
# Neighborhood               46272 non-null object
# Zip                        47355 non-null int64
# Property Use               47355 non-null object
# Property Description       44513 non-null object
# =============================================================================

# Since all Incident Type entries have a matching Incident Description we can drop Incident Type column
# Same for City Section and Neighborhood columns, the difference comes from 1083 empty strings in City Section column
bf_df.drop(columns=['Incident Type', 'City Section'])
# Or maybe not and use Incident Type for larger categories (see codes)

# Also we can combine Incident Number with Exposure Number to create a column of unique numbers instead of two
#Or maybe not and use Exposure Number for a specific subset
print(bf_df['Exposure Number'].value_counts())
# =============================================================================
# 0    47333
# 1       18
# 2        2
# 4        1
# 3        1
# Name: Exposure Number, dtype: int64
# =============================================================================

#So in 2017 there were 22 fire incidents when additional buildings and/or vehicles are exposed to the original fire incident.
print()
for item in ['Incident Type', 'Incident Description', 'District', 'Neighborhood', 
                 'Zip', 'Property Use', 'Property Description']:
    print(bf_df[item].value_counts())
    