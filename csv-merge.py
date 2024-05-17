'''
This program reads two csv files and merges them based on a common key column.
'''
# import the pandas library
# you can install using the following command: pip install pandas

import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_csv('CSV1.csv')
df2 = pd.read_csv('CSV2.csv')

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = 'ID_')
df3.set_index('ID_', inplace = True)

# Write it to a new CSV file
df3.to_csv('CSV3.csv')
