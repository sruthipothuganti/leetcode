#169
a = [2, 2, 1, 1, 1, 2, 2,3,3,3,3,3]
n=len(a)
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    if value>n//2:
        print(key)