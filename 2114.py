a=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
ans=0
for i in range(len(a)):
    temp=a[i]
    c=1
    for j in range(len(temp)):
        if(temp[j]==" "):
            c+=1
    ans=max(ans,c)
print(ans)