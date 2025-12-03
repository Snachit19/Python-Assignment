earth_weight = int(input("Enter your weight on Earth (kg): "))


planet_number = int(input(
    "Enter the planet number you want to travel to:\n"
    "1. Mercury\n"
    "2. Venus\n"
    "3. Mars\n"
    "4. Jupiter\n"
    "5. Saturn\n"
    "6. Uranus\n"
    "7. Neptune\n"
    "Your choice: "
))


if planet_number == 1:
    relative_gravity = 0.38
    planet_name = "Mercury"
elif planet_number == 2:
    relative_gravity = 0.91
    planet_name = "Venus"
elif planet_number == 3:
    relative_gravity = 0.38
    planet_name = "Mars"
elif planet_number == 4:
    relative_gravity = 2.53
    planet_name = "Jupiter"
elif planet_number == 5:
    relative_gravity = 1.07
    planet_name = "Saturn"
elif planet_number == 6:
    relative_gravity = 0.89
    planet_name = "Uranus"
elif planet_number == 7:
    relative_gravity = 1.14
    planet_name = "Neptune"
else:
    print("Invalid planet number")
    exit()  


destination_weight = int(earth_weight * relative_gravity)

print(f"Your weight on {planet_name} would be: {destination_weight} kg")