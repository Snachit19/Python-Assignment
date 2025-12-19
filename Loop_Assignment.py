#Q_No_1
list_1 = [1,2,3,4,5]
for i in range(5):
    if list_1[i]%2==0:
        print(f'Number {list_1[i]} is even')
    else:
        print(f'Number {list_1[i]} is odd')

#Q_No_2
list_2 = [10,20,30,40]
sum = 0
for i in list_2:
    print(f'Added {i}',end='.')
    sum += i
    print(f'Running Total is {sum}')
print(f'Total Sum: {sum}')

#Q_No_3
student_names = ["Ram", "Hari", "Sita"]
print("---Email Greeting Generated---")
for i in student_names:
    print(f'Hi {i}, your course approval is ready!')

#Q_No_4
page_list=[40,50,30,45]
print("--- Book Chapter Summary ---")
for i in range(-1,-5,-1):
    print(f'Chapter {-i} has {page_list[i]} pages.')

#Q_No_5
list_3=[4,5,3,2]
product=1
for i in list_3:
    product = product*i
print(f'Product is {product}')

#Q_No_6
number = 11
for i in range(1,11,1):
    print(f'11 X {i} = {11*i}')

#Q_No_7
students_records = [{"name": "ram", "math_grade": 43},{"name": "hari", "math_grade": 65},{"name": "sita", "math_grade": 90}]
for i in students_records:
    if i['math_grade'] >= 70:
        i['Status'] = 'Approved'
    else:
        i['Status'] = 'Rejected'
print(students_records)

#Q_No_7 Alternative way
students_records = [{"name": "ram", "math_grade": 43},{"name": "hari", "math_grade": 65},{"name": "sita", "math_grade": 90}]
for i in range(len(students_records)):
    if students_records[i]['math_grade'] >= 70:
        students_records[i]['Status'] = 'Approved'
    else:
        students_records[i]['Status'] = 'Rejected'
print(students_records)

#Q_No_8
number_list_1 = [1,2,3,4,5]
number_list_2 = [3,4,5,6,7]
common_numbers = []
for i in number_list_1:
    if i in number_list_2:
        common_numbers.append(i)
print(common_numbers)

#Q_No_9
list_4 = [1,2,3,4]
for i in list_4:
    if i == 2 :
        print(i)
    elif i ==4 :
        print(i)

#Q_No_10
list_5 = [1,2,3,4]
for i in list_5:
    if i != 3:
        print(i)

#Q_No_11
list_6 = [1, 2, 3, 4]
for i in range(2):
    if list_6[i] == 2:
        list_6[i] = "a"
        list_6.pop(i+1)
        list_6.insert(2,2)
print(list_6)

#Q_No_12
list_7 = [1, 2, 3, 4, 5]
odd = []
even = []
for i in range(len(list_7)):
    if list_7[i] % 2 == 0:
        even.append(list_7[i])
    else:
        odd.append(list_7[i])
print("Odd numbers:", odd)
print("Even numbers:", even)

#Q_No_13
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if (number % i) == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#Q_No_14
list = [1, 2, 3, 4, 'a', 'b']
int_types = []
str_types = []
for i in range(len(list)):
    if type(list[i]) == int:
        int_types.append(list[i])
    elif type(list[i]) == str:
        str_types.append(list[i])
print("Integer types:", int_types)
print("String types:", str_types)

#Q_No_15
input_string = input( ' Enter a string: ' )
digits = 0
letters = 0
for char in input_string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print("Number of digits:", digits)
print("Number of letters:", letters)

#Q_No_16
valid_username = "admin"
valid_password = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Invalid username or password.")

#Q_No_17
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#Q_No_18
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}.")

#Q_No_19
for i in range(1, 9):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

#Q_No_20
list = [1, 2, 3, 4]
for i in range(len(list)):
    if i == 0 or i == 1:
        print(list[i])

#Q_No_21
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum_odd = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        sum_odd += num
print(f"The sum of all odd numbers between {start} and {end} is {sum_odd}.")

#Q_No_22
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum_even = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        sum_even += num
print(f"The sum of all even numbers between {start} and {end} is {sum_even}.")

#Q_No_23
string = input('Enter a string: ')
space_count = 0
for char in string:
    if char == ' ':
        space_count += 1
print(f'The number of spaces in the given string is: {space_count}')

#Q_No_24
list = [1, 2, 3, 4]
list_2 = []
for i in range(len(list)):
    list_2.append(list[i] ** 3)
print(list_2)

#Q_No_25
string = "programming"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string is:", reversed_string)

#Q_No_26
for i in range(50):
    if i > 7:
        break
    print(i)

#Q_No_27
string = "Hello, World!"
for letter in string:
    print(letter)

#Q_No_28
from tkinter.font import names

names= ["Ram", "Shyam",1,2]
for i in names:
    if isinstance(i, str):
        print("Hello!, " + i) 

#Q_No_29
a = ["ram", "shyam", 1, 2]
lst = []
for i in a:
    lst.append("Dr." + str(i))
print(lst)

#Q_No_30
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(squared_numbers)

#Q_No_31
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []
for num in lst1:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)

#Q_No_32
numbers = [0, 1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 3 or num == 6:
        print(num)

#Q_No_33
lst1 = [10, 15.5, "hello", True, None, 3+4j]
types_list = []
for item in lst1:
    types_list.append(type(item))
print(types_list)

#Q_No_34
for i in range(5):
    print(i)
else:
    print("Done")

#Q_No_35
for i in range(105, 6, -7):
    print(i)

#Q_No_36
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
for char in bad_chars:
    string = string.replace(char, "")
print(string)

#Q_No_37
even_count = 0
odd_count = 0
for i in range(1, 11):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

#Q_No_38
total_sum = 0
for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i
print(total_sum)

#Q_No_39
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#Q_No_40
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")

#Q_No_41
num = int(input("Enter a number: "))
original_num = num
sum_of_cubes = 0
while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num = num // 10
if original_num == sum_of_cubes:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

#Q_No_42
input_string = "This is an example string."
vowels = "aeiouAEIOU"
result_string = ""
for char in input_string:
    if char not in vowels:
        result_string += char
print(result_string)