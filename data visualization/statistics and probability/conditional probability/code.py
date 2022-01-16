
import pandas as pd # package for data manipulation and analysis...
#import numpy as np

# data...
data= pd.read_csv('sample_obs.txt')

# probability of being a smoker / drinker.
prob_smoker= data['Smoker'].value_counts(normalize=True)[1]
prob_drinker= data['Drinker'].value_counts(normalize=True)[1]

total_obs= data.shape[0]

# probabilities
smoker_absent= data[(data['Absent']==1)&(data['Smoker']==1)]
drinker_absent= data[(data['Absent']==1)&(data['Drinker']==1)]

p_smoker_absent= smoker_absent['Smoker'].count()/total_obs
p_drinker_absent= drinker_absent['Drinker'].count()/total_obs

# conditional probability
# P(Absent|smoker)
p_smoker_absent/prob_smoker

# P(Absent|drinker)
p_drinker_absent/prob_drinker
