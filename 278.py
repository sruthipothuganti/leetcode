n = 5
bad = 4
def isBadVersion(version):
    return version >= bad

for i in range(1, n + 1):
    if isBadVersion(i):
        print(i)
        break