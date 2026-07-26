# 파일 입출력 연습

# 절대 경로: 내 위치가 어디든 찾아갈 수 있다. ( cd /etc/NetworkManager )
# 상대 경로:  내 위치에 따라 경로가 변한다. ( cd etc/NetworkManager )

# . : 현재 위치
# .. : 이전 폴더

'''
name_file = open("names.txt", "w")
name_file.write("변동헌")
name_file.close()
'''

name_file = open("names.txt", "r")
for i in name_file.readlines():
    print(i)
    
name_file.close()