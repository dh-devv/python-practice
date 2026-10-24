# list 와 tuple

# mutable ( 변할 수 있는 ) : list
# immutable ( 변할 수 없는 ) : tuple


data_list1 = [1, 2, 3]
data_list2 = data_list1  # 데이터를 공유함

data_list1.append(4)

print(data_list1)  # 공유하기에 2 에 추가했지만 1 에도 추가됨

print('-' * 60)
print()

# ----------------------------------------------------------------------------------------------#

# tuple () 소괄호 없이 ,  으로도 만들 수 있다.
data_tuple1 = 1, 2, 3
#print(type(data_tuple1))

data_tuple2 = data_tuple1

data_tuple2 += 4, 5

print(data_tuple1)
print(data_tuple2)  # 기존에 있던 data_tuple2 와 이름은 같지만, 다른 변수

# TypeError: 'tuple' object does not support item assignment
# data_tuple1[1] = 10  -- > tuple 는 수정 x

print('-' * 60)
print()

# -----------------------------------------------------------------------------------------------#
# dict : 한 쌍으로 저장되어 관리한다.

'''
len() 을 사용하면 한 쌍을 1로 카운트한다.
키 값은 중복될 수 없다. but 값은 중복이 가능하다.
키 값을 주면 그 키의 짝꿍 값을 가지고 온다.
'''

# 구조
#  dict명 = { 키 : 값, 키 : 값 }

# 분리
'''
1. 키 분리
  list(dict명.keys())

2. 값 분리
  dict명.valuse()
'''

food = {"짜장면" : 1500., "짬뽕" : 2500 }

print(len(food))
print(food["짜장면"]) # 짜장면 ( key ) 의 값 (value) 출력

if "짜장면" in food:
    food["짜장면"] = 4000
print(food)

if "탕수육" not in food:
    food["탕수육"] = 9000
print(food)

del food["짬뽕"]
print(food)

for name in food.keys() : 
    print(name)

for i in range(len(food)) :
    print(i+1 , ". " ,list(food.keys())[i])

total = 0
for i in food.values() : 
    total += i

avg = total / len(food)
print("평균 가격: ", total ,"원")

# ------------------------------------------------------------------------------------------------#
print('-' * 60)
print()

 # 등급을 입력받아 학점을 출력하는 프로그램

'''
1 ~ 5  등급이 있고, A ~ E 학점이 있다.
'''

score = { 1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E"}

user_input = int(input("당신의 등급을 입력하세요: "))

if user_input not in score :
    print("당신은 낙제 또는 입력 오류입니다.")
else:
    print(f"{user_input} 등급은 {score[user_input]} 학점입니다.")
