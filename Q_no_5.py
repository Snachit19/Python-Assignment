usage = int(input("Enter electricity usage in units: "))

if usage < 100:
    cost = usage * 5

elif usage <= 300:
    cost = (100 * 5) + (usage - 100) * 8

else:
    cost = (100 * 5) + (200 * 8) + (usage - 300) * 10

print("Total cost: Rs", cost)