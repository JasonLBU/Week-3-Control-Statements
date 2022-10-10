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
if (len(FirstPass) >= 8 & len(FirstPass) <=12):
    print("Password Set")
else:
    print("Invalid length error")
print()

# Task 4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
ChosenPass = input("Please enter a new password")
for i in range(BAD_PASSWORDS):
    if (i == ChosenPass):
        print("Password cannot be chosen from the list")
    else:
        print("Password Set")
print()

# Task 5
valid = True
while valid:
    UserPassword = input("Please enter a password")
    if (len(UserPassword) >= 8 & len(UserPassword) <= 12):
        print("Valid password length")

        for i in range(BAD_PASSWORDS):
            if (i == UserPassword):
                print("Password cannot be chosen from the invalid list")
            else:
                print("Password Set")
                valid = False
    else:
        print("Invalid length error")