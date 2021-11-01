l=list(map(int,input().split()))
if(l[0]<l[1]):
    n=1
    i=2
elif l[0]>l[1]:
    n=2
    i=2
else:
    i=1
    while(l[0]==l[i] and i<len(l)-1):
        i=i+1
    if(i<len(l)):
        if(l[0]<l[i]):
            n=1
        else:
            n=2
if(n==1):
    j=i
    for k in range(i-1,len(l)-1):
        if(l[k]>l[j]):
            print("False")
            break
        j=j+1
    else:
        print("True")
else:
     j=i
     for k in range(i-1,len(l)-1):
         
         if(l[k]<l[j]):
             print("False")
             break
         j=j+1
     else:
         print("True")
