age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
days = int(input("Enter number of days worked: "))


if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
    else:
        wage_per_day = 0
        print("Invalid gender entered.")
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
    else:
        wage_per_day = 0
        print("Invalid gender entered.")

else:
    wage_per_day = 0
    print("Age not in the eligible range for wages.")


total_wage = wage_per_day * days


if wage_per_day > 0:
    print(f"Total wages: {total_wage}")   