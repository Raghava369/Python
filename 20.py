def is_sorted(l):
    a=sorted(l)
    b=a[::-1]
    if l==a or l==b:
        return True
    return False
l=list(map(int,input().split()))
print(is_sorted(l))
    
