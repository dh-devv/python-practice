class Linux:

    def __init__(self, user_id, pw):
        self.id = user_id
        self.pw = pw
        self.current_directory = "/home/user"
        self.folders = []
        self.user_login = False
        self.files = []




    def login(self, user_id, pw):
        if self.id == user_id and self.pw == pw:
            print("로그인 성공!")
            self.user_login = True
        else:
            print("로그인 실패! 아이디 또는 비밀번호가 틀렸습니다.")



    def ls(self):
        print("현재 디렉터리의 파일 목록을 보여줍니다.")
        print()

        print("폴더: ")
        print(self.folders)

        print()
        print("파일: ")
        print(self.files)



    def pwd(self):
        print("현재 내 위치를 보여줍니다.")
        print(self.current_directory)



    def mkdir(self):
        print("새 디렉터리를 생성합니다.")
        folder_name = input("폴더 이름: ")
        self.folders.append(folder_name)



    def touch(self):
        print("새 파일을 생성합니다.")
        file_name = input("파일 이름: ")
        self.files.append(file_name)



    def terminal(self):
        if not self.user_login:
            print("먼저 로그인해주세요.")
            return
        commands = {
            "ls" : self.ls,
            "pwd": self.pwd,
            "mkdir" : self.mkdir,
            "touch" : self.touch
        }

        while True:
            user_input = input("user#linux:$ ")

            if user_input == "exit":
                print("터미널 종료")
                break

            elif user_input in commands:
                commands[user_input]()

            else:
                print("알 수 없는 명령어입니다.")


    def __str__(self):
        return f"아이디: {self.id} / 현재 디렉토리: {self.current_directory} / 폴더 목록: {self.folders} / 파일 목록: {self.files}"
## 객체 ##
user = Linux("Ubuntu", "password123")
user.login("Ubuntu", "password123")

user.terminal()
print(user)
