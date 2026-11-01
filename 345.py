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
#0r
class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        i = 0
        j = len(a) - 1
        vowels = "aeiouAEIOU"

        while i < j:
            if a[i] not in vowels:
                i += 1
            elif a[j] not in vowels:
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        return "".join(a)