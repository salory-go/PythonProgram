"""
Program: MidTermProject_ziy2133645.py
Author: Ziyao Liang
Last date modified: 09/16/22
The purpose of this program is to Write a text-based restaurant management system with the following features:

A text file with an existing or starting menu including item names,  wholesale and retail prices for each item on the menu, and a count of how many times the item had been ordered in the past month.
The ability for the restaurant manager to search and update the menu with additions and deletions based on sales targets.
The ability for a customer to view print or search the menu and place several orders.
The customers' orders are charged appropriate sales tax and the customer is offered the option to add a tip. The order summary is printed with subtotals and the grand total due.
The menu file is updated to reflect the updated count of items ordered.
"""
# class item represents each item in the menu
class item:
    # constructor to initialize variables
    def __init__(self, name, wholesale, retail, no_of_times):
        self.name = name
        self.wholesale = wholesale
        self.retail = retail
        self.no_of_times = no_of_times

    # returns the item in string format
    def __str__(self):
        return f"{self.name} {self.wholesale} {self.retail} {self.no_of_times}"


def Menu():
    """ Function to print the main menu"""
    print("*************MENU*************")
    print("1. Restaurant Manager")
    print("2. Customer")


def restaurent_manager_menu():
    """ Function to print the restaurent manager display"""
    print("Restaurant Manager Menu")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Update Item")
    print("4. Print Menu")


def addItem(menu):
    """ function to add item in the menu"""
    print("Enter name")
    name = input()
    print("Enter wholesale price")
    wholesale = float(input().strip("$"))
    print("Enter retail price")
    retail = float(input().strip("$"))
    print("Number of items")
    no_of_times = int(input())
    menu.append(item(name, wholesale, retail, no_of_times))


def search(menu, name):
    """ Function to search for a item in menu with the given name"""
    for i in range(len(menu)):
        if menu[i].name == name.strip():
            return i
    print("Item not present in menu")
    return -1


def update_menu():
    """ Function to print the update menu"""
    print("Enter choice to update")
    print("1) Name")
    print("2) wholesale")
    print("3) Retail")
    print("4) No of Items")


def updateitem(menu, name):
    """ Function to update item in the menu"""
    index = search(menu, name)
    update_menu()
    ch = int(input())
    if ch == 1:
        print("Enter new name")
        name = input()
        menu[index].name = name
    elif ch == 2:
        print("Enter new wholsale price")
        wholesale = float(input().strip("$"))
        menu[index].wholesale = wholesale
    elif ch == 3:
        print("Enter new retail price")
        retail = float(input().strip("$"))
        menu[index].retail = retail
    elif ch == 4:
        print("Enter new number of items")
        no = int(input())
        menu[index].no_of_times = no
    return menu


def removeItem(menu, name):
    """ Function to remove item from the menu"""
    index = search(menu, name)
    print(f"{menu[index].name} Deleted From menu")
    menu = menu[:index] + menu[index + 1 :]
    return menu


def print_menu(menu):
    """function to print the menu to restaurant manager """
    index = 1
    for i in menu:
        print(f"{index}. {i}")
        index += 1


def customer_menu(menu):
    """function to print the menu to customer"""
    index = 1
    for i in menu:
        print(f"{index}. {i.name} {i.retail}")
        index += 1


def place_order(menu):
    """ Function to place order by the customer"""
    names = []
    quantity = []
    total = 0
    while 1:
        print("Enter choice")
        ch = int(input())
        print("Enter Quantity")
        q = int(input())
        menu[ch - 1].no_of_times += q
        total += menu[ch - 1].retail * q
        names.append(menu[ch - 1].name)
        quantity.append(q)
        print("Do you want to place more order\n1) yes\n2) no")
        con = int(input())
        if con == 2:
            break

    """ 5% tax on the total amount"""
    total = total + total * 0.05
    print("Add Tip")
    tip = int(input())
    """ Adding tip to the total """
    total += tip
    """ printing bill of the customer """
    print("\t\tBILL\n")
    """ zip function combines the names and quantity array into a single array of tuples
    Eg : names=[rice,egg] and quantity=[1,2]
    zip function combines them as [(rice,1),(egg,2)]
    """
    for name, q in zip(names, quantity):
        print(f"{name} {q}")

    print("Total Bill is " + str(total))
    return menu


def write_to_file(filename, menu):
    """ Function to write the updated menu in the file"""
    with open(filename, "w") as f:
        for i in menu:
            f.write(f"{i.name}, ${i.wholesale}, ${i.retail}, {i.no_of_times}\n")


if __name__ == "__main__":
    """ array to store list of items """
    menu = []

    """ reading items from file into list"""
    with open("menu.txt") as f:
        for line in f.readlines():
            arr = line.rstrip().split(",")
            menu.append(
                item(
                    arr[0],
                    float(arr[1].strip().strip("$")),
                    float(arr[2].strip().strip("$")),
                    int(arr[3]),
                )
            )

    while 1:
        """ display the main menu """
        Menu()

        """ Enter choice """
        ch1 = int(input())

        """ if choice is 1 print restaurent manager display"""
        if ch1 == 1:
            restaurent_manager_menu()
            """ Enter choice """
            ch2 = int(input())
            if ch2 == 1:
                """ add item in the menu"""
                addItem(menu)
            elif ch2 == 2:
                """ if choice is 2 remove a item """
                print("Enter name of dish to remove ")
                name = input()
                menu = removeItem(menu, name)
            elif ch2 == 3:
                """ if choice is 3 update the item"""
                print("Enter name of item to update")
                name = input()
                menu = updateitem(menu, name)
            elif ch2 == 4:
                """ if choice is 4 print the menu"""
                print_menu(menu)
        else:
            print("*****Customer's Menu*****")
            print("1. View Menu")
            print("2. Place Order")
            ch = int(input())
            if ch == 1:
                """Display customers menu"""
                customer_menu(menu)
            elif ch == 2:
                """Invoke place order menu"""
                menu = place_order(menu)
        print("1. To Continue\n2. Exit")
        ch = int(input())
        """ if choice is 2 exit """
        if ch == 2:
            break

    """Store the updated menu into the file menu.txt """
    write_to_file("menu.txt", menu)
# Margherita Pizza, $1.75, $1.99, 5
# Farmhouse Pizza, $3.9, $3.95, 10
# Chicken Sausage Pizza, $3.0, $3.05, 8
# Spicy Pasta, $1.8, $1.85, 25
# Stuffed Garlic Bread, $1.5, $1.59, 20
# Veg Schezwan Noodles, $1.0, $1.05, 30
# Veg Biryani, $1.1, $1.2, 45