from menu_items import MenuItems
from menu_manager import MenuManager

def show_user_menu():
    user_action = input("What would you like to do?\nView an Item = 'V'\nAdd an Item = 'A'\nDelete an Item = 'D'\nUpdate an Item = 'U'\nShow the Menu = 'S'\nExit the menu = 'E'\n")
    while user_action not in "VADUSE":
        print("you have to type a letter from the menu")
        user_action = input("what would you like to do?\nView an Item = 'V'\nAdd an Item = 'A'\nDelete an Item = 'D'\nUpdate an Item = 'U'\nShow the Menu = 'S'\n")

def view_item():
    user_view = input("witch item would you like to see? ")
    item = MenuManager(user_view)
    if item:
        item.get_by_name()
    else:
        print("Item not found")
            
def add_item():
    user_add_name = input("type the name of the item you want to add")
    user_add_price = int(input("type the price of the item you want to add"))
    item2 = MenuItems(user_add_name, user_add_price)
    item2.save()
    print(f"The item {user_add_name} has been added")
    
def delete_item():
    user_delete_name = input("type the name of the item you want to delete")
    user_delete_price = int(input("type the price of the item you want to delete"))
    item3 = MenuItems(user_delete_name, user_delete_price) 
    if item3:
        item3.delete()
        print("the item has been deleted")  
    else:
        print("item not found")
            
def update_item():
    user_update_name = input("type the name of the item you want to update")
    user_update_price = int(input("type the price of the item you want to update"))
    item4 = MenuItems(user_update_name, user_update_price) 
    if item4 :
        new_name = (input("type the new name of the item"))
        new_price = (int(input("type the new price of the item")))
        item4.update(new_name, new_price)
        print("the item has been updated")
    else:
        print("item not found")
            
def show_menu():
    MenuManager.all_items()
        
def exit():
    MenuManager.all_items


def main(user_action):
    while True:
        show_user_menu()
        if user_action == "V":
            view_item()
        if user_action == "A":    
            add_item()
        if user_action == "D":
            delete_item()
        if user_action == "U":
            update_item()
        if user_action == "S":
            show_menu()
        if user_action == "E":
            exit()
        break