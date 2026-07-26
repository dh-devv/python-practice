# 클래스 상속 실습

class A:
    def __init__(self, data = 10) :
        self.data = data
        print("부모 생성자 호출")

    def printData(self) :
        print(self.data)

    def show(self) :
        print("부모 메소드")

class B(A):
    #pass
    def __init__(self, data, data2):
        #A.__init__(self, data)
        super().__init__(data)

        #self.data = data
        self.data2 = data2

    def printData2(self) :
        print(self.data, self.data2)


    # Overriding ( 재정의 )
    def printData(self):  # 부모 클래스의 메소드와 이름이 같아야 함
        print(self.data, self.data2)

'''
b = B()  # 상속을 받았기에 A로 접근 가능
b.printData()  # 부모 필드에 접근함
b.show()
'''

b = B(30, 20)
b.printData2()
b.printData()
