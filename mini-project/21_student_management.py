# dict 와 list 활용 연습하기
'''
num_dict = {"even" : [2, 4, 6] , "odd": [1, 3, 5]}

for i in num_dict["even"]:
    print(i)

    '''

# 학생 관리 프로그램

title = "학생 성적 관리 프로그램"
errermsg = "다시 시도해주세요"
msg = " 1. 추가\n 2. 수정\n 3. 삭제\n 4. 목록\n 5. 나가기"

student_dict = {}  # DB
subject_list = ["국어", "영어", "수학"]  # 과목의 종류

while True :
    choice = int(input(title + "\n" + msg + "\n"))

        ## 추가하기 ## 
    if choice == 1 :
        name = input("학생 이름: ")

        if name not in student_dict :
            scores = input("과목별 점수 입력(80, 20, 40): ").split(',')
            student_dict[name] = [int(score) for score in scores]
        else:
            print("이미 등록된 학생입니다.")   # 이미 있는 학생

        print(student_dict)  # 추가된 DB 보여주기


        ## 수정하기 ##
    elif choice == 2 :
        choice = int(input(" 1. 학생명\n 2. 점수\n"))

        if choice == 1:
            name = input("수정할 학생의 이름: ")

            if name in student_dict :
                new = input("새로운 학생명: ")
                score_list = student_dict[name]

                del student_dict[name]
                student_dict[new] = score_list

                print("수정완료")
            else:
                print("존재하지 않는 학생입니다.")

        elif choice == 2:
            name = input("수정할 학생의 이름: ")
            choice = int(input(" 1. 국어점수 \n 2. 영어점수 \n 3. 수학점수\n"))

            if name in student_dict :
                student_dict[name][choice - 1] = int(input("새로운 점수: "))
            else:
                print("존재하지 않는 학생입니다.")

    elif choice == 3 :
        name = input("삭제할 학생이름: ")

        if name in student_dict :
            del student_dict[name]
        else:
            print("존재하지 않는 학생입니다.")

    elif choice == 4 :
        for key in student_dict.keys() :
            print("[" + key + "]")
            cnt = 0

            for value in student_dict[key] :
                print(subject_list[cnt] + ":" + str(value) + "점")
                cnt += 1

    elif choice == 5 :
        break

    else:
        print(errermsg)