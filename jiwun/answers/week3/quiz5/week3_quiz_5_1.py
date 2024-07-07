# 두수의 최대 공약수 구하기

def gcd(a, b):
    divisor = 1
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            divisor = i
    return divisor


num1 = int(input("1번 숫자 입력 : "))
num2 = int(input("2번 숫자 입력 : "))

print(f"최대 공약수 : {gcd(num1, num2)}")
