is_valid = True
balance = 50000
correct_pin = 123

if is_valid:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("\n--- ATM MENU ---")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter amount to withdraw: "))
            
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance!")
        
        else:
            if choice == 2:
                print("Current Balance:", balance)
            else:
                if choice == 3:
                    print("Thank you for visiting")
                else:
                    print("Invalid option")
    else:
        print("Wrong PIN")
else:
    print("Invalid Card")