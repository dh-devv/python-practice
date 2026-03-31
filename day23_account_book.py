history = []
money = []

while True:
  user = int(input("1.입력 / 2.내역보기 / 3. 종료 , 중 하나를 선택하세요: "))
  if user == 1:
    name = input("물건의 이름을 입력하세요: ")
    mo = int(input("물건의 금액을 입력하세요: "))
    history.append(name)
    money.append(mo)
    print()

  elif user == 2:
    for i in range(len(history)):
      print(f"구매한 물건: {history[i]}, 금액: {money[i]}")
    print()

  elif user == 3:
      break
  else:
    print("1~3 까지의 수를 입력하지 않았습니다.")
    
