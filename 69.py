n=8
left=0
right=n
ans=0
while left<=right:
  mid=(left+right)//2
  sqrt=mid*mid
  if sqrt==n:
    ans=mid
    break
  elif sqrt<n:
    ans=mid
    left=mid+1
  else:  
    right=mid-1
print(ans)

