# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:45:59 2017

@author: Asif
"""
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 
FinalDataForVector=[]
a1="gr5 2017 3gb 32gb with free magic bag"
a2="gr5 2017-gold"
a3="gr3 2017"
FinalDataForVector.append("gr5 2017 3gb 32gb  free magic bag")
FinalDataForVector.append("gr5 2017-gold")
FinalDataForVector.append("gr3 2017")
word_vectorizer3gram = CountVectorizer(analyzer='word', ngram_range=(1,1), min_df=1 ,tokenizer=None)
word_vectorizer3gram.fit_transform(FinalDataForVector)
stp3gram=word_vectorizer3gram.get_feature_names()
print(stp3gram)
lst = ["gr5 2017 gold"]
sentence1 = word_vectorizer3gram.transform(lst)
s=sentence1.toarray()
s1=np.squeeze(np.asarray(s))
print("s1=",s1)
lst = ["gr3 2017"]
sentence1 = word_vectorizer3gram.transform(lst)
s=sentence1.toarray()
s2=np.squeeze(np.asarray(s))
print("s2=",s2)
lst = ["gr5 2017 3gb 32gb free magic bag"]
sentence1 = word_vectorizer3gram.transform(lst)
s=sentence1.toarray()
s3=np.squeeze(np.asarray(s))
print("s3=",s3)
from scipy import spatial
result1 =  spatial.distance.cosine(s1, s2)
print('res11= ',result1)
result2 = spatial.distance.cosine(s1, s3)
print('res22= ',result2)



print('Levenshtein distance=',nltk.edit_distance(a1, a2))
print('Levenshtein distance=',nltk.edit_distance(a3, a2))
