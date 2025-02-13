age = int(input("Welcome to SE Factory Cinema, How old are you? "))

if age < 5:
    print("You cannot enter the cinema.")
elif age < 18:
    print("Ticket price is $10.")
elif age >= 18 and age <= 65:
    print("Ticket price is $12.")
elif age > 65:
    print("Ticket price is $10.")