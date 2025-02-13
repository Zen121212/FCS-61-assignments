username = input("Enter your username: ")
password = input("Enter your password: ")

while username != "admin" or password != "1234":
    print("Access denied.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
print("Access granted.")