
class Datavalidation(Exception):
    def __init__(self,salary,message):
        self.salary=salary
        self.message=message
        super().__init__(f"Validation Error: {salary}, {message}")


#ETL class for each line

class ETL():
    def __init__(self,name,salary):
        self.name = name
        self.salary = float(salary)

    def validate(self):
        if self.salary<0:

            raise Datavalidation(self.salary,"salary can't be Negative")
        return self.salary
    
    def to_dict(self):
        return {"name":self.name, "salary":self.salary}
    
import csv,json

result=[]
error =[]

try:

    with open("/Users/kaviya/Desktop/Employees.csv","r") as f:
        reader = csv.DictReader(f)
    
        for row in reader:
            try:
                record=ETL(row["Name"],row["Salary"])
                record.validate()
                result.append(record.to_dict())

            except Datavalidation as e:
                error.append(str(e))

except FileNotFoundError as e:
    print("File missing")


with open("/Users/kaviya/Desktop/Employees.json","w") as f:
    json.dump({"results":result, "errors":error}, f,indent=2)

