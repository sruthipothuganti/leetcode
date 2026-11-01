class Solution:
    def isValid(self, s1: str) -> bool:
        s=[]
        for i in s1:
            if i=="(" or i=="[" or i=="{":
                s.append(i)
            else:
                if len(s)==0:
                    return False
                t=s.pop()
                if i==")" and t!="(":
                    return False
                elif i=="]" and t!="[":
                    return False
                elif i=="}" and t!="{":
                    return False
        return len(s)==0