print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    size_price = 15
elif size == "M":
    size_price = 20
else:
    size_price = 25

if pepperoni == "Y":
    if size == "S":
        bill = size_price + 2
    else:
        bill = size_price + 3

if extra_cheese == "Y":
    bill =+ 1

print(f"Your final bill is: {bill}")
