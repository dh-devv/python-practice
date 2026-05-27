class Linux():

    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        self.current_directory = "/home/user"
        self.folders = []
        self.user_login = False




    def login(self, id, pw):
        if self.id == id and self.pw == pw:
            print("로그인 성공!")
            self.user_login = True
        else:
            print("로그인 실패! 아이디 또는 비밀번호가 틀렸습니다.")




    def terminal(self, command):
        if not self.user_login:
            print("먼저 로그인해주세요.")
            return

        if command == "ls":
            print("현재 디렉토리의 파일 목록을 보여줍니다.")

            print(self.folders)

        elif command == "cd":
            print("디렉토리를 변경합니다.")

        elif command == "mkdir":
            print("새 디렉토리를 생성합니다.")

            folder_name = input("폴더 이름: ")
            self.folders.append(folder_name)

        elif command == "pwd":
            print(self.current_directory)

        else:
            print("알 수 없는 명령어입니다.")

    def __str__(self):
        return f"아이디: {self.id} / 현재 디렉토리: {self.current_directory} / 폴더 목록: {self.folders}"
## 객체 ##
user = Linux("Ubuntu", "password123")
user.login("Ubuntu", "password123")

user.terminal("pwd")
print()
user.terminal("mkdir")
print()
user.terminal("ls")
print()
print(user)
