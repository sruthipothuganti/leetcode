#longest substring
s = "abcabcbb"
t=""
ans=0
for i in s:
    if i in t:
        t=t[t.index(i)+1:]
    t+=i
    ans=max(ans,len(t))
print(ans)
#or
s = "abcabcbb" 
s1=set()
l=0
m=0
for i in range(len(s)):
    if s[i] in s1:
        s1.remove(s[l])
        l+=1
    s1.add(s[i])
    m=max(m,i-l+1)
print(m)