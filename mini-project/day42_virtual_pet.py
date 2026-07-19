## 동물 키우기 프로그램 ##

class Pet():
    def __init__(self, name):
        self.name = name
        self.hp = 50


        ## 밥 먹기 ##
    def eat(self):
        self.hp += 10
        print(f"{self.name}가 밥을 먹었습니다.")
        print('-' * 60)


        ## 놀기 ##
    def play(self):
        if self.hp == 0 :
            print(f"{self.name} 는 체력이 없습니다.")
        else:
            self.hp -= 20
        
            if self.hp <= 0:
                print(f"{self.name}가 지쳤습니다.")
                print()

            else:
                print("놀이가 끝났습니다.")
       
        print('-' * 60)

        ## 잠 자기 ##
    def sleep(self):
        self.hp += 50
        print(f"{self.name} 가 잠에서 깨어났습니다.")
        print('-' * 60)

        ## 상태 확인하기 ##
    def show_status(self):
        print('-' * 60)
        print(f"이름 : {self.name}")
        print(f"체력 : {self.hp}")
        print('-' * 60)

## 객체 ##
print("(예시)")

if __name__ == "__main__":

    my_pet = Pet("강아지")
    my_pet.show_status() # 초기 상태 확인하기

    print('-' * 20)
    my_pet.eat()  # 밥 먹기
    my_pet.play() # 놀기
    my_pet.play()

    print('-' * 20)
    my_pet.show_status()  # 최종 상태 확인하기

print('-' * 60)

yes_list = ["Y", "y"]
no_list = ["N", "n"]


## 내가 만드는 객체 ##
if __name__ == "__main__":
    try:
        user_input = input("직접 하시겠습니까? (y/n): ")  # 프로그램 실행 여부 묻기

        if user_input in yes_list:  # 실행한다.
        
            pet_name = input("펫 이름을 입력하세요: ")  # 이름 입력하기
            pet = Pet(pet_name)

            print('-' * 60)
            while True: 
                print("-1 을 입력하면 종료됩니다.")  # 게임 플레이
                print()

                print(" 1: 밥 먹기, 2: 놀기, 3: 잠 자기, 4: 상태 확인")
                
               
                choose = input("어떤 것을 하시겠습니까? (1, 2, 3, 4) : ")  # 상호작용

                       ## 종료 ##

                if choose == "-1" :
                    print('-' * 60)
                    break
                
                try:
                    choose = int(choose)

                except ValueError:
                    print("제대로된 입력이 아닙니다.")    
                    continue
                      ## 상호작용 ##

                if choose == 1:
                    pet.eat()

                elif choose == 2:
                    pet.play()
                
                elif choose == 3:
                    pet.sleep()

                elif choose == 4:
                    pet.show_status()
                
                else:
                    print("잘못된 입력입니다.")
                    print('-' * 60)
                    continue


        elif user_input in no_list:  # 실행하지 않는다.
            pass      
        else:
            print("잘못된 입력입니다.")

            ## 프로그램 종료 ##
        print("프로그램을 종료합니다.")

        

    except ValueError:
        print("제대로 된 입력이 아닙니다.")