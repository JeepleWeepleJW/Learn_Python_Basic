# 짝수의 합
# for 문 예시2

even_sum = 0

for i in range(0, 11):
    if i % 2 == 0:
        even_sum += i

print("짝수 합 :", even_sum)