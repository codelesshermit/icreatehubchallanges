username = "user"
password = "123456"

login_attempts = 0
max_login_attempts = 3

while login_attempts < max_login_attempts:
    login_attempts +=1
    username_input = input("Username: ")
    password_input = input("Password: ")


    if username_input == username and password_input == password:
        print("Login Successful")
        break
    elif username_input == username and password_input != password:
        print("Password Incorrect! Try Again")
    elif username_input != username and password_input == password:
        print("Username Incorrect! Try Again")
    else:
        print("Username and Password Incorrect! Try Again")

else:
    print("Too Many Attempts Account Locked")
    
