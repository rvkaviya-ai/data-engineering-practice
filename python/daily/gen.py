data =[10,20,30]

result =(x*10 for x in data)
print(result) # <generator object <genexpr> at 0x100e58ee0>

print(result.__next__()) # 100
print(result.__next__())
print(result.__next__())

def gen():
    for x in data:
        print(f"Processing {x}")
        yield x*10

for value in gen():
    print(value)