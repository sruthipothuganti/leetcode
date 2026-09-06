nums=[1,2,3,1]
l=0
r=len(nums)-1
while l<r:
    m=(l+r)//2
    if nums[m]>nums[m+1]:
        r=m
    else:
        l=m+1
print(l)