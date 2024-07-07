# 사각형,  삼각형 별찍기

# 5열 직각삼각형 찍기
def print_triangle(row):
    for i in range(1, row + 1):
        print("*" * i)


# 5행 5열 사각형 찍기
def print_rectangle(row, col):
    star = "*" * col
    for _ in range(row):
        print(star)


shape = input("출력할 도형 : ")

if shape == "삼각형":
    print_triangle(5)
elif shape == "사각형":
    print_rectangle(5, 5)
else:
    print("해당 도형은 없습니다.")
