```python
servers = {} # 서버의 이름과 cpu 사용량을 담을 공간 #

while True:
  server = input("서버 이름: ") # 서버 이름 입력받기

    ## 입력을 종료하는 로직 ##
  if '종료' in server:
    break

  cpu_input = input("cpu 사용량: ") # 해당 서버의 cpu 사용량 입력받기

    ## 입력을 종료하는 로직 ##
  if '종료' in cpu_input:
    break

  cpu = int(cpu_input)
  servers[server] = cpu  # 서버 값에 cpu 사용량 넣기
  print()

print(f" 총 {len(servers)} 대의 서버가 등록되었습니다.")

## cpu 사용량에 따른 해당 서버의 과부화 여부 출력 ##
print()
for name, usage in servers.items():
  if usage >= 80:
    print(f"경고! {name} 서버 과부화 상태 !")
  else:
    print(f"{name} 서버 정상 상태")
```
