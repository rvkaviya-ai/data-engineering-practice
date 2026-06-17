
raw_users = [
 {'name': ' Alice ', 'email': 'alice@example.com'},
 {'name': 'bob', 'email': 'bob@example.com'},
 {'name': None, 'email': 'charlie@example.com'},
 {'name': ' CHARLIE', 'email': 'charlie2@example.com'},
]

#  name shave extra spaces, inconsistent casing, or are missing

import pandas as pd, numpy as np


df = pd.DataFrame(raw_users)

print("Before cleaning..\n")
print(df)
print("\n")

name_null_count = df["name"].isnull().sum()
print(f"name_null_count: {name_null_count}\n")

df["name"]=df["name"].str.strip().str.title().str.lower()

print("After cleaning..\n")
print(df)
print("\n")

result=df.to_dict(orient="records")

print("dataframe --> list of dict using to_dict(orient=\"records\")\n")
print(result)
