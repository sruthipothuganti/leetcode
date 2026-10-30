s = "(()())(())"
c=0
r=[]
for i in s:
  if i=="(":
    if c>0:
      r.append(i)
    c+=1
  elif i==")":
      c-=1
      if c>0:
        r.append(i)
print("".join(r))
