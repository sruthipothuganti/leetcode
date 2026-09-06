a="acb"
t="ahbgdc"
j=0
for i in range(len(t)):
    if j<len(a) and a[j]==t[i]:
        j+=1
if j==3:
    print("True")
else:
    print("False")
    