import os

def menu(pokemon):
    clear_console()
    while True:
        print("Select a Pokemon")
        for pkmn in pokemon:
            print(pkmn.name)
        menu_items(input(), pokemon)

def menu_items(choice, team):
    match choice:
        case '1':
            options(team[0])
        case '2':
            options(team[1])
        case _:
            clear_console()

def options(selected):
    clear_console()
    print(f"You choose {selected.name}!")

    selected.status(); selected.moveset(); print()
    
    a = input('Learn a Move?').lower(); 
    if a == 'y' or a == 'yes':
        selected.learn_move(input("What's the move? "))

def clear_console():
    """Clears console, command on windows is 'cls', unix is 'clear'"""
    os.system('cls' if os.name == 'nt' else 'clear')