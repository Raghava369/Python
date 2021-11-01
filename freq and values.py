nums=list(map(int,input().split()))
l=[]
for i in range(0,len(nums),2):
    r=[nums[i+1]]*nums[i]
    l.extend(r)
        

print(l)
    
