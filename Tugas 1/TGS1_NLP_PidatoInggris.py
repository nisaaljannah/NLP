#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('popular')


# In[6]:


import requests
import urllib.request
#response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
response =  urllib.request.urlopen('https://siddiqleksono.wordpress.com/2011/05/29/text-pidato-presiden-amerika-barack-obama-di-ui-versi-english/')
html = response.read()
print(html)


# In[7]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
text = soup.get_text(strip = True)
print(text)


# In[8]:


tokens = [t for t in text.split()]
print(tokens)


# In[9]:


from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)


# In[10]:


freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))


# In[11]:


freq.plot(20, cumulative=False)


# In[ ]:




