#written in the notes some are ot written
#leetcode1
a=[2,7,11,15]
target=9
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]+a[j]==target:
            print([i,j])

#frequency
a=[2, 3, 2, 4, 3, 2]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

