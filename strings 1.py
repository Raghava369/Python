n=input()
sums=0
for i in range(len(n)):
    if n[i] in "123456789":
        s=int(n[i])
        sums=sums+s
print(sums)
