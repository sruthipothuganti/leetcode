nums = [0,1,0,3,8]
a=[]
for i in range(len(nums)):
    if nums[i]!=0:
        a.append(nums[i])
while len(a)<len(nums):
    a.append(0)
print(a)
#or 
nums = [0,1,0,3,8]
j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        j+=1
print(nums)
