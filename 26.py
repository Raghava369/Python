tf=open("temperatures.txt",'r')
l=tf.readlines()
print(l)
nf=open("farranheat.txt",'w')
for i in range(len(l)):
    t=int(l[i])
    f=(t*9/5)+32
    print(f,end="\n",file=nf)
nf.close()
    
               
               
