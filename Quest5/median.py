# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:14:48 2021

@author: haktu
"""
#%% Question 5
import pandas as pd
df = pd.read_csv("country_vaccination_stats.csv", delimiter=",")
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

medians=df.groupby('country').median().sort_values(by=['daily_vaccinations'],ascending=False)

print(medians.head(3))
