#python script for grade calculation
def grade():
    m=int(input("enter marks"))
    if m>=80 and m<=100:
        print("A Grade")
    elif m>=60 and m<80:
        print("B Grade")
    elif m>=40 and m<60:
        print("C Grade")
    elif m>=0 and m<40:
        print("fail")
    else:
        print("invalid marks")
     
          
