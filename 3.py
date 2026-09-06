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