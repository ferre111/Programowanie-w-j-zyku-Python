password = "admin1"

password_flag = True

while password_flag:
    print("Enter the password: ")
    if input() == password:
        password_flag = False
        print("Correct password!")
    else:
        print('Incorrect password, try again.')
