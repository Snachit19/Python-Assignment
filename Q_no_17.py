salary = float(input("Enter employee salary: "))
years = int(input("Enter years of service: "))

if years > 10:
    bonus = salary * 0.10
elif years >= 6 and years <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05

print("Bonus Amount: Rs", bonus)
print("Total Salary After Bonus: Rs", salary + bonus)