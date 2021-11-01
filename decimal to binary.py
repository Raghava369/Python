def decToBinary(n):
    s=""
    while(n!=0):
          rem=n%2
          s=str(rem)+ s
          n=n//2
    if(len(s)>=4):
        print(s[len(s)-4])
    else:
        print(0)
    

        
        
