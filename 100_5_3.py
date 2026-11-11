import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPasswordGenerator!")
nr_letters = int(input("How many letters do you want your password to have?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

total_characters = nr_letters + nr_numbers + nr_symbols

password = []

for pw in range(1, nr_letters + 1):
    password += letters[random.randint(0, 49)]
    
for pw in range(1, nr_numbers + 1):
    password += numbers[random.randint(0,9)]
    
for pw in range(1, nr_symbols + 1):
    password += symbols[random.randint(0, 9)]

random.shuffle(password)
joined_password = "".join(password)
print(joined_password)