attempts = 0
correct_password = "12345"
while True:
    password = input("Enter the password: ")
    attempts += 1
    if password == correct_password:
        print("Password correct!")
        break
    elif attempts == 1:
        print("Warning: 4 attempts remaining.")
    elif attempts == 2:
        print("Warning: 3 attempts remaining.")
    elif attempts == 3:
        print("Warning: 2 attempts remaining.")
    elif attempts == 4:
        print("Warning: 1 attempt remaining.")
    elif attempts == 5:
        print("Too many incorrect attempts. Access denied. Authorities have been notified.")
        break
    else:
        print("Incorrect password. Try again.")


    
