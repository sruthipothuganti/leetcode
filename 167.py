#leetcode 2114
"""a=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
ans=0
for i in range(len(a)):
    temp=a[i]
    c=1
    for j in range(len(temp)):
        if(temp[j]==" "):
            c+=1
    ans=max(ans,c)
print(ans)"""
"""
#leetcode 2011
operations=int(input())
ans=0
for i in range(operations):
    operations=input()
    if operations=="++X" or operations=="X++":
        ans+=1
    else:
        ans-=1
print(ans)
"""
"""
#leetcode 1108
a=input()
r=""
for i in a:
    if i ==".":
        r+="[.]"
    else:
        r+=i
print(r)"""
"""
#leetcode 167
a=[2,4,7,11]
t=9
l=0
r=len(a)-1
while(l<r):
    ts=a[l]+a[r]
    if ts==t:
        print([l+1,r+1])
        break
    elif ts>t:
        r-=1
    else:
        l+=1"""