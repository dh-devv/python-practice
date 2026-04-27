 ```python    ## 영단어를 맞추는 프로그램 ##


# 단어를 저장해둔 딕셔너리 #
voca_dict = {
    "구조" : "structure",
    "관리자" : "admin",
    "상태" : "status"
}
score = 0  # 맞춘 영단어의 개수 
print("복습을 시작합니다.")

for korean , english in voca_dict.items():
   # 유저에게 입력받기
  user = input(f"{korean} 의 영단어를 입력하세요: ") 
   
   # 정답일 경우 #
  if user == english:
    print("정답입니다.")
    print()
    score += 1

   # 정답이 아닐 경우 #
  else:
    print(f"아쉽네요, 정답은 {english} 입니다.")
    print()

# 프로그램이 끝났을 때 출력 #
print(f"지금까지 총 {score} 개의 문제를 맞췄습니다.")
```
