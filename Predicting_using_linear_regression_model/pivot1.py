# Code to understand how 'pivot' function of Pandas work 
import pandas as pd 
import numpy as np 
df = pd.DataFrame({'foo':['one', 'one', 'one','two','two','two'], 
'bar': ['A', 'B', 'C', 'A','B','C'], 
'baz':[1,2,3,4,5,6], 
'zoo':['x','y','z','q','w','t']}) 
print('Original Dataframe') 
print(df) 
print('\n') 
print('Reshaped Dataframe after pivot') 
print(df.pivot(index='foo', columns='bar',values='baz')) 
print('\n') 
