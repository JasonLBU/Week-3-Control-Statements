# Task 1
name = input("What is your name?")
if (name == ""):
    print("Hello, Stranger!")
else:
    print("Hello, " + name + ". Good to meet you!")
print()

# Task 2
password_1 = input("Please enter a new password")
password_2 = input("Please enter another password")
if (password_1 == password_2):
    print("Password Set")
else:
    print("Error")
print()

# Task 3
# Modify Task 2 program,so the password must be between
# 8 and 12 characters long
FirstPass = input("Please enter a new password")
if (len(FirstPass) >= 8 and len(FirstPass) <=12):
    print("Password Set")
else:
    print("Invalid length error")
print()

# Task 4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
Userpassword = input("Please enter a new password")
if (Userpassword in BAD_PASSWORDS):
        print("Password cannot be chosen from the list")
else:
        print("Password Set")
print()

# Task 5
valid = True
while valid:
    UserPassword = input("Please enter a password")
    if ((len(UserPassword) >= 8 and len(UserPassword) <= 12) and UserPassword not in BAD_PASSWORDS):
        print("Valid password")
        print("Password Set")
        valid = False
        break
    else:
        print("Invalid Password")
# Task 6
for i in range(13):
    result = i * 7
    print(str(i) + " x 7 = " + str(result))

# Task 7
# Modify Task 6 to ask the user for a number of the table
TableNum = int(input("Enter a number"))
if (TableNum >= 0 and TableNum <= 13):
    for i in range(TableNum):
        result = i * TableNum
        print(str(i) + " x " + str(TableNum) + " = " + str(result))
else:
    print("Invalid number")
print()
# Task 8
TableNum = int(input("Enter a number"))
if TableNum < 0:
    for i in range(12,-1,-1):
        result = i * TableNum
        print(str(i) + " x " + str(TableNum) + " = " + str(result))