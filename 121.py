#121
a=[7,1,5,3,6,4]
mini=a[0]
ans=0
for i in range(1,len(a)):
    mini=min(mini,a[i])
    ans=max(ans,a[i]-mini)
print(ans)