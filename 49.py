a = ["eat","tea","tan","ate","nat","bat"]
s={}
for i in a:
    key=''.join(sorted(i))
    if key not in s:
        s[key]=[]
    s[key].append(i)
print(list(s.values()))