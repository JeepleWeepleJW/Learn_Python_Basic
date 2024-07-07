# 짝수의 합
# while 문 예시

even_sum = 0
loop_cnt = 0
while loop_cnt < 11:
    if loop_cnt % 2 == 0:
        even_sum += loop_cnt
    loop_cnt += 1

print("짝수 합 :", even_sum)