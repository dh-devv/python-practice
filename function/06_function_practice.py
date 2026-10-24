## 함수 연습하기

### 학생 관리 프로그램

name_list = [] # 이름을 저장할 변수
scores = []  # 점수를 저장할 변수

class Student:
    def __init__(self, name):  # 이름 입력받기 ( 근데 이름은 어디서 쓰는거지? )
        self.name = name

    def calculate_grade(self, score):  # 등급 확인하기
        if score >= 90:
            grade =  'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        return grade


    def calculate_average(self, scores):  # 평균 확인하기
        return sum(scores) // len(scores)

    def print_result(self, name):        # 결과 출력하기
        index = name_list.index(name)
        score = scores[index]
        grade = self.calculate_grade(score)

        print(f"name: {name}")
        print(f"score: {score}")
        print(f"grade: {grade}")
        print("-" * 20)

    def input_student_info(self):         # 학생 정보 입력받기
        global name_list, scores

        name = input("Enter name: ")
        scores = []
        name_list = []

        name_list.append(name)
        for subject in ["Korean", "Math", "English"]:
            score = int(input(f"Enter {subject} score: "))
            scores.append(score)

        return scores, name_list

# 유저 입력을 받는 부분
while True:
    print("1. 학생 성적 입력")
    print("2. 평균 구하기")
    print("3. 해당 학생의 정보 출력하기")
    print("4. 등급 구하기")
    print("5. 프로그램 종료")

    try:
        user_input = input("Enter your choice (1 ~ 4): ")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break

    if user_input == '1':
        Student.input_student_info()

    elif user_input == '2':
        average_score = Student.calculate_average(scores)
        print(f"평균 점수: {average_score}")

    elif user_input == '3':
        name = input("Enter name: ")

        try:
            Student.print_result(name)
        except Exception as e:
            print(f"{e} 존재하지 않는 학생입니다.") 

    elif user_input == '4':
        name = input("Enter name: ")

        try:
            Student.print_result(name)
        except ValueError:
            print(f"존재하지 않는 학생입니다.")

    elif user_input == '5':
        print("프로그램을 종료합니다.")
        break


        
        
