class Point():
    def __init__(self, x, y):   # 입력받은 값을 각각 x, y에 저장
        self.x = x
        self.y = y
    
    def origin(self):           # 원점과의 거리를 계산하기
        return (self.x**2 + self.y**2)**0.5

    def distance(self, other):   # 다른 점과 점 사이의 거리를 계산하기
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return (x_diff**2 + y_diff**2)**0.5

    def __add__(self, other):   # 두 점의 좌표를 더해서 새로운 점 만들기 ( 다시 __init__ 실행)
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y) # 새로운 점

   ## 새로운 클래스 등장 ##
class Circle():
    def __init__(self, c ,r):    # 중심은 이미 Point 클래스에서 만들어짐, 반지름은 객체에서 p1, 뒤에 오는 값
        self.center = c 
        self.radius = r

    def area(self):    # 원의 넓이 계산하기
        return (3.14 * self.radius**2)

    def distance(self, other):    # 원의 중심과 다른 점 사이의 거리 계산하기
        return self.center.distance(other)

    def include(self, other):   # 다른 한 점이 어디에 위치하는 지 판단하기 ( 원 안: 1, 원 위: 0, 원 밖: -1)
        if self.distance(other) < self.radius:
            return 1
        elif self.distance(other) == self.radius:
            return 0
        else:
            return -1

    def __str__(self):   # 원의 중심의 좌표를 각각의 변수에 저장하고, 출력하기
        x = self.center.x
        y = self.center.y
        r = self.radius
        return f"중심: ({x}, {y}), 반지름: {r}"

p1 = Point(3, 4)  # 원의 중심
p2 = Point(7, 8)  # 다른 한 점 ( 원의 중심과의 거리, 위치 등을 구할 때, 사용)
C1 = Circle(p1, 3)  # 원의 중심과 반지름

print(C1.area())  # 넓이 구하는 메서드 실행
print(C1.distance(p2))  # 원의 중심과 다른 한 점 사이의 거리 계산하는 메서드 행
print(C1.include(p2))   # 다른 한 점의 위치 판단하는 메서드 실행
print(C1)  # 중심과 반지름 출력하기

