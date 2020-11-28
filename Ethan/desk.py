class Desk:
    def __init__(self,color,price=423):
        self.color=color
        self.price=price
    def __repr__(self):
        return f"{self.color}(${self.price})"


    def say_hi(self):
        print("Hi, I am a desk")

if __name__ == '__main__':
    x = Desk('color')
   
    x.say_hi()

p=Desk("My price is:",  423)


print("My color is: Brown")

print(p)
print("Please buy me!")