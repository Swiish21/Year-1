
def verify_password(user_password,entered_password):
    return user_password == entered_password

user_password = "Djmalcom19."

entered_password = input("Enter Password: ")

if verify_password(user_password,entered_password):
    print("The Password is correct!")
else:
    print("This is the Wrong Password! Try again.")
