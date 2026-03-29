##파이썬 여러 함수 학습 ##

## 숫자를 입력받아 최댓값과 최솟값, 평균을 구하는 프로그램 ##
nums = []  # 숫자 저장


print("-1 입력시 프로그램이 종료됩니다.")
# 1. 숫자 입력받기
while True:
    num = int(input("숫자를 입력하세요: "))

    # 숫자를 그만 입력받기
    if num == -1:
        break
    # 입력받은 숫자를 저장하기
    else:
        nums.append(num)
if len(nums) == 0:
    print("아무 숫자도 입력되지않음, 프로그램을 종료합니다.")
else:
    ## 2. 저장된 숫자 중에서 최댓값,최솟값,평균 을 출력하기
    print(f"최댓값: {max(nums)}/ 최솟값: {min(nums)}/ 평균: {sum(nums)/len(nums)}")
