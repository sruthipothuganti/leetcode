nums = [-4,-1,0,3,10]
a=[]
for i in range(len(nums)):
    a.append(nums[i]*nums[i])
a.sort()
print(a)
