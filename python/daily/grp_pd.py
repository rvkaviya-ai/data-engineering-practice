
import pandas as pd

df = pd.DataFrame({
    "name":   ["Kaviya","Ravi","Meena","Kumar","Divya","Priya"],
    "dept":   ["DE","Analytics","DE","Analytics","DE","Analytics"],
    "salary": [90000, 80000, 95000, 70000, 85000, 75000],
    "exp":    [4, 3, 6, 2, 5, 3]
})

print(df)

print("\n")

#Group the df by dept, find average salary, max experience, and count of employees

result = df.groupby("dept").agg(
    avg_salary =  ("salary","mean"),
    max_exp = ("exp","max"),
    head_count = ("name","count")
).reset_index()

print(result)   

def level(x):
    return "Senior" if x>3 else "Junior"

df["emp_level"] = df["exp"].apply(lambda x: "Senior" if x>3 else "Junior") #apply(lambda x: "Senior" if x>3 else "Junior")

print ("new column: emp_level added !\n")
print(df)

#df.to_csv("/Users/kaviya/Desktop/Employees_data.csv",sep='|',index=False)