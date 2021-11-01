def merge(l1,l2):
    l1.extend(l2)
    l1.sort()
    return l1
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print(merge(l1,l2))
