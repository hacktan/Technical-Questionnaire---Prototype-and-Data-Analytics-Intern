import pandas as pd
import numpy as np
df = pd.read_csv("country_vaccination_stats.csv", delimiter=",")
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')


mins=df.groupby('country').min().reset_index().set_index('country')['daily_vaccinations'] #finding all countries min values.


nans=np.where(df.daily_vaccinations.isnull()) #missing data indexes


for y in nans:
    df.daily_vaccinations[y]=mins[df.country[y]] #filling missing data with their minimum values.


nansForNoValues=np.where(df.daily_vaccinations.isnull())# a check for those with no minimum value.
if(len(nansForNoValues)):
    for y in nansForNoValues:
        df.daily_vaccinations[y]=0

print(df)
