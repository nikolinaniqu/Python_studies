import abc

class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @abc.abstractmethod
    def tax(self):
        pass
    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")

class Shoes(Product):
    def tax(self):
        return self.price*1.2
p=Shoes("Nike Airmax",100)
p.buy()

class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @abc.abstractmethod
    def tax(self):
        pass
    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")

class Shoes(Product):
    def tax(self):
        return self.price*1.2
p=Shoes("Nike Airmax",100)
p.buy()
