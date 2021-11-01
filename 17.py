def sum_digit(num):
    sum_is=0
    while(num!=0):
        sum_is=sum_is+num%10
        num=num//10
    return sum_is
n=int(input())
print(sum_digit(n))
