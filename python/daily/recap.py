

nums = [4,3,2,7,8,2,3,1]

count={}

for n in nums:
    count[n]=count.get(n,0)+1

print(count)

res =[]

for n,c in count.items():
    if c ==2: res.append(n)

print(res)