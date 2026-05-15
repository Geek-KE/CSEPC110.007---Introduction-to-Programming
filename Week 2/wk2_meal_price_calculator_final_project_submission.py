# This program calculates the total cost of a meal including drinks and an optional tip,
# then computes the change owed to the customer after payment.

# Meal prices
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Number of people
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute and display subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print()
print(f"Subtotal: ${subtotal:.2f}")

# Sales tax
print()
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * (tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Total
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# This is my creative additional part to the assignment
tip_percent = float(input("What tip percentage would you like to leave? "))
tip = subtotal * (tip_percent / 100)
print("Tip: $" + str(round(tip, 2)))

print()

# Grand total including tip
grand_total = total + tip
print("Grand Total: $" + str(round(grand_total, 2)))

print()

# Payment and change
payment = float(input("What is the payment amount? "))
change = payment - grand_total
print("Change: $" + str(round(change, 2)))