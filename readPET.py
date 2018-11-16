# do one thing and do it well
# wrapper function reads the PET file int a pandas dataframe

import os, pandas as pd

def readPET(str_file):
    df = pd.read_csv(str_file)
    return df

str_path = 'C:\\Users\\kbranna\\Source\\Repos\\daily_to_hourly_met'
str_file_csv = 'siletz_HSPF_PET.csv'
str_file = os.path.join(str_path, str_file_csv)

df = readPET(str_file)

# check out the object type
type(df)
# what are the dimensions
df.shape
# what are the coumn names
col_names = list(df)
col_names

# look at first 10 rows
df.iloc[:10,]

