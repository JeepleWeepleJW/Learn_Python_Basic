# 시험 점수 평균 구하기
def get_total_score(count):
    temp_score = 0
    for i in range(count):
        score = int(input(f"{i + 1}번 학생 점수 : "))
        temp_score += score
    return temp_score


student_count = 10
total_score = get_total_score(student_count)
print(f"{student_count}명 학생 시험 평균 : {total_score / student_count}")
