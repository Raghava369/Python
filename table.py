n=int(input("enter a number"))
s=int(input("enter a starting point"))
e=int(input("enter a end point"))
ans=n*s
if s<e:
    for i in range(s,e+1):
        print(n,'x',i,'=',ans)
        ans=ans+n
elif e<s:
        for i in range(s,e-1,-1):
            print(n,'x',i,'=',ans)
            ans=ans-n
            
        
