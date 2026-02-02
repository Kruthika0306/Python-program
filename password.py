password = input("Enter password: ")

if len(password) < 8:
    print("Weak: Password too short")
elif password.isalpha() or password.isdigit():
    print("Medium: Add numbers and symbols")
else:
    print("Strong password!")
