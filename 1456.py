#leetcode 1456
s = "abciiidef"
k=3
l=0
v="aeiouAEIOIU"
c=0
m=0
for i in range(len(s)):
    if s[i] in v:
        c+=1
    if i-l+1==k:
        m=max(m,c)
        if s[l] in v:
            c-=1
        l+=1
print(m)