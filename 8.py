n=str(input("Enter a word :"))
for i in range(0,len(n)):
    if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' ):
        break
    else:
        continue
if(i==len(n)-1):
    print("no vowels")
else:
    print("word contains vowels")
