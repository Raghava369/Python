n=input()
for i in range(len(n)):
    if n[i] in "aeiouAEIOU":
        n=n.replace(n[i],"_")
print(n)
        

