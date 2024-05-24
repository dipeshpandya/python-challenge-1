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

order_list = []

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
    menu_category = input("  ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name.lower()}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name.lower()} item would you like to order?")
            i = 1
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 21 - len(key + key2)
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
            menu_selection = input("Type item number to order: ")
            # 3. Check if the customer typed a number
            #print(f"item number -  {ii}")
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                item_selection = int(menu_selection)
                # 4. Check if the menu selection is in the menu items
                if item_selection in menu_items.keys():
                    # Store the item name as a variable
                    item_selected_name = menu_items[int(menu_selection)]["Item name"]
                    item_price = menu_items[int(menu_selection)]["Price"]
                    #print(f"{item_selected_name}")
                    # Ask the customer for the quantity of the menu item
                    qty = input(f"How many {item_selected_name}? Default is 1 ")

                    # Check if the quantity is a number, default to 1 if not
                    if qty.isdigit():
                        item_qty = int(qty)
                    else:
                        item_qty = 1
                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_selected_name
                        ,"Quantity": item_qty
                        ,"Price": item_price
                        })

                    # Tell the customer that their input isn't valid

                else:
            # Tell the customer they didn't select a menu option
                    print(f"{menu_selection} was not a menu option. Please select a number from the menu to order an item.")
    else:
        # Tell the customer they didn't select a number
        print(f"Your input is invalid. {menu_category} is not an option. Please select a number from the menu.")

    # Creating a while loop to get make sure customer is looped back or can finish the order
    keep_on_ordering = True
    while keep_on_ordering:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        #using match/case 
        match(keep_ordering.upper()):
            # Keep ordering - Selecting (Y)es will loop back to while place_order:
            case 'Y':
                print("good")
                break
            # selecting (N)o will finish the order
            case 'N':
                place_order = False
                print("OK, Thank you. Preparing your order \n") 
                break

            # in case user selects something other than Y or N, it will loop back to "keep_ordering"
            case _: 
                print("Please select corret option")
                

# Uncomment the following line to check the structure of the order
# print(order_list)
# showing customer what is being prepared
print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity | Total Price ")
print("--------------------------|--------|----------|---------------")

# 6. Loop through the items in the customer's order using list comprehension
if type(order_list) is list:
    for line in order_list:
        
        # 7. Store the dictionary items as variables
        item_name = line['Item name']
        price = line['Price']
        quantity = line['Quantity']
        extended_price = line['Price'] * line['Quantity']
        
        # 8. Calculate the number of spaces for formatted printing
        name_length = 25-len(item_name)
        
        # 9. Create space strings
        order_item_spaces = " " * (name_length)
        quantity_spaces = " " * (8 - len(str(quantity)))
        price_spaces = " " * (5 - len(str(price)))
        extended_price_spaces = " " * (12-len(str(extended_price)))
        # Creating line using - by calculating space
        item_line = "-" * (name_length + len(item_name)+1)
        price_line = "-" * 8
        quantity_line = "-" * 10
        total_price_line = "-" * 15

        # 10. Print the item name, price, and quantity and extended price
        print(f"{item_name}{order_item_spaces} |  ${price}{price_spaces}| {quantity_spaces}{quantity} |  {extended_price_spaces}${extended_price}")
    else:
        # When list is finished, printing top line for receipt total This step wasnt asked for but did it to make it look better. 
        print(f"{item_line}|{price_line}|{quantity_line}|{total_price_line}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

        # Rounding off the sum to 2 decimal points
        total_cost = round(sum(line['Price'] * line['Quantity'] for line in order_list),2)

        # calculating space to align extended price to read correctly for extended price more or less than $10.00 
        right_align = " " * (len(item_line+price_line+quantity_line+total_price_line)-18-len(str(total_cost)))

        # printing final summary line with total order value
        print(f"Your total order is {right_align}${total_cost}")

        # printing bottom line of the receipt
        print(f"{item_line}-{price_line}-{quantity_line}--{total_price_line}")
