## 함수를 활용한 성적 처리기 ##
def data(score):

    passed_scores = [i for i in scores if i >= 60]
    passed_scores.sort()

    print(f"상위 3명은 {passed_scores[-3:]}")
scores = [85,92,47,68,95,30,77,82,55,100]
data(scores)
