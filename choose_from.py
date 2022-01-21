# code from lilstuko, https://github.com/lilstuko/hunger_games.git

def choose_from_menu(choices, prompt):
    while True:
        try:
            for index, option in enumerate(choices):
                print(f"{index + 1}) {option}")
            choice = int(input(prompt))
            if choice >= 1 and choice <= len(choices):
                menu_item = choices[choice - 1]
                break
        except ValueError:
            print("Sorry! Please type the number of the option you wish to select!")

    return menu_item

def choose_from_menu_with_easteregg(choices, prompt, easter_egg, funcyeasteregg):
    while True:
        try:
            for index, option in enumerate(choices):
                print(f"{index + 1}) {option}")
            choice = input(prompt)
            if choice == easter_egg:
                funcyeasteregg()
            else:
                choice = int(choice)
                if choice >= 1 and choice <= len(choices):
                    menu_item = choices[choice - 1]
                    break
        except ValueError:
            print("Sorry! Please type the number of the option you wish to select!")

    return menu_item