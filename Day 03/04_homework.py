stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

flavour = input("Please enter your favourite ice cream flavour🍦:")
fav_flavour = flavour.strip(".,!@#$%^&*)(/_-=+?<>:;'}]{[|1234567890").strip().lower()

# Task 1.1
if fav_flavour == stock1:
    print(f"Yes, we have {stock1} in stock.")
elif fav_flavour == stock2:
    print(f"Yes, we have {stock2} in stock.")
elif fav_flavour == stock3:
    print(f"Yes, we have {stock3} in stock.")
elif fav_flavour == stock4:
    print(f"Yes, we have {stock4} in stock.")
else:
    print(f"Sorry, we ran out of {fav_flavour}")

# Task 1.2
if fav_flavour == stock1 or stock2 or stock3 or stock4:
    print(f"Yes, we have {fav_flavour} in stock.")
else:
    print(f"Sorry, we don't have {fav_flavour}.")

# Task 1.3 (refactoring)
# code quality improves, functionality remains the same
flavours = ["vanilla", "chocolate", "tin roof", "cookie dough"]
if fav_flavour in flavours:
    print(f"We have {fav_flavour} in stock")

else:
    print(f"We do not have {fav_flavour} in stock")
