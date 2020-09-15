import pandas as pd
pd.options.display.max_colwidth = 20
df = pd.read_csv("yy.tsv", header=None, sep='\t')
print(df.head())