print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%?"))
tip_percentage = tip/100
tip_amount = tip_percentage * bill
split = int(input("How many people to split the bill?"))
result = (tip_amount+bill)/split
result_rounded = round(result, 2)
print(f"Each person should pay: {result_rounded}")