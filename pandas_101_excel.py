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

print('Weight added:\n', cats_df)
print('\n')

#count how many cats
count = cats_df['Cat'].count()
print('Count：', count)
print('\n')

#average weight of the cats
avg = cats_df['Weight'].mean()
print('Mean:', avg)
print('\n')

#max weight of the cats
max_number = cats_df['Weight'].max()
print('Max:', max_number)
print('\n')

#standard deviation weight of the cats by groups
std = cats_df['Weight'].std()
print('Standard Deviation:\n', std)
print('\n')

#average weight of the cats by groups
avg = cats_df.groupby('Cat').mean()
print('Group Mean:\n', avg)
print('\n')

#average weight of the cats by groups
g_count = cats_df.groupby('Cat')['Owner'].count()
print('Group Count by Owner:\n', g_count)

#average weight by category of cats
g_mean = cats_df.groupby('Cat')['Weight'].mean()
print('Group Average Weight of Cats by type:\n', g_mean)
print('\n')


