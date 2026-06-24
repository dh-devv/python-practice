## 학생 성적 관리 프로그램 ##

N = int(input(("학생 수를 입력하세요: ")))

class Student:
    def __init__(self, name, kor, eng, math):  # 이름, 국영수 점수 입력 받기
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total_score(self):
        return self.kor + self.eng + self.math     # 총합 점수 계산

    def average_score(self):
        return self.total_score() / 3   # 전체 평균 점수 계산


    def __str__(self):  # 학생 정보 출력
        return f"이름: {self.name} /  국어: {self.kor} /  영어: {self.eng} /  수학: {self.math} \n 총점: {self.total_score()} /  평균: {round(self.average_score(), 2)}"


 ## 학생 정보 입력 ##
students = []

for i in range(N):
    name = input(f"학생 {i + 1}의 이름을 입력하세요: ")
    kor = int(input(f"학생 {i + 1}의 국어 점수를 입력하세요: "))
    eng = int(input(f"학생 {i + 1}의 영어 점수를 입력하세요: "))
    math = int(input(f"학생 {i + 1}의 수학 점수를 입력하세요: "))
    
    student = Student(name, kor, eng, math)
    students.append(student)

print('-' * 60)

math_cut = int(input("수학과목의 1등급 컷을 정수로 말하시오: "))
kor_cut= int(input("국어과목의 1등급 컷을 정수로 말하시오: "))
eng_cut = int(input("영어과목의 1등급 컷을 정수로 말하시오: "))


## 학생 정보 출력 ##
print("\n학생 성적 정보:")
print("-" * 60)

for student in students:
    print(student)
    print()

    if student.math >= math_cut:
        print(f"수학 1등급: {student.name}")
    else:
        print("수학 1등급이 아닙니다.")

    if student.kor >= kor_cut:
        print(f"국어 1등급: {student.name}")
    else:
        print("국어 1등급이 아닙니다.")

    if student.eng >= eng_cut:
        print(f"영어 1등급: {student.name}")
    else:
        print("영어 1등급이 아닙니다.")
    
    print("-" * 60)
