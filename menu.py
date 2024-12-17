# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customerOrder= []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Please select a menu Item: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                 customerMenuInt = int(menu_selection)
                # 4. Check if the menu selection is in the menu items
                 if (customerMenuInt) in menu_items.keys():
                    
                    
                     # Store the item name as a variable
                        customerItemSelection = menu_items[customerMenuInt]["Item name"]



                    # Ask the customer for the quantity of the menu item
                        customerItemQuantity = input("How many do you want: ")

                    # Check if the quantity is a number, default to 1 if not
                        if customerItemQuantity.isdigit():
                            itemQuantity = int(customerItemQuantity)
                            
                            newOrder = ({"Item name" : menu_items[customerMenuInt]["Item name"], "Price": menu_items[customerMenuInt]["Price"], "Quantity": itemQuantity})
                            customerOrder.append(newOrder)
                            # DEBUG print("Current Order:", customerOrder)
                        else:   
                            itemQuantity = 1
                           
                            newOrder = ({"Item name" : menu_items[customerMenuInt]["Item name"], "Price": menu_items[customerMenuInt]["Price"], "Quantity": itemQuantity})
                            customerOrder.append(newOrder)
                           # DEBUG print("Current Order:", customerOrder)

                       
  
                    #throw error
                 else:       print(f"{customerMenuInt} was not a menu option.")
            else:
                print(f"{menu_category} was not a menu option.")
                        

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        # 5. Check the customer's input
        match keep_ordering:
            case "y" | "Y":
                break
            case "n" | "N":
                place_order = False 
                break
            case _: #default case
                print("Please enter either y or n")             


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
# 6. Loop through the items in the customer's order
for order in customerOrder:
    # 7. Store the dictionary items as variables
    itemName = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    nameSpace = ' ' * (26 - len(itemName))
    priceSpace = ' '* (6 - len(f"{price:.2f}"))
    # 9. Create space strings

    # 10. Print the item name, price, and quantity
    print(f"{itemName}{nameSpace}| ${price:.2f}{priceSpace}| {quantity}")

# 11. Calculate the cost of the order using list comprehension
totalPrice = sum(order["Price"] * order["Quantity"] for order in customerOrder)
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print(f"Your total is ${totalPrice:.2f}, Enjoy!")