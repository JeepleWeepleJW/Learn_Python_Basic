# 짝수의 합
# 등차수열 사용

first = 0
last = 10
common_difference = 2
n = (last - first) // common_difference + 1
even_sum = (n / 2) * (first + last)

print(f"짝수의 합 : {int(even_sum)}")
