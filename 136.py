#136
a=[2,2,1,1,4,5]
dici={}
for i in a:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
for key,value in dici.items():
    if value==1:
        print(key)