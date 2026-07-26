# 클래스 예제

class A :
    data = 10

    def printData(self):
        print(self)
        print(self.data)

    def intro():
        print("난 A 클래스이다.")

obj1 = A()
obj2 = A()

obj1.data = 20
print(obj1)   # 메모리에 할당된 주소값 가져오기
obj1.printData()
print(obj2)
obj2.printData()
A.intro()

# 자동차 클래스 만들기

class Car:

    # 전역 변수 ( 여러 메소드에서 공유할 변수들)
    brand = ""
    color = ""
    price = 0

    def __init__(self, brand = "", color = "", price = 0) : # 생성자
        # 해당 필드의 객체에 알맞게 초기화
        self.brand = brand
        self.color = color
        self.price = price

    def engineStart(self) :
        print( self.brand + " 시동 켰음")

    def engineStop(self) :
        print( self.brand + " 시동 껐음")

momCar = Car("Benz", "Yellow", 35000)
dadyCar = Car("BMW", "BLUE", 15000)
myCar = Car()

# 불편함
'''
momCar.brand = "Benz"
momCar.color = "Yellow"
momCar.price = 35000
'''

momCar.engineStart()
dadyCar.engineStop()