class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[]
        for i in num:
            while s and k>0 and s[-1]>i:
                s.pop()
                k-=1
            s.append(i)
        while k>0:
            s.pop()
            k-=1
        res= "".join(s).lstrip("0")
        if res:
            return res
        else:
            return "0"