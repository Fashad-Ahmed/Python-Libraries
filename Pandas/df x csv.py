import numpy as np
import pandas as pd

my_dict = { 'name' : ["a", "b", "c", "d", "e","f", "g"],
                   'age' : [20,27, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}

df = pd.DataFrame(my_dict)
print(df)

# to CSV
df.to_csv('csv_example', index=False)

#read file
df_csv = pd.read_csv('csv_example')
print(df_csv)

# playing with header
df_csv1 = pd.read_csv('csv_example', header=[0,1,2])
print(df_csv1)

df_csv2 = pd.read_csv('csv_example', names = ['a','b','c'])
print(df_csv2)


df_csv3 = pd.read_csv('csv_example', sep=":", index_col=[0])    #[0....,2]
print(df_csv3)
