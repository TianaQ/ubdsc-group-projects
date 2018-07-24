#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:39:26 2018

@author: tatianakurilo
"""

import pandas as pd

freelancers = pd.read_csv('marketing_all.csv')

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
        name = ''
    return name

def get_region(country_code):
    try:
        region = COUNTRY_DICT[country_code][1]
    except:
        print("Missing country code: " + country_code)
        region = ''
    return region

def get_iso_code(country_code):
    try:
        iso_code = COUNTRY_DICT[country_code][2]
    except:
        print("Missing ISO code: " + country_code)
        iso_code = ''
    return iso_code

freelancers['city'] = freelancers['Location'].apply(get_city)
freelancers['country_code'] = freelancers['Location'].apply(get_country_code)
freelancers['country_name'] = freelancers['country_code'].apply(get_country_name)
freelancers['region'] = freelancers['country_code'].apply(get_region)
freelancers['iso_code'] = freelancers['country_code'].apply(get_iso_code)
#### LOCATION IN FREELANCERS DATAFRAME END ####

#Writing csv with new columns of geographical info
freelancers.to_csv('csv/freelancers_loc.csv', sep=',', encoding='utf-8', index=False)


#### SKILLS IN FREELANCERS DATAFRAME START ####
# Converting string of skills to list of skills
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

#Writing csv with number of skills column
freelancers.to_csv('csv/freelancers_loc_num_skills.csv', sep=',', encoding='utf-8', index=False)


#creating new columns for each skill - if a freelancer has skill
def skill_in_skill_list_column( skill_col, skill):
    return skill in skill_col

for SKILL in SKILL_LIST:
    freelancers[SKILL] = freelancers['skill_list'].apply(skill_in_skill_list_column, args=(SKILL,))

# Writing csv with columns for each skill
freelancers.to_csv('csv/freelancers_skills.csv', sep=',', encoding='utf-8', index=False)

#### SKILLS IN FREELANCERS DATAFRAME END ####

#### MAKING CSV OF SKILLS ####
skills_world = []
for SKILL in SKILL_LIST:
    skill_subset = freelancers[freelancers[SKILL] == True]
    skill_pph_median = skill_subset['dollars_ph'].median()
    skill_pph_mean = skill_subset['dollars_ph'].mean()
    skill_pph_std = skill_subset['dollars_ph'].std()
    skills_world.append((SKILL, freelancers[SKILL].sum(), skill_pph_median, skill_pph_mean, skill_pph_std))
 
world_skills_df = pd.DataFrame(skills_world, columns=['skills', 'w_offers', 'w_median_pph', 'w_mean_pph', 'std'])

# Writing csv of world averages for each skill
world_skills_df.to_csv('csv/skills_world.csv', sep='\t', encoding='utf-8', index=False)


#### SKILLS BY COUNTRY ####
country_list = sorted(freelancers['iso_code'].unique().tolist())


skills_dict = {}
count = 0
print('Building Skills by Country Dictionary')
for SKILL in SKILL_LIST:
    if count % 10 == 0:
        print(count)
    count+=1
    skill_subset = freelancers[freelancers[SKILL] == True]
    for country in country_list:
        key = (SKILL, country)
        country_skill_subset = skill_subset[skill_subset['iso_code'] == country]
        if country_skill_subset.shape[0] > 0:
            skills_dict[key] = [country_skill_subset.shape[0], 
                        country_skill_subset['dollars_ph'].mean(), 
                        country_skill_subset['dollars_ph'].median()]
        else: 
            skills_dict[key] = [0, 0, 0]


mux = pd.MultiIndex.from_tuples(skills_dict.keys(), names=('skills', 'iso_code'))
skills_dict_df = pd.DataFrame(list(skills_dict.values()), index=mux)
skills_dict_df.columns = ['offers', 'mean_pph', 'median_pph']
skills_dict_df.info()

skills_iso_offers_df = world_skills_df.copy().drop(columns=['w_median_pph', 'w_mean_pph', 'std'])
skills_iso_median_df = world_skills_df.copy().drop(columns=['w_offers', 'w_mean_pph', 'std'])
skills_iso_mean_df = world_skills_df.copy().drop(columns = ['w_offers', 'w_median_pph', 'std'])
for country in country_list:
    country_offers = skills_dict_df.xs(country, level='iso_code').reset_index(level='skills').drop(columns=['mean_pph', 'median_pph'])
    country_offers.rename(columns={'offers':country}, inplace=True)
    skills_iso_offers_df = pd.merge(skills_iso_offers_df, country_offers, 'right', 'skills')
    
    country_median = skills_dict_df.xs(country, level='iso_code').reset_index(level='skills').drop(columns=['mean_pph', 'offers'])
    country_median.rename(columns={'median_pph':country}, inplace=True)
    skills_iso_median_df = pd.merge(skills_iso_median_df, country_median, 'right', 'skills')
    
    country_mean = skills_dict_df.xs(country, level='iso_code').reset_index(level='skills').drop(columns=['offers', 'median_pph'])
    country_mean.rename(columns={'mean_pph':country}, inplace=True)
    skills_iso_mean_df = pd.merge(skills_iso_mean_df, country_mean, 'right', 'skills')


skills_iso_offers_df.to_csv('csv/skills_country_offers.csv', sep='\t', encoding='utf-8', index=False)
skills_iso_median_df.to_csv('csv/skills_country_median_pph.csv', sep='\t', encoding='utf-8', index=False)
skills_iso_mean_df.to_csv('csv/skills_country_mean_pph.csv', sep='\t', encoding='utf-8', index=False)

