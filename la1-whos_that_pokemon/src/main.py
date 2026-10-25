#Made by Justine Paul T. Ignacio
import requests as rqs
import random as rd

#List of pokemons in the guessing game
pokemon_pool = ["blastoise","rayquaza","charizard","entei","dialga","palkia","gyarados","dragonite"]

#Generate a number based on the length of the list -1 to account for index 0
random_choice = rd.randint(0, len(pokemon_pool) - 1)
random_pokemon = pokemon_pool[random_choice]

#Get the pokemon information via pokeapi requests based on random pokemon
get_pokemon = rqs.get(f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}")
pokemon = get_pokemon.json()

name = pokemon["name"]
height = pokemon["height"]
weight = pokemon["weight"]

print (name)
print (height)
print (weight)
