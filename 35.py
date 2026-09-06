#search inserted position
nums = [1,3,6]
target = 5
left=0
right=len(nums)-1
while left<right:
    mid=(left+right)//2
    if target==nums[mid]:
        print(mid)
        break
    elif target<nums[mid]:
        right-=1
    else:
        left+=1
else:
    print(left)
