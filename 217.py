a=[1,2,3,4]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    if value>1:
        print("True")
        break
else:
    print("False")