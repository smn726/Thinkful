
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic('matplotlib inline')


# In[43]:


apps = pd.read_csv('googleplaystore.csv')
print(apps)


# In[45]:


apps.iloc[0:11, 1:3]


# In[90]:


# Here we extract only the ART_AND_DESIGN app reviews

arts = apps[apps['Category'] == "ART_AND_DESIGN"]


# In[91]:


print(arts)


# In[96]:


# Here we further breakdown the ART_AND_DESIGN reviews to only include those of Free apps

freeArts = arts[arts['Type'] == 'Free']


# In[97]:


print(freeArts)


# In[161]:


# Here we create an array of only Ratings and exclude the NaN Ratings

freeArtsRatings = freeArts.iloc[:, 2]
freeArtsRatings = freeArtsRatings.dropna()


# In[162]:


print(freeArtsRatings)


# In[149]:


# Here we plot the free app ratings in a histogram 

plt.hist(freeArtsRatings)


# In[154]:


# Here we plot the ratings into a boxplot

plt.boxplot(freeArtsRatings)


# In[164]:


# From the boxplot, you can determine the mean to be around 4.375.
# The lowest rating was slightly below a 3.25 and the highest rating is a 5.0

