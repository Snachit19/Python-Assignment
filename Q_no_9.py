num = int(input("Enter a number: "))

# Check if the number is positive
if num > 0:
    # Check if the number is even or odd
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")