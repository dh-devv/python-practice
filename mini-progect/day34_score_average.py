class School:
    def __init__(self, school_name):
        self.school_name = school_name

        self.class_1 = []
        self.class_2 = []
        self.class_3 = []

        self.score_1 = []
        self.score_2 = []
        self.score_3 = []

    def first_grade(self, student_class, score):
        self.class_1.append(student_class)
        self.score_1.append(score)

    def second_grade(self, student_class, score):
        self.class_2.append(student_class)
        self.score_2.append(score)

    def third_grade(self, student_class, score):
        self.class_3.append(student_class)
        self.score_3.append(score)

    def average(self, scores):
        if len(scores) == 0:
            return 0
        return sum(scores) / len(scores)

    def __str__(self):
        return f"학교 이름: {self.school_name}, 1학년 평균: {self.average(self.score_1)}, 2학년 평균: {self.average(self.score_2)}, 3학년 평균: {self.average(self.score_3)}"

    school = School("부산 컴퓨터과학고등학교")

    school.first_grade("1반", 80)
    school.first_grade("2반", 90)

    school.second_grade("1반", 75)

    school.third_grade("3반", 88)

    print(school)