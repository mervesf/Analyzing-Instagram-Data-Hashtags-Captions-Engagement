# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 23:28:29 2023

@author: user
"""
import pandas as pd
import numpy as np

df=pd.read_csv('Instagram data.csv',encoding = 'latin1')

#Number of views of tweets according to their hashtags (from most to least, respectively)/ And the words in the hashtag tags in each of #them
from_hashtag=df[['From Hashtags','Hashtags']].sort_values(by='From Hashtags',ascending=False)
def find_words(values):
    result=[]
    for i in values:
        li2=[]
        for j in range(0,len(i)):
            i=i+'\#'
            if i[j]=='#':
                for k in range(j+1,len(i)) :
                    if (i[k]=='#'):
                        li2.append(i[j+1:k-1])
                        break
        result.append(li2)
    return result

result_hashtag=find_words(from_hashtag['Hashtags'])

# Number of views of tweets according to their hastags (from most to least, respectively)/ And the words in the caption of each one:

from_caption=df[['From Hashtags','Caption']].sort_values(by='From Hashtags',ascending=False)
def find_words_caption(values):
    unique=[]
    char='.:,;&'
    result=[]
    for i in values:
        for j in char:
            i=i.replace(j,'')
        result.append(i.split(' '))
    for i in result:
        for j in i:
            if j not in unique:
                unique.append(j)
    return result,unique


# How posts with words in common with each other are displayed:
def compare(data,list1):
    print(data)
    print(data.index)
    
    ordinal_hashtags=[]
    new_index=pd.DataFrame(list(range(0,len(data.index))),index=data.index)
    data2=pd.DataFrame(data,index=data.index)
    data2=data2.sort_values(by=data2.columns[0],ascending=False)
    for i in data2.index:
        for j  in np.arange(0,len(data.index)):
            if data.index[j]==i:
                ordinal_hashtags.append(list1[j])
    return ordinal_hashtags
def max_near_feature(variable):
    new_data=pd.DataFrame(variable).sort_values(by=0,ascending=False)
    return new_data.iloc[:10,:].index
def find_common(list1,value):
    common_value=[]
    for i in list1:
        common_value.append(sum(list(map(lambda x, y: 1 if x == y else 0, i, value))))
    return common_value
def find_near_feature(data):
    hashtag_list=[]
    common_list=[]
    result_caption,unique_words=find_words_caption(data.iloc[:,11])
    for i in range(0,len(result_caption)):
            near_list=find_common(result_caption,result_caption[i])
            common_list.append(max_near_feature(near_list))
    for i in range(0,len(common_list)):
        hashtag_list.append(find_words(data.iloc[common_list[i],12]))
        
   
    result_final=compare(data.iloc[common_list[0],8],hashtag_list[0])
  
    return result_final

sonuc=find_near_feature(df)



        

