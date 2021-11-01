prices=list(map(int,input().split()))
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if(prices[i]>=prices[j]):
            prices[i]=prices[i]-prices[j]
            break
            
print(prices)
