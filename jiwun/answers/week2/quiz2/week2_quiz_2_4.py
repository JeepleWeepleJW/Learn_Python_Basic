# 짝수의 합
# generator expression 과 sum 사용

even_sum = sum(i for i in range(0, 11) if i % 2 == 0)
print(f"짝수 합 : {even_sum}")
