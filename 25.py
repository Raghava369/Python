nf=open("mail.txt",'r')
s=nf.readlines()
l=''
c=0
for i in s:
    
    if "\n" in i:
        i=i[:len(i)-1]
    if c!=len(s)-1: 
        l=l+i+';'
    else:
        l=l+i+'.'
    c+=1
print(l)
