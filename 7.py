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
rev=rev*sign
if rev < -2147483648 or rev > 2147483647:
    print(0)
else:
    print(rev)
