def get_positive_integer():
    while True:
        try: 
            value = int(input("How many pizzas would you like to order? "))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a valid number!")

def get_yes_no_input(message):
    while True:
        answer = input(message).lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Please answer "Y" or "N".')

def calculate_pizza_price(num_of_pizzas, is_delivery_needed, is_tuesday, used_app):
    base_price_per_pizza = 12.00
    delivery_charge = 2.50
    discount_percentage = 0.25
    app_discount = 0

    total_price = num_of_pizzas * base_price_per_pizza

    if is_delivery_needed.lower() == 'y' or is_delivery_needed.lower() == 'yes':
        total_price += delivery_charge

    if used_app.lower() == 'y' or used_app.lower() == 'yes':
        app_discount = total_price * discount_percentage
        total_price -= app_discount

    if is_tuesday.lower() == 'y' or is_tuesday.lower() == 'yes':
        total_price *= 0.5

    total_price = round(total_price, 2)

    return total_price

try:
    print("Welcome to BPP !\n=======================")

    num_of_pizzas = get_positive_integer()
    is_delivery_needed = get_yes_no_input("Do you want delivery for the pizzas? (Y/N) ")
    is_tuesday = get_yes_no_input("Is today Tuesday? (Y/N) ")
    used_app = get_yes_no_input("Did you connect us via our app? (Y/N) ")

    total_price = calculate_pizza_price(num_of_pizzas, is_delivery_needed, is_tuesday, used_app)

    print("\nTotal Order:")
    print(f"Number of Pizzas: {num_of_pizzas}")
    print(f"Delivery: {'Yes' if is_delivery_needed == 'y' else 'No'}")
    print(f"Tuesday Discount: {'Yes' if is_tuesday == 'y' else 'No'}")
    print(f"App Discount: {'Yes' if used_app == 'y' else 'No'}")

    print(f"\nTotal Price: £{total_price:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid value.")
