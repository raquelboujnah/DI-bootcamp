# import MenuItems from menu_items

def show_user_menu():
    #display program menu
    user_action = input("what would you like to do?\n View an Item = 'V'\nAdd an Item = 'A'\nDelete an Item = 'D'\n Update an Item = 'U'\n Show the Menu = 'S'\n")
    while user_action not in "VADUS":
        print("you have to tyoe a letter from the menu")
        user_action = input("what would you like to do?\n View an Item = 'V'\nAdd an Item = 'A'\nDelete an Item = 'D'\n Update an Item = 'U'\n Show the Menu = 'S'\n")
        
    if user_action == "V":
        user_view = input("witch item would you like to see? ")
        print(self.items[user_view])
    elif user_action == "A":
        user_add = ("type the name and the price of the item you want to add")
        user_add_aswer = tuple(user_add)
        MenuItems.save(user_add_aswer[0], user_add_aswer[1])
    elif user_action == "D":
        user_delete = ("type the name of the item you want to delete")
        MenuItems.delete(user_delete)    
    elif user_action == "U":
        user_add = ("type the name and the price of the item you want to update")
        user_update_aswer = tuple(user_add)
        MenuItems.update(user_update_aswer[0], user_update_aswer[1])
    elif user_action == "S":
        show the menu