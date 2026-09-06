n=10
pick=6
l=1
r=n
while l<=r:
    m=(l+r)//2
    if m==pick:
        print(m)
        break
    elif m<pick:
        l=m+1
    else:
        r=m-1

