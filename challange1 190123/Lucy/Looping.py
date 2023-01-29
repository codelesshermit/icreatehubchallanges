username="your_username"
password="your_password"
attempts=0
while attempts<3:
    user_username=input("Enter your username:")
    user_password=input("Enter your password:")
    if user_username==username and user_password==password:
        print("Login successful.")
        break
    elif user_username!=username and user_password==password:
        print("incorrect username.")
    elif user_username==username and user_password!= password:
        print("incorrect password.")  
    else:
        print("incorrect username and password.")     
        attempts+=1
    if attempts==3:
            print("Your account has been locked.")    
        


