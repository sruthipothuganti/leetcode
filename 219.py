nums = [1,2,3,1]
k = 3
d={}
for i in range(len(nums)):
    if nums[i] in d:
        if i-d[nums[i]]<=k:
            print("True")
            break
    d[nums[i]]=i
else:
    print("False")