#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:39:26 2018

@author: tatianakurilo
"""

import pandas as pd

freelancers = pd.read_csv('marketing_all.csv')
freelancers.info()

country_codes = pd.read_csv('country_codes.csv')
COUNTRY_DICT = country_codes.set_index('Code').T.to_dict('list')

# =============================================================================
# RangeIndex: 10003 entries, 0 to 10002
# Data columns (total 5 columns):
# Name              10003 non-null object
# Bio               10002 non-null object
# Location          10003 non-null object
# Skills            10003 non-null object
# Price per hour    10003 non-null object
# =============================================================================

# =============================================================================
# Georg S.	
# SEO Expert & Content Creater
# Munich, DE	
# ['link building', 'search engine optimization (seo)', 'search engine optimization article (seo article)', 
# 'online marketing', 'German translation', 'content management', 'content marketing', 'off-page optimization']	
# $59
# =============================================================================

## Price Per Hour to numbers
def clear_dollar_sign(price_per_hour):
    price = price_per_hour[1:]
    if price[-1].lower() == 'k':
        price = price[:-1] + '00'
        if '.' in price in price:
            price = "".join(price.split('.'))
    return float(price)

freelancers['dollars_ph'] = freelancers['Price per hour'].apply(clear_dollar_sign)

#### LOCATION IN FREELANCERS DATAFRAME START ####
def get_city(location):
    return location.split(',')[0].strip()

def get_country_code(location):
    return location.split(',')[-1].strip()

def get_country_name(country_code):
    try:
        name = COUNTRY_DICT[country_code][0]
    except:
        print("Missing country code: " + country_code)
        name = 'NA'
    return name

def get_region(country_code):
    try:
        region = COUNTRY_DICT[country_code][1]
    except:
        print("Missing country code: " + country_code)
        region = 'NA'
    return region

def get_iso_code(country_code):
    try:
        iso_code = COUNTRY_DICT[country_code][2]
    except:
        print("Missing ISO code: " + country_code)
        iso_code = 'NA'
    return iso_code

freelancers['city'] = freelancers['Location'].apply(get_city)
freelancers['country_code'] = freelancers['Location'].apply(get_country_code)
freelancers['country_name'] = freelancers['country_code'].apply(get_country_name)
freelancers['region'] = freelancers['country_code'].apply(get_region)
freelancers['iso_code'] = freelancers['country_code'].apply(get_iso_code)
#### LOCATION IN FREELANCERS DATAFRAME END ####

freelancers.info()
freelancers.to_csv('freelancers.csv', sep=',', encoding='utf-8', index=False)


#### SKILLS IN FREELANCERS DATAFRAME START ####
#Converting string of skills to list of skills
def get_skill_list_from_string(skill_string):
    if len(skill_string) > 0:
        skill_list = skill_string[2:-2].split("', '")
        if '' in skill_list:
            skill_list.remove('')
    return skill_list
            
# Getting list of unique skills
def get_unique_skills(skills_colunm):
    skill_set = set()
    def build_skill_set(skill_string):
        lst = get_skill_list_from_string(skill_string)
        [skill_set.add(x) for x in lst]
    skills_colunm.apply(build_skill_set)    
    return skill_set

SKILL_SET = (get_unique_skills(freelancers['Skills']))
SKILL_LIST = sorted([x.strip() for x in SKILL_SET]) 
print(len(SKILL_LIST))


freelancers['skill_list'] = freelancers['Skills'].apply(get_skill_list_from_string)
freelancers['num_of_skills'] = freelancers['skill_list'].apply(len)

freelancers.to_csv('freelancers_num_skills.csv', sep=',', encoding='utf-8', index=False)

#creating new columns for each skill - if a freelancer has skill
def skill_in_skill_list_column( skill_col, skill):
    return skill in skill_col

for SKILL in SKILL_LIST:
    freelancers[SKILL] = freelancers['skill_list'].apply(skill_in_skill_list_column, args=(SKILL,))

# Writing csv with skill columns 
freelancers.info()
freelancers.to_csv('freelancers_skills.csv', sep=',', encoding='utf-8', index=False)

#### SKILLS IN FREELANCERS DATAFRAME END ####

#### MAKING CSV OF SKILLS ####
skill_freq = []
for SKILL in SKILL_LIST:
    skill_subset = freelancers[freelancers[SKILL] == True]
    skill_pph_mean = skill_subset['dollars_ph'].mean()
    skill_pph_std = skill_subset['dollars_ph'].std()
    skill_freq.append((SKILL, freelancers[SKILL].sum(), skill_pph_mean, skill_pph_std))
 
skills_df = pd.DataFrame(skill_freq, columns=['skill', 'frequency', 'mean', 'std'])
skills_df.info()
skills_df.to_csv('skills.csv', sep='\t', encoding='utf-8', index=False)