age = int(input("Enter your age: "))


if age >= 18:
  
    has_degree = input("Do you have a degree? (yes/no): ").strip().lower()
    
    if has_degree == "yes":
        
        experience = int(input("Enter your years of work experience: "))
        
       
        if experience > 3:
            print("Highly Eligible")
        elif 1 <= experience <= 3:
            print("Eligible")
        else:
            print("Under Review")
    else:
        print("Not Eligible (No degree)")
else:
    print("Not Eligible (Under 18)")