nums = [4,5,6,7,0,1,2]
target = 0
l=0
r=len(nums)-1
while l<=r:
    mid=(l+r)//2
    if target==nums[mid]:
        print(mid)
        break
    if nums[l]<=nums[mid]:
        if nums[l]<=target<nums[mid]:
            r=mid-1
        else:
            l=mid+1
    else:
        if nums[l]<=target<nums[mid]:
            l=mid+1
        else:
            r=mid-1
print(-1)
