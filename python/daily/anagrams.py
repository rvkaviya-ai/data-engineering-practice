
count=[0]*26

print (count)

from collections import defaultdict

x=defaultdict(list)

x ={
    "name":["kavs","kishore"],
    "age":[24,23]
}
print(type(list(x.values())))

print(x.values())
print(list(x.values()))

y= {}

y["key1"]=[]
y["key2"]=['a','b']

print(type(y.values()))
print(list(y.values()))
