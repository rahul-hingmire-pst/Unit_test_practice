class Checkout:
    class Discount:
        def __init__(self,noitems,price):
            self.noitems =noitems
            self.price = price
        
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items  = {}
        
    def adddiscount(self,item ,noofitems, price):
        discount = self.Discount(noofitems,price)
        self.discounts[item] = discount

    def additemprice(self,item,price):
        self.prices[item] = price
    
    def additem(self, item):
        if item in self.items:
           self.items[item] += 1
        else:
            self.items[item] = 1

    def calculatetotal(self):
        total = 0
        for item, cnt in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if cnt >= discount.noitems:
                    noofitems = cnt // discount.noitems  # 3 // 2 
                    total += noofitems * discount.price  
                    remaining = cnt % discount.noitems
                    total += remaining * self.prices[item]
                else:
                    total += self.prices[item] * cnt
            else:
                total += self.prices[item] * cnt
        return total
    
    

