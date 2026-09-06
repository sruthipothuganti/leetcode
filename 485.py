nums = [1,1,0,1,1,1]
c=0
maxi=0
for i in nums:
    if i==1:
        c+=1
    else:
        c=0
    maxi=max(maxi,c)
print(maxi)