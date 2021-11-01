email="raghavakovvuri@gmail.com"
pwd="password"
mid=input("enter mail")
password=input("enter password")
if(mid==email):
    if(password==pwd):
        print("login successfully")
    else:
        print("password is incorrect")
else:
    print("email is invalid")
