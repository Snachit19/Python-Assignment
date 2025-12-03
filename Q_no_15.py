# Input marks
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

# Calculations
total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

# Grade decision
if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Division"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)