# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:31:48 2020

@author: redjack

"""
import pandas as pd

cats_df = pd.read_excel('cats.xlsx', index_col=0) 

print(cats_df)

print('\n')

#reset index
cats_df = cats_df.reset_index()

print(cats_df)
print('\n')

#Add how heavy they are
cats_df['Weight'] = [10.0, 7.7, 5.8, 3.2, 5.8]

print('Weight added:', cats_df)
print('\n')

#count how many cats
count = cats_df['Cat'].count()
print('Count：', count)
print('\n')

#average weight of the cats
avg = cats_df['Weight'].mean()
print('Mean:', avg)
print('\n')

#average weight of the cats by groups
avg = cats_df.groupby('Cat').mean()
print('Group Mean:', avg)



