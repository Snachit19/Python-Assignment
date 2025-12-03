current_floor = 5
requested_floor = int(input("Enter requested floor: "))

if requested_floor > current_floor:
    print("Lift should go UP")
elif requested_floor < current_floor:
    print("Lift should go DOWN")
else:
    print("Lift should STAY")