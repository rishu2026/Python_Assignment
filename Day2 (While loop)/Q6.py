# Q6: Username and password authentication system with limited attempts
username = "rishu123"
password = "Rishu@123"
while True:
    user = input("Enter Username: ")
    if user == username:
        break
    else:
        print("Incorrect Username! Try again.")
attempt = 3
while attempt > 0:
    pas = input("Enter Password: ")
    if pas == password:
        print("Login Successful")
        break
    else:
        attempt -= 1
        print("Wrong Password! Attempts left:", attempt)
