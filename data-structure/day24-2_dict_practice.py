## 딕셔너리 공부하기 ##

# 1. 딕셔너리 생성
fruits = {"red":"apple", "blue":"blueberry", "yellow":"banana"}
print(fruits)

# 2. red 키에 든 사과를 키위로 바꾸기
fruits['red'] = "kiwi"
print(fruits)

print(fruits['red'])  # 딕셔너리에서 red 키에 해당하는 부분만 출력하기

# 3. 새로운 키를 딕셔너리에 추가하기
fruits['green'] = "green apple"
print(fruits)
