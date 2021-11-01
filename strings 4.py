n=input()
if(len(n)%2==0):
    if(n[:len(n)//2]==n[len(n)//2:]):
        print('True')
    else:
        print("False")
elif(len(n)%2!=0):
    if(n[:len(n)//2]==n[len(n)//2 +1:]):
        print("True")
    else:
        print("False")

