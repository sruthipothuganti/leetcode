a=[2,3,1,2,3,4]
target=7
l=0
r=0
s=0
min_len=float('inf')
while r<len(a):
    s+=a[r]
    while s>=target:
        length=r-l+1
        min_len=min(min_len,length)
        s-=a[l]
        l+=1
    r+=1
if min_len==float('inf'):
    print(0)
print(min_len)