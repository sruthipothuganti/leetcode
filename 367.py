def isPerfectSquare(self, n: int) -> bool:
        l=0
        r=n
        while l<=r:
            m=(l+r)//2
            sq=m*m
            if sq==n:
                return True
            elif sq<n:
                l=m+1
            else:
                r=m-1
        return False 