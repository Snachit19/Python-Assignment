a = int(input("Enter students in class A: "))
b = int(input("Enter students in class B: "))
c = int(input("Enter students in class C: "))


desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2


total_desks = desks_a + desks_b + desks_c


print("Minimum number of desks needed:", total_desks)