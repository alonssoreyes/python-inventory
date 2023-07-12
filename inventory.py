
inventory = [
    {'id': 1, 'product': 'Apple', 'price': 10, 'quantity': 3},
    {'id': 2, 'product': 'Banana', 'price': 15, 'quantity': 5},
    {'id': 3, 'product': 'Orange', 'price': 8, 'quantity': 2},
    {'id': 4, 'product': 'Mango', 'price': 20, 'quantity': 4},
    {'id': 5, 'product': 'Pineapple', 'price': 25, 'quantity': 1},
    {'id': 6, 'product': 'Strawberry', 'price': 12, 'quantity': 6},
    {'id': 7, 'product': 'Watermelon', 'price': 18, 'quantity': 3},
    {'id': 8, 'product': 'Grapes', 'price': 10, 'quantity': 4},
    {'id': 9, 'product': 'Blueberries', 'price': 15, 'quantity': 2},
    {'id': 10, 'product': 'Kiwi', 'price': 10, 'quantity': 5},
    {'id': 11, 'product': 'Chair', 'price': 50, 'quantity': 10},
    {'id': 12, 'product': 'Table', 'price': 100, 'quantity': 5},
    {'id': 13, 'product': 'Lamp', 'price': 30, 'quantity': 8},
    {'id': 14, 'product': 'Book', 'price': 15, 'quantity': 20},
    {'id': 15, 'product': 'Shirt', 'price': 25, 'quantity': 15},
    {'id': 16, 'product': 'Pants', 'price': 35, 'quantity': 12},
    {'id': 17, 'product': 'Shoes', 'price': 60, 'quantity': 7},
    {'id': 18, 'product': 'Hat', 'price': 20, 'quantity': 10},
    {'id': 19, 'product': 'Socks', 'price': 8, 'quantity': 30},
    {'id': 20, 'product': 'Backpack', 'price': 40, 'quantity': 5}
]



def add_item():
    product = input("Please provide the product name: ")
    quantity = input(f"How many {product} items you have? ")
    price = input(f"What is the price for {product}: ")

    to_append = {
        'id': len(inventory) + 1,
        'product': product,
        'price': price,
        'quantity': quantity
    }

    inventory.append(to_append)

    print("Product has been added successfuly...")
    print(f"Details: \n Product name: {product} \n Quantity: {quantity} \n Price: {price}")



def update_item():
    try:
        searched_id = int(input("Provide the product id you want update: "))
        index = find_by_id(searched_id)
        print(f"Found product {inventory[index]['product']}")
        field_to_change = input("What field do you need to change? (id, product, price, quantity) ")

        if not field_to_change in inventory[index]:
            raise KeyError('Key not found in product item')
        
        print(f"Great, let's change {field_to_change}...")
        new_value = input(f"Please provide the new value for {field_to_change}: ")

        inventory[index][field_to_change] = new_value

        print(f"Changes to {inventory[index]['product']} applied successfuly")

    except (KeyError, IndexError) as error:
        print(str(error))

def search_item():
    criteria = criteria_selection()
    criteria_value = input(f"What is the value you are looking for {criteria}")

    if criteria in ['id', 'quantity', 'price']:
        criteria_value = int(criteria_value)
    
    match_items = search_by(criteria, criteria_value)
    print(match_items)

    
def search_by(criteria, value):
    return list(filter(lambda item: item[criteria] == value, inventory))


def sort():
    global inventory
    criteria = input("Please provide a criteria to sort the inventory: (id, product, quantity, price)")

    if not criteria in ['id','product','quantity','price']:
        print("Criteria is not valid")
        return
    
    inventory =  sorted(inventory, key=lambda x: x[criteria])

    list_all()
    

def finish():
    print("Shutting down...")
    exit(1)


def criteria_selection():
    props = []
    count = 1
    for key in inventory[0].keys():
        print(f"{count}. {key}")
        count = count + 1
        props.append(key)
    selected_field = int(input("Provide the number of criteria: "))
    return props[selected_field - 1]

def find_by_id(id):
    for index,item in enumerate(inventory):
        if id == item['id']:
            return index
    
    raise IndexError(f"Product with id {id} not found in inventory")


def list_all():
    for item in inventory:
        print(f"======================")
        print(f"Product name: {item['product']}\nQuantity: {item['quantity']}\nPrice: ${item['price']}")

def calculate_total_value():
    total_value = 0
    for item in inventory:
        total_value += int(item['price']) * int(item['quantity'])
    print(f"Inventory total value: ${total_value}")

def get_item_with_highest_quantity():
    if len(inventory) > 0:
         highest= max(inventory, key=lambda item: item['quantity'])
         print(f"{highest['product']} is the product with the highest quantity with: {highest['quantity']} items")
    else:
        return None




functions = {
    '1': add_item,
    '2': update_item,
    '3': search_item,
    '4': sort,
    '5': list_all,
    '6': calculate_total_value,
    '7': get_item_with_highest_quantity,
    '0': finish
}




def main():
    selected_option = None
    while selected_option != 0:
        print("======= Inventory, please choose an option ====")
        print('1. Add an item')
        print('2. Update an item')
        print("3. Search")
        print("4. Sort inventory")
        print("5. List all products")
        print("6. Show Inventory total value")
        print("7. Get the product with highest quantity")
        print("0. Exit application.")

        selected_option = input("Which operation you want to perform? ")

        functions[selected_option]()


main()




