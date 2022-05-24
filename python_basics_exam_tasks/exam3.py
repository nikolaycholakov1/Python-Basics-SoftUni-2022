student_count = int(input())

below_299 = 0
below_399 = 0
below_499 = 0
above_5 = 0
average_grade = 0

for student in range (1, student_count + 1):
    student_grade = float(input())
    average_grade = average_grade + student_grade

    if student_grade <= 2.99:
        below_299 += 1
    elif student_grade >= 3 and student_grade <= 3.99:
        below_399 += 1
    elif student_grade >= 4 and student_grade <= 4.99:
        below_499 += 1
    elif student_grade >= 5:
        above_5 += 1

print(f"Top students: {(above_5 / student_count) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(below_499 / student_count) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(below_399 / student_count) * 100:.2f}%")
print(f"Fail: {(below_299 / student_count) * 100:.2f}%")
print(f"Average: {average_grade / student_count:.2f}")
