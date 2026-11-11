student_name = input("Enter student name: ").strip()

marks = []
for i in range(1, 4):
    subject_mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(subject_mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)

if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks <= 79:
    grade = "A"
elif 60 <= average_marks <= 69:
    grade = "B"
elif 50 <= average_marks <= 59:
    grade = "C"
else:
    grade = "F"

print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")
