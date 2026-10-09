nums = [1,2,0,-3,6,8]
s=[]
for i in nums:
    if i>0:
        s.append(i)
print(s)
x=1
while x>0:
    if x in s:
        x+=1
print(x)





