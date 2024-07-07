# 문자 5번 출력
def print_msg(msg, count):
    print((msg + "\n") * count, end="")


msg = input("입력 값 : ")
print_msg(msg, 5)
