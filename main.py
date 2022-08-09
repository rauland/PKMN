import os
from pkmn import Pokemon

def main():
    clear_console()
    while True:
        menu = {
            '0':"Select a PKMN",
            '1':"1. Pikachu",
            '2':"2. Charzard"
        }
        for i in menu:
            print(menu[i])
        menu_items(input())

def menu_items(choice):
    match choice:
        case '1':
            options(Pikachu)
        case '2':
            options(Charzard)
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

Pikachu = Pokemon("Pikachu","Electric", 100); Charzard = Pokemon("Charzard","Fire", 135)

main()
