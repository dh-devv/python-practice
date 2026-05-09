## set 학습하기 ##

Primes = {2,3,5,7,11,13,17,19} # 소수
odds = {1,3,5,7,9,11,13,15,17,19} # 홀수
print(Primes & odds) # 소수 집합과 홀수 집합의 교집합 출력

evens = {2,4,6,8,10,12,14,16,18} # 짝수
print(Primes | evens) # 짝수 집합과 소수 집합의 합집합 출력

print(Primes - odds) # 소수 집합과 홀수 집합의 차집합 출력
print(odds - Primes) # 홀수 집합 과 소수 집합의 차집합 출력
