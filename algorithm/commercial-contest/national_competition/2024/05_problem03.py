# 3번: SNS 비밀번호

N = input()   # password

upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
numbers = [str(i) for i in range(10)]
special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

data = {
    "upper" : False,
    "lower" : False,
    "numbers" : False,
    "special_symbols" : False
}
answer = ''

for i in N:
    if i in upper:
        data["upper"] = True
    elif i in lower:
        data["lower"] = True
    elif i in numbers:
        data["numbers"] = True
    elif i in special_symbols:
        data["special_symbols"] = True

goodList = []
badList = []

for key, value in data.items():
    if value == True:
        goodList.append(key)
    else:
        badList.append(key)

if len(badList) >= 2:
    answer = "check your password"

elif len(badList) == 0:
    answer = "accept"

for bad in badList:
    if bad == "upper":
        answer = "need uppercase"
    elif bad == "lower":
        answer = "need lowercase"
    elif bad == "numbers":
        answer = "need number"
    elif bad == "special_symbols":
        answer = "need special symbols"


print(answer)