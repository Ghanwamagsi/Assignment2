
item1_quantity = int(input("Enter the quantity of item 1: "))
item1_price = float(input("Enter the price of item 1: "))

item2_quantity = int(input("Enter the quantity of item 2: "))
item2_price = float(input("Enter the price of item 2: "))
item3_quantity = int(input("Enter the quantity of item 3: "))
item3_price = float(input("Enter the price of item 3: "))

# Calculate the total cost
total_cost = (item1_quantity * item1_price) + (item2_quantity * item2_price) + (item3_quantity * item3_price)

# Apply discounts if applicable
if total_cost >= 100 and total_cost <= 200:
    item3_price = float(input("Enter the price of item 3: "))

# Calculate the total cost
total_cost = (item1_quantity * item1_price) + (item2_quantity * item2_price) + (item3_quantity * item3_price)

# Apply discounts if applicable
if total_cost >= 100 and total_cost <= 200:
    total_cost *= 0.95  # 5% discount
elif total_cost > 200:
    total_cost *= 0.9  # 10% discount

# Print the total cost
print("Total cost: $", total_cost)



inventory = []

# Function to add items to the inventory
def add_item(name, quantity, price):
    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(item)

# Add items to the inventory
add_item("Apple", 10, 1.5)
add_item("Banana", 15, 0.75)
add_item("Orange", 8, 2.0)

# Print the inventory
print("Inventory:")
for item in inventory:
    print("Name:", item["name"])
    print("Quantity:", item["quantity"])
    print("Price:", item["price"])
    print()

# Calculate the total value of the inventory
total_value = 0
for item in inventory:
    total_value += item["quantity"] * item["price"]

# Print the total value
print("Total Value of Inventory:", total_value)



# Prompt the user to enter a temperature in Celsius
temperature_celsius = float(input("Enter a temperature in Celsius: "))

# Check if the temperature is below freezing or above 30°C
if temperature_celsius <= 0:
    print("It's below freezing! Remember to wear warm clothes.")
elif temperature_celsius > 30:
    print("It's hot outside! Remember to stay hydrated.")

# Convert the temperature to Fahrenheit
temperature_fahrenheit = (temperature_celsius * 9/5) + 32

# Print the converted temperature in Fahrenheit
print("Temperature in Fahrenheit:", temperature_fahrenheit)



names_list = []

# Prompt the user to add names to the list
for i in range(3):
    name = input("Enter a name: ")
    names_list.append(name)

# Print the list of names
print("List of names:", names_list)

# Check if a specific name is in the list
specific_name = input("Enter a name to check: ")
if specific_name in names_list:
    print(specific_name, "is in the list!")
else:
    print(specific_name, "is not in the list."))



def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Test the function by finding the factorial of 5
number = 5
factorial_result = factorial(number)
print("The factorial of", number, "is", factorial_result)




def calculate_ticket_price(age, day):
    adult_price = 10
    child_price = 5
    senior_price = 7.5

    if age >= 18 and age < 65:
        if day.lower() == "weekday":
            return adult_price
        else:
            return adult_price + 2
    elif age < 18:
        if day.lower() == "weekday":
            return child_price
        else:
            return child_price + 2
    else:
        if day.lower() == "weekday":
            return senior_price
        else:
            return senior_price + 2

# Test the function
age = int(input("Enter your age: "))
day = input("Enter the day of the week (weekday/weekend): ")
ticket_price = calculate_ticket_price(age, day)
print("The ticket price is:", ticket_price)



def calculate_ticket_price(age, day, num_tickets):
    adult_price = 10
    child_price = 5
    senior_price = 7.5

    if age >= 18 and age < 65:
        if day.lower() == "weekday":
            price_per_ticket = adult_price
        else:
            price_per_ticket = adult_price + 2
    elif age < 18:
        if day.lower() == "weekday":
            price_per_ticket = child_price
        else:
            price_per_ticket = child_price + 2
    else:
        if day.lower() == "weekday":
            price_per_ticket = senior_price
        else:
            price_per_ticket = senior_price + 2

    total_price = price_per_ticket * num_tickets

    # Apply discount for groups or family packages
    if num_tickets >= 5:
        discount = 0.1  # 10% discount
        total_price -= total_price * discount

    return total_price

# Test the modified function
age = int(input("Enter your age: "))
day = input("Enter the day of the week (weekday/weekend): ")
num_tickets = int(input("Enter the number of tickets: "))
ticket_price = calculate_ticket_price(age, day
def calculate_bill(items, quantities, prices):
    total_amount = 0

    for i in range(len(items)):
        item_total = quantities[i] * prices[i]
        total_amount += item_total

    return total_amount

# Test the function
items = ["Pizza", "Burger", "Fries"]
quantities = [2, 3, 1]
prices = [10, 5, 3]

bill_amount = calculate_bill(items, quantities, prices)
print("The total bill amount is:", bill_team)
      
def calculate_bill(items, quantities, prices, discount=0, tax=0, num_friends=1):
    total_amount = 0

    for i in range(len(items)):
        item_total = quantities[i] * prices[i]
        total_amount += item_total

    # Apply discount
    total_amount -= total_amount * discount

    # Apply tax
    total_amount += total_amount * tax

    # Split the bill among friends
    if num_friends > 1:
        total_amount /= num_friends

    return total_amount

# Test the modified function
items = ["Pizza", "Burger", "Fries"]
quantities = [2, 3, 1]
prices = [10, 5, 3]
discount = 0.1  # 10% discount
tax = 0.05  # 5% tax
num_friends = 3

bill_amount = calculate_bill(items, quantities, prices, discount, tax, num_friends)
print("The total bill amount is:", bill_amount)



def estimate_travel_cost(destination, transportation_cost, accommodation_cost, activity_cost):
    total_cost = transportation_cost + accommodation_cost + activity_cost
    return total_cost

# Test the function
destination = "Paris"
transportation_cost = 500
accommodation_cost = 1000
activity_cost = 500
total_cost = estimate_travel_cost(destination, transportation_cost, accommodation_cost, activity_cost)
print("The estimated travel cost for", destination, "is $", total_cost)









ss