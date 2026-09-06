intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
ans=[]
for i in intervals:
  if not ans or i[0]>ans[-1][1]:
    ans.append(i)
  else:
    ans[-1][1]=max(ans[-1][1],i[1])
print(ans)
    
  

