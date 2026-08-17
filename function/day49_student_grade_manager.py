
## 학생 관리 프로그램 V2

# 학생 한 명의 정보를 저장하고 처리하는 클래스
class Student:

    # 모든 학생에게 공통으로 사용하는 과목 목록
    subjects = ["국어", "수학", "영어"]

    # 학생 객체가 만들어질 때 실행되는 함수
    def __init__(self, name, scores):
        # 학생의 이름을 객체 안에 저장
        self.name = name

        # 학생의 점수 목록을 객체 안에 저장
        self.scores = scores

    # 학생의 평균 점수를 계산하는 함수
    def calculate_average(self):
        # 점수의 합을 점수 개수로 나눔
        return sum(self.scores) / len(self.scores)

    # 점수를 등급으로 바꾸는 함수
    @staticmethod
    def calculate_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    # 학생의 이름, 과목별 점수, 등급, 평균을 출력하는 함수
    def print_result(self):
        print(f"\n이름: {self.name}")

        # 과목과 점수를 하나씩 꺼내서 처리
        for subject, score in zip(self.subjects, self.scores):
            grade = self.calculate_grade(score)
            print(f"{subject} 점수: {score}, 등급: {grade}")

        # 평균 점수 계산
        average = self.calculate_average()
        print(f"평균 점수: {average:.1f}")
        print("-" * 20)

    # 학생의 등급만 출력하는 함수
    def print_grades(self):
        print(f"\n{self.name}님의 등급")

        # 각 과목의 점수를 등급으로 바꾸어 출력
        for subject, score in zip(self.subjects, self.scores):
            grade = self.calculate_grade(score)
            print(f"{subject}: {grade}")

        print("-" * 20)


# 점수를 입력받는 함수
def input_score(subject):
    # 올바른 점수가 입력될 때까지 반복
    while True:
        try:
            # 입력받은 문자열을 정수로 변환
            score = int(input(f"{subject} 점수를 입력하세요: "))

            # 점수가 0점 이상 100점 이하인지 확인
            if 0 <= score <= 100:
                # return은 점수를 돌려주고 이 함수를 종료함
                return score

            print("점수는 0점부터 100점 사이로 입력하세요.")

        # 숫자가 아닌 값을 입력했을 때 발생하는 오류 처리
        except ValueError:
            print("점수는 숫자로 입력하세요.")


# 학생 이름과 점수를 입력받아 Student 객체를 만드는 함수
def input_student_info():
    # 이름 입력
    name = input("이름을 입력하세요: ").strip()

    # 이름이 비어 있으면 다시 입력받음
    while not name:
        print("이름을 입력해야 합니다.")
        name = input("이름을 입력하세요: ").strip()

    # 점수를 저장할 빈 리스트
    scores = []

    # 국어, 수학, 영어 점수를 차례대로 입력받음
    for subject in Student.subjects:
        score = input_score(subject)
        scores.append(score)

    # 입력받은 이름과 점수로 학생 객체를 만들어 반환
    return Student(name, scores)


# 학생 목록에서 이름이 일치하는 학생을 찾는 함수
def find_student(students, name):
    # students 리스트에서 학생 객체를 하나씩 확인
    for student in students:

        # 이름이 일치하면 해당 학생 객체를 반환
        if student.name == name:
            return student

    # 끝까지 찾지 못하면 None을 반환
    return None


# 프로그램의 전체 흐름을 담당하는 함수
def main():
    # 여러 학생 객체를 저장할 리스트
    students = []

    # 메뉴를 계속 보여주기 위한 반복문
    while True:
        print("\n1. 학생 성적 입력")
        print("2. 평균 구하기")
        print("3. 학생 정보 출력하기")
        print("4. 등급 구하기")
        print("5. 프로그램 종료")

        try:
            # 메뉴 번호를 문자열로 입력받음
            user_input = input("메뉴를 선택하세요 (1~5): ").strip()

        # 사용자가 Ctrl+C를 누르면 프로그램 종료
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            break

        # 학생 성적 입력
        if user_input == "1":
            student = input_student_info()

            # 같은 이름의 학생이 이미 있는지 확인
            if find_student(students, student.name) is not None:
                print("이미 등록된 이름입니다.")
            else:
                # 학생 객체를 리스트에 추가
                students.append(student)
                print(f"{student.name} 학생의 정보가 저장되었습니다.")

        # 평균 구하기
        elif user_input == "2":
            if not students:
                print("등록된 학생이 없습니다.")
                continue

            name = input("평균을 확인할 학생 이름: ").strip()
            student = find_student(students, name)

            if student is None:
                print("존재하지 않는 학생입니다.")
            else:
                average = student.calculate_average()
                print(f"{student.name}님의 평균 점수: {average:.1f}")

        # 학생 전체 정보 출력
        elif user_input == "3":
            if not students:
                print("등록된 학생이 없습니다.")
                continue

            name = input("정보를 확인할 학생 이름: ").strip()
            student = find_student(students, name)

            if student is None:
                print("존재하지 않는 학생입니다.")
            else:
                student.print_result()

        # 학생 등급 출력
        elif user_input == "4":
            if not students:
                print("등록된 학생이 없습니다.")
                continue

            name = input("등급을 확인할 학생 이름: ").strip()
            student = find_student(students, name)

            if student is None:
                print("존재하지 않는 학생입니다.")
            else:
                student.print_grades()

        # 프로그램 종료
        elif user_input == "5":
            print("프로그램을 종료합니다.")

            # while True 반복문을 탈출
            break

        # 1~5 이외의 값을 입력했을 때
        else:
            print("1부터 5 사이의 메뉴를 선택하세요.")


# 이 파일을 직접 실행했을 때만 main() 실행
if __name__ == "__main__":
    main()