#Given an employee CSV, find the average salary per department, flag employees above department average, and write the result to a new CSV.

import pandas as pd
import numpy as np



try:    

    df = pd.read_csv("/Users/kaviya/Desktop/Employees.csv")
    print(df)

    
except FileNotFoundError as e:
    print(f"file not found issue..{str(e)}")

except Exception as e:
    print(f"Unexpected error: {str(e)}")


print(df.dtypes)
avg_df =df.groupby("Department")["Salary"].mean().reset_index()
avg_df.columns = ["Dept","avg_salary"]

df = pd.merge(df,avg_df,left_on="Department",right_on="Dept" , how ='left')
print(df)

df["level"]=np.where(df["Salary"]>df["avg_salary"],"Above_avg","Below_avg")

df=df.drop("Dept",axis=1)

print("final df:")
print(df)

df.to_csv("/Users/kaviya/Desktop/output.csv", index=False)