class product:
    def __init__(self,name,items,price):
        self.name=name
        self.items=items
        self.price=price
    def get_price(self,n):
        if(n<10):
            cost=n*self.price
            print("actual cost is",cost,"rupees")
            print("10% discount on purchasing more than 9 items")
            print("20% discount on purchasing more than 99 items")
        elif(n<100):
            discount=(10*(n*self.price))/100
            print("actual cost is ",n*self.price)
            print("discount is ",discount)
            print("final cost is",n*self.price -discount)
            print("20% dicount on purchasing more than 99 items")
        elif(n>99):
            discount=(20*(n*self.price))/100
            print("actual cost is ",n*self.price)
            print("discount is ",discount)
            print("final cost is",n*self.price -discount)
    def my_purchase(self,n):
         if(n<10):
            cost=n*self.price
            print("actual cost is",cost,"rupees")
         elif(n<100):
             discount=(10*(n*self.price))/100
             print("actual cost is ",n*self.price)
             print("discount is ",discount)
             print("final cost is",n*self.price -discount)
         elif(n>99 and n<=200):
             discount=(20*(n*self.price))/100
             print("actual cost is ",n*self.price)
             print("discount is ",discount)
             print("final cost is",n*self.price -discount)
         else:
             print("available 200")
            
p=product("pen",200,5)
n=int(input("enter number of pens you want to buy"))
p.get_price(n)
n=int(input("enter number of pens you want to buy"))
p.my_purchase(n)


      







            
            
        
