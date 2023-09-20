#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('popular')


# In[3]:


get_ipython().system('pip install PySastrawi')


# In[4]:


get_ipython().system('pip install Sastrawi')


# ## Preproses Text Dengan NLTK dan Sastrawi

# In[5]:


import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[7]:


f = open('E:\\TUGAS NLP\\Tugas 1\\pidato_presiden.txt', encoding='utf-8')
isi_berita = f.read()
print(isi_berita)


# In[8]:


word_tokens = word_tokenize(isi_berita)
print(word_tokens)


# In[9]:


stop_words = set(stopwords.words('indonesian'))
word_tokens_no_stopwords = [w for w in word_tokens if not w in stop_words]
print(word_tokens_no_stopwords)


# In[10]:


freq_kata_1 = nltk.FreqDist(word_tokens)
freq_kata_2 = nltk.FreqDist(word_tokens_no_stopwords)
print(freq_kata_1.most_common(20))
print()
print(freq_kata_2.most_common(20))


# In[11]:


import matplotlib.pyplot as plt


# In[12]:


freq_kata_1.plot(20)
freq_kata_2.plot(20)
plt.show()


# In[13]:


#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Figures inline and set visualization style
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(word_tokens_no_stopwords)
freqdist1.plot(25)
plt.show()


# In[ ]:




