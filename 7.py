x = -123
rev=0
if x>0:
    sign=1
else:
    sign=-1
x=abs(x)
while x>0:
    d=x%10
    rev=rev*10+d
    x=x//10
print(rev*sign)
