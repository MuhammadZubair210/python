class Car():
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def getSpeed(self,x):
        if self.brand == x:
             print("if works")
        else:
             print("else works")


