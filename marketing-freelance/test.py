#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:33:54 2018

@author: tatianakurilo
"""
import re
text_list = ["['google analytics', 'keyword research', 'link building', 'search engine marketing (sem)', 'search engine optimization (seo)', 'social bookmarking', 'social media marketing', 'social media management', 'content writing', 'digital marketing', 'google adwords', 'Object-relational mapping (ORM, O/RM, O/R mapping tool)', 'pay per click (ppc)', 'seomoz']", "'email marketing', 'adobe illustrator', 'flyer', 'graphics design', 'logo', 'illustration', 'email design', 'email development', 'medical illustration', 'adobe photoshop', 'book illustration', "children's book illustration", 'hand drawing', 'logo design'"]
text = "email marketing', 'adobe illustrator', 'flyer', 'graphics design', 'logo', 'illustration', 'email design', 'email development', 'medical illustration', 'adobe photoshop', 'book illustration', "children's book illustration", 'hand drawing', 'logo design"
if re.match('\s".*",', text):
    print('oops')
else:
    print(text[2:-2].split("', '"))


 