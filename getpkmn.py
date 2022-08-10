import requests
from pkmn import Pokemon

def getpkmn(pokedex):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokedex}')
    pkmn = r.json()
    
    p = Pokemon(pkmn['name'],pkmn['types'][0]['type']['name'],pkmn['stats'][0]['base_stat'])
    # pkmn['stats'][0]['base_stat'] # HP
    # pkmn['stats'][1]['base_stat'] # attack
    # pkmn['stats'][2]['base_stat'] # defence
    # pkmn['stats'][3]['base_stat'] # special-attack
    # pkmn['stats'][4]['base_stat'] # special-defense
    # pkmn['stats'][5]['base_stat'] # speed
    return p