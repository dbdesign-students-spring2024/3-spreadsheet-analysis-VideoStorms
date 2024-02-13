# place your code to clean up the data file below.

import pandas as pd

df = pd.read_csv('NYPD_Arrest_Data__Year_to_Date__20240213.csv') 

df = df.drop(df.columns[2], axis=1)

df.to_csv('modified_file.csv', index=False) 
