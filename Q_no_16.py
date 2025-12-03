cost_price = float(input("Enter the cost price of the bike: "))

if cost_price > 100000:
    tax = cost_price * 0.15
elif cost_price > 50000 and cost_price <= 100000:
    tax = cost_price * 0.10
else:
    tax = cost_price * 0.05

print("Road Tax to be paid: Rs.", tax)