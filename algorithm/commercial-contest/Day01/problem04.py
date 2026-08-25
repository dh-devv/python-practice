# 4번: 반별 총점 구하기

user_input = input() # 일단 입력받기

class1, class2, class3 = user_input.split('/') # '/' 기준으로 나누기

school = [class1, class2, class3] # 리스트로 만들기
School = []
Scores = []

#school.remove(':')

# print(school)  --> 반이랑 점수랑 같이 저장됨

for i in school:
    class_name, scores = i.split(':')

    School.append(class_name)
    score_list = list(scores.split(' '))  # 점수를 리스트로 저장하기

    for j in score_list:
        if j != '':
            Scores.append(int(j))
    School.append(Scores)
    Scores = [] # 초기화

#print(School)
#classNumber = 1

'''
for i in range(3):
    print(f"{classNumber}반 총점: {sum(School[i])}")  # 아니 여기서 왜 오류가 뜨는거지???
    classNumber += 1
'''

cnt = 1
for i in range(0, 6, 2):
    if cnt == 3:
        print(f"{School[i]} 총점: {sum(School[i+1])}")  # School[i]는 반 이름, School[i+1]은 점수 리스트 
    else:
        print(f"{School[i]} 총점: {sum(School[i+1])}",end=' /')  # School[i]는 반 이름, School[i+1]은 점수 리스트
    cnt += 1
