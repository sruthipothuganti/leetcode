nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
a=[]
for i in nums2:
    if i not in a and i in nums1:
        a.append(i)
print(a)
