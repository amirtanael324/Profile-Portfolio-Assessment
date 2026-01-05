correct_password = "12345"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Password correct!")
        break
    else:
        print("Incorrect password. Try again.")
