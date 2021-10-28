print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0

if size == "s":
    bill = 15
if size == "m":
    bill = 20
if size == "l":
    bill = 25

# Add pepperoni?
if add_pepperoni == "y" and size == "s":
    bill += 2
if add_pepperoni == "y" and size == "m":
    bill += 3
if add_pepperoni == "y" and size == "l":
    bill += 3

# Extra Cheese?
if extra_cheese == "y":
    bill += 1
    print(f"Your total bill is ${bill}")
else:
    print(f"Your total bill is ${bill} ")




