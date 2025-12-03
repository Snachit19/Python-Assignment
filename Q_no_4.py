age = int(input("Enter age: "))
membership = input("Do you have a membership card? (yes/no): ").lower()

if age < 12:
    print("Ticket Price: Free")
else:
    if age <= 60:
        if membership == "yes":
            print("Ticket Price: Rs. 150")
        else:
            print("Ticket Price: Rs. 200")
    else:
        print("Ticket Price: Rs. 100")