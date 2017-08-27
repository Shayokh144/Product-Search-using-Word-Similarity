# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:10:38 2017

@author: Asif
"""


productList=['shirt','pant','pen','bat','ball','xcamera','camera','cameras8']
#productList=['shirt']
queryList=['shijt','pent','pans','camera','camera s8']
letters    = 'abcdefghijklmnopqrstuvwxyz 0123456789'
print(len(letters))

'''
using cosine distance
'''
from scipy import spatial
import operator

charDct={}
cnt=0
for char in letters:
    charDct.update({char:cnt})
    cnt+=1

#print(charDct['a'])

sorted_lst=[]

for query in queryList:
    
    print("\n\n",query)
    vpl=[0]*37
    vql=[0]*37
    
    for char in query:
        vql[charDct[char]]+=1
    recoDct={}
    for item in productList:
        
        for c in item:
            vpl[charDct[c]]+=1
        result = 1 - spatial.distance.cosine(vpl, vql)
        recoDct.update({item:result})
        #print(query,"  ",item,"  ",result)
        vpl=[0]*37
    sorted_lst=sorted(recoDct.items(), key=operator.itemgetter(1),reverse=True)
    for i,j in sorted_lst:
        print(i,"=",j)
 
    #print(sorted_lst)
        
    
#print(sorted_lst) 





'''
using sequence matcher

'''
import difflib

for query in queryList:
    a=query
    for product in productList:
        b=product
        seq = difflib.SequenceMatcher(None,a,b)
        d = seq.ratio()*100
        print("SM   ",query,'   ',product,'    ',d)


























    