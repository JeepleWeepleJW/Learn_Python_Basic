# 짝수 번째의 문자만 출력
# range 사용

msg = "메나고는추바지보배가니아구니투야"
msgSum = ""

for i in range(0, len(msg)):
    if (i+1) % 2 == 0:
        msgSum += msg[i]

print(msgSum)