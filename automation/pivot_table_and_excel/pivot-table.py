# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 09:26:52 2022

@author: DELL
"""

import pandas as pd
import os

df = pd.read_excel('supermarket_sales.xlsx')
df = df[['Gender','Product line', 'Total']]

# df = print(df)

pivot_table = df.pivot_table(index="Gender", columns ='Product line', values= 'Total', aggfunc='sum').round(0)
# print(pivot_table)
pivot_table.to_excel("pivot_table.xlsx", "Report", startrow = 4)