l=list(map(int,input().split()))
target=int(input())
if target not in l:
    l.append(target)
l=sorted(l)
if target in l:
    print(l.index(target))
