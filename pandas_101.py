# -*- coding: utf-8 -*-

#Created on Thu Apr 23 21:28:45 2020

#@author: redjack

import pandas as pd
import numpy as np

#simply array
data = np.array(['strawberry', 'apple', 'orange'])

print(data)

#put numpy to a dataframe
df = pd.DataFrame(data)

#See what's the difference between pandas & numpy?
print('Original DataFrame:\n', df)
print('\n')

#print the first 3
print('Print first 3 rows:\n', df.head(3))
print('\n')

#Give the first column a name
df.rename(columns = {list(df)[0]: 'Fruit'}, inplace = True)
    
print('Give a name to the first column:', '\n', df)
print('\n')

#Add a column to pandas dataframe; declare colour as a list
colour = ['red','red','orange']

df['Colour'] =  colour

print('DataFrame with one more column:\n', df)
print('\n')

#Add a row to this dataframe:
df = df.append({'Fruit': 'pear', 'Colour': 'yellow'}, ignore_index=True)

print('Add one row to the DataFrame:\n', df)
