# 직각삼각형 변의 길이 구하기
def pythagorean_theorem(x, y):
    return x ** 2 + y ** 2


x = int(input("x 값 : "))
y = int(input("y 값 : "))

print(f"z제곱 : {pythagorean_theorem(x, y)}")
