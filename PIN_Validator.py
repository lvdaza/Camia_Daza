pin = input("Enter your 6 digit PIN: ")

if len(pin) == 6:
    print("Valid length pin")
else:
    print("Invalid length PIN, must contain 6 characters")