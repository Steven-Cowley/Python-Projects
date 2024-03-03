# food ordering app written by Steven Cowley

# TODO create food items ie 3 burger types
# TODO create 3 fry types (small, medium large)
# TODO create 3 drink types (small, medium, large) POSSIBLY add different types of drinks 

# create lists to hold types of items
burger_types = ["burger1", "burger2", "burger3"]
fry_types = ["small", "medium", "large"]
drink_types = ["small", "medium", "large"]

# TODO create prices for each item

burger_prices = [3.45, 5.85, 7.23]
fry_prices = [1.25, 3.50, 5.75]
drink_prices = [2.50, 5.11, 8.21]

# TODO generate an interaction between program and the user

# display burgers
print("Burgers")
for burger_type, burger_price in zip(burger_types, burger_prices):
    print(f"{burger_type} {burger_price:.2f}")

# display fries
print("\nFrench fries:")
for fry_type, fry_price in zip(fry_types, fry_prices):
    print(f"{fry_type} {fry_price:.2f}")

# display drinks
print("\nDrinks")
for drink_type, drink_price in zip(drink_types, drink_prices):
    print(f"{drink_type} {drink_price:.2f}")

# gather input from user
choice_of_burger = input("what type of burger would you like: ")
choice_of_fries = input("what type of fries would you like: ")
choice_of_drink = input("what type of drink would you like: ")

total = 0.00
for choice_of_burger in burger_types:
    if choice_of_burger == 'burger1':
        total += burger_prices[0]
    elif choice_of_burger == 'burger2':
        total += burger_prices[1]
    elif choice_of_burger == 'burger3':
        total += burger_prices[2]
    else:
        continue

for choice_of_fries in fry_types:
    if choice_of_fries == 'small':
        total += fry_prices[0]
    elif choice_of_fries == 'medium':
        total += fry_prices[1]
    elif choice_of_fries == 'large':
        total += fry_prices[2]

for choice_of_drink in drink_types:
    if choice_of_drink == 'small':
        total += drink_prices[0]
    elif choice_of_drink == 'medium':
        total += drink_prices[1]
    elif choice_of_drink == 'large':
        total += drink_prices[2]
    else:
        continue

print(f"your total is {total}")
payment_method = input("how will you be paying card or cash: ")
if payment_method == 'card':
    customer_amount = input("reciving payment ")
    if customer_amount == total or customer_amount > total:
        customer_amount - total
        print("payment sucessfull, enjoy your meal")
    elif customer_amount < total:
        print("payment unsucessfull: invalid funds")
elif payment_method == 'cash':
    cash_given = float(input("enter cash amount here"))
    if cash_given >= total:
        change = cash_given - total
        print(f"your change is {change:.2f} enjoy your meal!")
    else:
        print("sorry this is not enough")
        