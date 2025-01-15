class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show(self):
        print(self.real, "+", self.img, "i")
        
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        print("The sum is: ", end="")
        return complex(newReal, newImg)
    
c1 = complex(1,5)
c1.show()
c2 = complex(6,4)
c2.show()

c3 = c1 + c2
c3.show()
