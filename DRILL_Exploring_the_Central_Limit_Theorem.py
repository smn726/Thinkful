
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt


# In[3]:


pop1 = np.random.binomial(10, 0.2, 10000)
pop2 = np.random.binomial(10, 0.5, 10000)

# Let's make a histogram for the two groups

plt.hist(pop1, alpha=0.5,  label='pop1')
plt.hist(pop2, alpha=0.5, label='pop2')
plt.legend(loc='upper right')
plt.show()


# In[15]:


print(pop1.mean())
print(pop1.std())
print(pop2.mean())
print(pop2.std())


# In[4]:


sample1 = np.random.choice(pop1, 100, replace=True)
sample2 = np.random.choice(pop2, 100, replace=True)

plt.hist(sample1, alpha=0.5, label='sample1')
plt.hist(sample2, alpha=0.5, label='sample2')
plt.legend(loc='upper right')
plt.show()


# In[5]:


print(sample1.mean())
print(sample2.mean())
print(sample1.std())
print(sample2.std())

# Compute the difference between the two sample means
diff = sample2.mean() - sample1.mean()
print(diff)


# In[6]:


size = np.array([len(sample1), len(sample2)])
sd = np.array([sample1.std(), sample2.std()])

# The squared std dev. are devided by the sample size and summed,
# then we take the square root of the sum
diff_se = (sum(sd ** 2 / size)) ** 0.5

# The difference between the means divided by the standard error: T-value.
print(diff/diff_se)


# In[7]:


from scipy.stats import ttest_ind
print(ttest_ind(sample2, sample1, equal_var=False))


# In[10]:


# (1)
# n = 1000 , I expect the sample means to follow a more normal probability distribution,
# clustering around the true population mean
sample3 = np.random.choice(pop1, 1000, replace=True)
sample4 = np.random.choice(pop2, 1000, replace=True)

plt.hist(sample3, alpha=0.5, label='sample1')
plt.hist(sample4, alpha=0.5, label='sample2')
plt.legend(loc='upper right')
plt.show()


# In[14]:


print(sample3.mean())
print(sample3.std())
print(sample4.mean())
print(sample4.std())


# In[17]:


# n = 20, I expect these sample means to greatly misrepresent the true population mean
sample5 = np.random.choice(pop1, 20, replace=True)
sample6 = np.random.choice(pop2, 20, replace=True)

plt.hist(sample5, alpha=0.5, label='sample1')
plt.hist(sample6, alpha=0.5, label='sample2')
plt.legend(loc='upper right')
plt.show()


# In[18]:


print(sample5.mean())
print(sample5.std())
print(sample6.mean())
print(sample6.std())


# In[21]:


# (2)
pop1 = np.random.binomial(10, 0.3, 10000)

sample7 = np.random.choice(pop1, 1000, replace=True)
sample8 = np.random.choice(pop2, 1000, replace=True)

plt.hist(sample7, alpha=0.5, label='sample1')
plt.hist(sample8, alpha=0.5, label='sample2')
plt.legend(loc='upper right')
plt.show()

print(sample7.mean())
print(sample7.std())
print(sample8.mean())
print(sample8.std())

diff1 = sample8.mean() - sample7.mean()
size1 = np.array([len(sample7), len(sample8)])
sd1 = np.array([sample7.std(), sample8.std()])

diff_se1 = (sum(sd1 ** 2 / size1)) ** 0.5

print(diff1/diff_se1)


# In[22]:


pop1 = np.random.binomial(10, 0.4, 10000)

sample9 = np.random.choice(pop1, 1000, replace=True)
sample10 = np.random.choice(pop2, 1000, replace=True)

plt.hist(sample9, alpha=0.5, label='sample1')
plt.hist(sample10, alpha=0.5, label='sample2')
plt.legend(loc='upper right')
plt.show()

print(sample9.mean())
print(sample9.std())
print(sample10.mean())
print(sample10.std())

diff2 = sample10.mean() - sample9.mean()
size2 = np.array([len(sample9), len(sample10)])
sd2 = np.array([sample9.std(), sample10.std()])

diff_se2 = (sum(sd2 ** 2 / size2)) ** 0.5

print(diff2/diff_se2)


# In[23]:


# The t-value was lower when the p-value was higher, in the second iteration.


# In[25]:


# (3)

pop3 = np.random.logistic(10, 0.2, 10000)
pop4 = np.random.logistic(10, 0.5, 10000)

print(pop3.mean())
print(pop4.mean())

# Let's make a histogram for the two groups

plt.hist(pop3, alpha=0.5,  label='pop1')
plt.hist(pop4, alpha=0.5, label='pop2')
plt.legend(loc='upper right')
plt.show()

sample11 = np.random.choice(pop3, 1000, replace=True)
sample12 = np.random.choice(pop4, 1000, replace=True)

plt.hist(sample11, alpha=0.5, label='sample1')
plt.hist(sample12, alpha=0.5, label='sample2')
plt.legend(loc='upper right')
plt.show()

print(sample11.mean())
print(sample11.std())
print(sample12.mean())
print(sample12.std())

diff3 = sample12.mean() - sample11.mean()
size3 = np.array([len(sample11), len(sample12)])
sd3 = np.array([sample11.std(), sample12.std()])

diff_se3 = (sum(sd3 ** 2 / size3)) ** 0.5

print(diff3/diff_se3)


# In[ ]:


# Using the logistic distribution, the sample means still accurately represent the population values.

