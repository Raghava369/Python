n=int(input())
for i in range(1,n+1):
    s=65
    for j in range(1,i+1):
        print(chr(s),end=' ')
        s+=1
    print(end="\n")
