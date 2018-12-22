
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[23]:


# Logistic distribution
logistic = np.random.logistic(0, 1, 1000)
plt.hist(logistic)
plt.axvline(logistic.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(logistic.mean () + logistic.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(logistic.mean() - logistic.std(), color='b', linestyle='dashed', linewidth=2)

plt.show()


# In[24]:


logistic.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, logistic, 'o')
plt.show()


# In[25]:


# It seems the data from a logistic distribution is normally distributed.


# In[29]:


# Beta distribution
beta = np.random.beta(2, 3, 1000)
plt.hist(beta)
plt.axvline(beta.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(beta.mean () + beta.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(beta.mean() - beta.std(), color='b', linestyle='dashed', linewidth=2)

plt.show()


# In[30]:


beta.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, beta, 'o')
plt.show()


# In[31]:


# The data from a beta distribution should be evaluated further to determine normality.


# In[35]:


# Gumbel distribution
gumbel = np.random.gumbel(0, 1, 1000)
plt.hist(gumbel)
plt.axvline(gumbel.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(gumbel.mean () + gumbel.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(gumbel.mean() - gumbel.std(), color='b', linestyle='dashed', linewidth=2)

plt.show()


# In[36]:


gumbel.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, gumbel, 'o')
plt.show()


# In[37]:


# The data from a gumbel distribution does not support a normal distribution strongly.


# In[70]:


# Chisquare distribution
chisquare = np.random.chisquare(2, 1000)
plt.hist(chisquare)
plt.axvline(chisquare.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(chisquare.mean () + chisquare.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(chisquare.mean() - chisquare.std(), color='b', linestyle='dashed', linewidth=2)

plt.show()


# In[71]:


chisquare.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, chisquare, 'o')
plt.show()


# In[44]:


# The data from a chisquare distribution does not seem to be normally distributed


# In[66]:


# Pareto distribution
pareto = np.random.pareto(3, 1000)
plt.hist(pareto)
plt.axvline(pareto.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(pareto.mean () + pareto.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(pareto.mean() - pareto.std(), color='b', linestyle='dashed', linewidth=2)

plt.show()


# In[67]:


pareto.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, pareto, 'o')
plt.show()


# In[48]:


# The data in a pareto distribution is not normally distributed


# In[55]:


# Weibull distribution
weibull = np.random.weibull(2, 1000)
plt.hist(weibull)
plt.axvline(weibull.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(weibull.mean () + weibull.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(weibull.mean() - weibull.std(), color='b', linestyle='dashed', linewidth=2)

plt.show()


# In[56]:


weibull.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, weibull, 'o')
plt.show()


# In[72]:


# The data from a weibull distribution does seem to be normally distributed


# In[73]:


# Generate two normally-distributed varibles, one with a mean of 5 and std dev. or 0.5,
# and the other with a mean of 10 and a std dev of 1


# In[85]:


var1 = np.random.normal(5, 0.5, 1000)
var2 = np.random.normal(10, 1, 1000)
var3 = var1 + var2


# In[86]:


plt.hist(var3)
plt.axvline(var3.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(var3.mean() + var3.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(var3.mean() - var3.std(), color='b', linestyle='dashed', linewidth=2)
plt.show()


# In[87]:


var3.sort()
norm = np.random.normal(0, 1, 1000)
norm.sort()
plt.plot(norm, var3, 'o')
plt.show()


# In[ ]:


# The data from var3 is normally distributed.

