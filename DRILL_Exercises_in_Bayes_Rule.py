
# coding: utf-8

# In[1]:


# A = Test giving a positive result
# A~ = Test giving negative result
# B = Person suffering from Tripshaw's Disease (TD)
# B~ = Person not suffering from TD
# P(B) = 0.5% = 0.005
# P(B~) = 1 - 0.005 = 0.995
# P(A|B) = P(B|A) * P(A) / P(B) = 98% = 0.98
# Therefore, P(~A|B) = 0.02
# P(A|B~) = P(B~|A) * P(A) / P(B~) = 10% = 0.10
# Therefore, P(~A|B~) = 0.90


# In[ ]:


# (1)
# By intuition, I'd suggest the chances are very close to the probability of a test coming up
# positive on a person not suffering from TD, ie, ~10%

# P(A) = (Probability the test is positive given person suffering)*(Probability person suffering) + 
#        (Probability the test is positive given person not suffering)*(Probability person not suffering) = 
#        P(A|B)*P(B) + P(A|~B)*P(B~) = (0.98)(0.005) + (0.10)*(0.995) = 0.0049 + 0.0995 = 0.1044

# My intuition and the calculations were similar.

# (2)
# This was given as "a 98% probability of giving a positive result when applied to a person suffering from TD".
# By intuition and calculation I'd determine P(A|B) = 98% = 0.98

# (3)
# We were told that the test had a 10% probability of giving a false positive when applied 
# to a non-sufferer or P(A|B~) = 0.10
# By intuition, I'd suggest there is a 90% probability of giving a negative result when applied to a non-sufferer.
# Given P(A|B~) = 0.10 => P(~A|~B) = 1 - P(A|B~) = 1 - 0.10 = 0.90

# (4)
# Intuitively, I'd say the test has a low chance of misclassifying a person.
# By calculation, we are looking for P(A|B~) + P(A~|B) = (0.10) + (0.02) = 0.12 = 12%

