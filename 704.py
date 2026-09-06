#704 binary search
nums = [-1,0,3,5,9,12]
left=0 
target=9
right=len(nums)-1
while left<right:
    mid=(left+right)//2
    if target==nums[mid]:
        print("element found at index:",mid)
        break
    elif target<nums[mid]:
        right=mid-1
    else:
        left=mid+1
else:
    print("target not found")