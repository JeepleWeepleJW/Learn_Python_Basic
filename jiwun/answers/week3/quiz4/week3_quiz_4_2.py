# 시험 점수 평균 구하기
def get_avg_score(count):
    total_score = sum(int(input(f"{i + 1}번 학생 점수 : ")) for i in range(count))
    return total_score / count


student_count = 10
avg_score = get_avg_score(student_count)
print(f"{student_count}명 학생 시험 평균 : {avg_score}")
