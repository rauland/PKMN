from getpkmn import getpkmn
from menu import menu

def main():
    pokemon  = []
    pokemon += [getpkmn('pikachu')]
    pokemon += [getpkmn('charizard')]
    menu(pokemon)
main()