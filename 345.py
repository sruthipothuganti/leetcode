s = "IceCreAm"
vowels="aeiouAEIOU"
li=[]
for i in s:
    if i in vowels:
        li.append(i)
li.reverse()
s=list(s)
j=0
for i in range(len(s)):
    if s[i] in vowels:
        s[i]=li[j]
        j+=1
print(*s)
