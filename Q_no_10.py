a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Greater number is:", a)
elif b > a:
    print("Greater number is:", b)
else:
    print("Both numbers are equal.")
def check_number_sign():
    if a > 0:
        print("The number is positive.")
    elif a < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")