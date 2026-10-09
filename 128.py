a = [100, 4, 200, 1, 3, 2]
s=set(a)
c=0
m=0
for i in s:
    if i-1 not in s:
        c=1
        n=i
        while n+1 in s:
            c+=1
            n+=1
        m=max(m,c)
print(m)