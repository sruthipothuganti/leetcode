class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        res=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<len(nums1):
            res.append(nums1[i])
            i+=1
        while j<len(nums2):
            res.append(nums2[j])
            j+=1
        n=len(res)
        if n%2==1:
            return res[n//2]
        mid=n//2
        return (res[mid-1]+res[mid])/2
obj=Solution()
nums1=[1,3]
nums2=[2]
ans=obj.findMedianSortedArrays(nums1,nums2)
print(ans)




        