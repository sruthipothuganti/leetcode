class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        ans=True
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()!=s[r].lower():
                ans=False
                break
            else:
                l+=1
                r-=1
        return ans