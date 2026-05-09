## AI 의 도움을 받아서 딕셔너리와 튜플의 실전 활용법을 학습함. ##
```python
# 튜플: 관리자 
admin_info = ('홍길동', '010-1234-5678')

# 딕셔너리: 서버 상태 관리
server_status = {
    "web_server" : "online",
    "DB_server" : "offline",
    "cloud_node" : "online"
}

# 세트 : 사용중인 os 종류 (중복 제거)
os_list = ['ubuntu','windows','ubuntu','centOS','windows']
unique_os = set(os_list)


# 확인하기
print(f"  관리자: {admin_info[0]}, {(admin_info[1])}")
print(f"현재 서버 상태 : {server_status}")
print(f"설치된 os 종류: {unique_os}")

if server_status['DB_server'] == "offline":
    print("-"*60)
    print("경고, DB 서버가 꺼져있습니다. 확인필요.")
```
