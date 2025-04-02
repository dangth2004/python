# Viết chương trình tính GPA và xếp loại tương ứng khi biết điểm tổng kết học phần và số tín chỉ của từng môn học
def convert_to_grade_4(score):
    if score >= 9.0:
        return 4.0
    elif score >= 8.5:
        return 3.7
    elif score >= 8.0:
        return 3.5
    elif score >= 7.0:
        return 3.0
    elif score >= 6.5:
        return 2.5
    elif score >= 5.5:
        return 2.0
    elif score >= 5.0:
        return 1.5
    elif score >= 4.0:
        return 1.0
    else:
        return 0.0


def calculate_gpa():
    n = int(input())
    total_credits = 0
    total_grade_points = 0.0

    for _ in range(n):
        credit, score = map(float, input().split())
        grade_4 = convert_to_grade_4(score)
        total_credits += credit
        total_grade_points += credit * grade_4

    if total_credits == 0:
        gpa = 0.0
    else:
        gpa = total_grade_points / total_credits

    gpa_rounded = round(gpa, 2)

    if gpa_rounded >= 3.60:
        rank = "Excellent"
    elif gpa_rounded >= 3.20:
        rank = "Very good"
    elif gpa_rounded >= 2.50:
        rank = "Good"
    elif gpa_rounded >= 2.00:
        rank = "Average"
    else:
        rank = "At risk"

    print(f"{gpa_rounded:.2f}: {rank}")


calculate_gpa()
