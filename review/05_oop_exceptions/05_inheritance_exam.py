# 클래스 상속 예제


class Car():

    def __init__(self, brand, color, price) :
        self.brand = brand
        self.color = color
        self.price = price

    def engineStart(self):
        print(self.brand + " 시동 켰음")

    def engineStop(self):
        print(self.brand + " 시동 껐음")


class SuperCar(Car) :

    def __init__(self, brand, color, price, mode):
        super().__init__(brand, color, price)
        self.mode = mode

        ## Ovcerriding ##
    def engineStart(self):
        print(self.brand + "음성으로 시동 켰음")

    def openRoof(self):
        print("지붕 열림")

    def closeRoof(self):
        print("지붕 닫힘")

ferrari = SuperCar("ferrari", "red", 35000, "daliy")

ferrari.engineStart()
ferrari.engineStop()
ferrari.openRoof()
ferrari.closeRoof()


print('-' * 60)
print()

# 클래스 변수

class A :
    seq = 0

    def __init__(self) :
        A.seq += 1

        self.num = A.seq

    def test(self):
        self.seq = 10

obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()

obj1.test()
print(obj1.num)
print(obj1.seq)