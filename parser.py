import pandas as pd
from attributes import *

pd.options.display.max_colwidth = 20
df = pd.read_csv("mlchallenge_set_2021.tsv", header=None, sep='\t', names=['category','primary_image','all_image','attributes','index'])
df['attributes']=df['attributes'].apply(lambda x: attribute_parser(x))
print(df.head())
