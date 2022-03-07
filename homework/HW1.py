import pandas as pd
df = pd.read_csv("train.csv", header=None)
df.info()
df.head()

df.columns = ["label", "title", "lead"]
label_map = {1:"world", 2:"sport", 3:"business", 4:"sci/tech"}
def replace_label(x):
	return label_map[x]
df["label"] = df["label"].apply(replace_label) 

df.head()

# TODO implement a new column text which contains the lowercased title and lead
df["text"] = df["title"].str.lower() + " " + df["lead"].str.lower()
df.head()

# TODO print the number of documents for each label
df["label"].value_counts()

# TODO create a new column with the number of words for each text
import spacy
nlp = spacy.load("en_core_web_sm")
df["word_count"] = df["text"].apply(lambda x: len(x.split(" ")))