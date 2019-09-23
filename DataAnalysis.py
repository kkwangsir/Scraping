import pandas as pd
from IPython.display import display, HTML
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter


df1 = pd.read_csv("java_sk.csv",encoding="utf-8")
df2 = pd.read_csv("python_sk.csv")
df = pd.concat([df1,df2], axis=0).drop_duplicates()
df=df1.append(df2).drop_duplicates()
print("after clean duplicates: ",df.shape)

# df = df[df.Sponsored != 'Sponsored']
print("after clean Sponsored: ",df.shape)

counts = df.groupby("Company").count()["Title"].sort_values(ascending=False)[:10]
counts.plot("bar",figsize=(20,5))
plt.savefig("img/companies.png")

plt.show()


def cleanData(desc):
    desc = word_tokenize(desc)
    desc = [word.lower() for word in desc if word.isalpha() and len(word) > 2]
    desc = [word for word in desc if word not in stop_words]
    return desc
# nltk.download('punkt')
# nltk.download('punkt')

stop_words = stopwords.words('english')

tags_df = df["Description"].apply(cleanData)

result = tags_df.apply(Counter).sum().items()
result = sorted(result, key=lambda kv: kv[1],reverse=True)
result_series = pd.Series({k: v for k, v in result})
skills = ["senior","expert","intern","intermediate","entry","fresher"]

filter_series = result_series.filter(items=skills)
filter_series.plot('bar',figsize=(10,5))

plt.savefig("img/level.png")

plt.show()

