#maxi avg subarray-leetcode 643
nums = [1,12,-5,-6,50,3]
k = 4
left=0
right=0
s=0
m=float("-inf")
while(right<len(nums)):
    s=s+nums[right]
    if right-left+1==k:
        a=s/k
        m=max(m,a)
        s=s-nums[left]
        left+=1
    right+=1
print(m)

