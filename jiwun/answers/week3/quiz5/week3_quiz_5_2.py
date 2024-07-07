# 두수의 최대 공약수 구하기

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("1번 숫자 입력 : "))
num2 = int(input("2번 숫자 입력 : "))

print(f"최대 공약수 : {gcd(num1, num2)}")
