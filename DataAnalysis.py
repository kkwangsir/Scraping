import pandas as pd
from IPython.display import display, HTML

df1 = pd.read_csv("java_sk.csv",encoding="utf-8")
df2 = pd.read_csv("python_sk.csv")
# df = pd.concat([df1,df2], axis=0).drop_duplicates()
print(df1.shape)
print(df2.shape)
