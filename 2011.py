operations=int(input())
ans=0
for i in range(operations):
    operations=input()
    if operations=="++X" or operations=="X++":
        ans+=1
    else:
        ans-=1
print(ans)