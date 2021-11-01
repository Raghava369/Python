####try:
####    a=10
####    b=10
####    print(a+b+c)
####except:
####    print("done")
##try:
##    a=10
##    b=20
##    print(a+b+c)
##    print(a/0)
##except ZeroDivisionError:
##    print('cannot divide with zero')
##except NameError:
##    print("name issue,avoid")
##finally:
##    print("done")
try:
    a=20
    if a<15:
        raise ValueError("give more than 15")
    else:
        print("payment can be done")
except ValueError as error:
    print(error)
        
