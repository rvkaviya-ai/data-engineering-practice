
# task is to parse the file and extract all lines where the log level is "ERROR"

import pandas as pd

data = pd.read_csv("/Users/kaviya/Desktop/log.csv") # read csv file and convert content into data frame

data["level"]=data["level"].str.strip()

print(data)
print("\n")

error_log = data[data["level"]=='ERROR']

print(error_log)