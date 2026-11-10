# Student Grade Calculator

student_name = input("Enter Student Name: ")

subject1 = float(input("Enter Marks for Subject 1: "))
subject2 = float(input("Enter Marks for Subject 2: "))
subject3 = float(input("Enter Marks for Subject 3: "))

total_marks = subject1 + subject2 + subject3

average_marks = total_marks / 3

if average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "F"

print("\n----- Student Result -----")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")