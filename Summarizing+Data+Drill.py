
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
import statistics

# (Problem 1)
# Age started playing the Brady kids:
# Greg 14
# Marcia 12
# Peter 11
# Jan 10
# Bobby 8
# Cousin Oliver 8
# Cindy 6


# Sum(ages) = 69
# mean = sum / 7 = 9.857
# median = 10
# mode = 8

df = pd.DataFrame()
df['ages'] = [14, 12, 11, 10, 8, 8, 6]

mean = np.mean(df['ages'])
print(mean)
median = np.median(df['ages'])
print(median)
mode = statistics.mode(df['ages'])
print(mode)


# Choose mean since there are no extreme values causing the mean to seem abnormal


# variance = sum((x-mean)^2) / (n-1) = ((14-9.857)^2 + (12-9.857)^2 + (11-9.857)^2 + (10-9.857)^2
#					+ (8-9.857)^2 + (8-9.857)^2 + (6-9.857)^2) / 6
#	= (17.164 + 4.592 + 1.306 + 0.02 + 3.448 + 3.448 + 14.876) / 6
#	= 45.034 / 6 = 7.476
#
# std dev = 7.476^0.5 = 2.734
# std error = 2.734/(7^0.5) = 1.033

variance = np.var(df['ages'], ddof=1)
print(variance)
std = np.std(df['ages'], ddof=1)
print(std)
se = np.std(df['ages'], ddof=1) / np.sqrt(len(df['ages']))
print(se)

# Choose standard error as it is small enough to indicate a precise estimate


# In[16]:


# (Problem 2)
# Age started playing the Brady kids:
# Greg 14
# Marcia 12
# Peter 11
# Jan 10
# Bobby 8
# Cousin Oliver 8
# Cindy 7


# Sum(ages) = 70
# mean = sum / 7 = 10
# median = 10
# mode = 8

df = pd.DataFrame()
df['ages'] = [14, 12, 11, 10, 8, 8, 7]

mean = np.mean(df['ages'])
print(mean)
median = np.median(df['ages'])
print(median)
mode = statistics.mode(df['ages'])
print(mode)

# Only the sum of the ages(70) and the mean(10) changed.


# variance = sum((x-mean)^2) / (n-1) = ((14-9.857)^2 + (12-9.857)^2 + (11-9.857)^2 + (10-9.857)^2
#					+ (8-9.857)^2 + (8-9.857)^2 + (7-9.857)^2) / 6
#	= (17.164 + 4.592 + 1.306 + 0.02 + 3.448 + 3.448 + 8.162) / 6
#	= 38.14 / 6 = 6.357
#
# std dev = 6.357^0.5 = 2.521
# std error = 2.521/(7^0.5) = 0.953

variance = np.var(df['ages'], ddof=1)
print(variance)
std = np.std(df['ages'], ddof=1)
print(std)
se = np.std(df['ages'], ddof=1) / np.sqrt(len(df['ages']))
print(se)

# All values changes, variance, std dev, and std error. Each were lower than the original values in (Problem 1)


# In[22]:


# (Problem 4)
# Age started playing the Brady kids:
# Greg 14
# Marcia 12
# Peter 11
# Jan 10
# Bobby 8
# Cindy 6
# Jessica 1

# Sum(ages) = 62
# mean = sum / 7 = 8.857
# median = 10
# mode = /

df = pd.DataFrame()
df['ages'] = [14, 12, 11, 10, 8, 6, 1]

mean = np.mean(df['ages'])
print(mean)
median = np.median(df['ages'])
print(median)

# I find it more difficult to choose both a central tendency or variance value with the new data


# variance = sum((x-mean)^2) / (n-1) = ((14-8.857)^2 + (12-8.857)^2 + (11-8.857)^2 + (10-8.857)^2
#					+ (8-8.857)^2 + (6-8.857)^2) + (1-8.857)^2) / 6
#	= (26.45 + 9.878 + 4.592 + 1.306 + 0.734 + 8.162 + 61.732) / 6
#	= 112.854 / 6 = 18.809

# std dev = 18.809^0.5 = 4.337
# std error = 4.337/(7^0.5) = 1.639

variance = np.var(df['ages'], ddof=1)
print(variance)
std = np.std(df['ages'], ddof=1)
print(std)
se = np.std(df['ages'], ddof=1) / np.sqrt(len(df['ages']))
print(se)


# In[33]:


# (Problem 5)
# Percentage of Brady Bunch Fans:
# TVG 20% - 0.20
# EW 23% - 0.23
# PCT 17% - 0.17
# Sci 5% - 0.05

# I would take the mean of these percentages to estimate the % of adult Americans who were Brady Bunch fans
# on the 50th Anniversary

# (0.2 + 0.23 + 0.17 + 0.05) / 4 = 0.65 / 4 = 0.1625 ~ 16.25%

df = pd.DataFrame()
df['fanPerc'] = [0.2, 0.23, 0.17, 0.05]

mean = np.mean(df['fanPerc'])
print(mean)

# However, since SciPhi Phanatic magazine is so low (outlier) and is a very special type of magazine, 
# it might not be a good representation of the general population, so we will recalculate with only
# TV Guide, Entertainment Weekly and Pop Culture Today

df = pd.DataFrame()
df['newPerc'] = [0.2, 0.23, 0.17]

newMean = np.mean(df['newPerc'])
print(newMean)

# I would estimate the percentage of adult Americans who were Brady Bunch fans on the 50th anniversary to be 20%.sorryu 

