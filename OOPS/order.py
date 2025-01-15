class order():
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, o2):
        if (self.price > o2.price):
            return True
        else:
            return False
    
o1 = order("Tomato", 60)
o2 = order("Onion", 80)
print(o1<o2)