import requests as rq
import random as rdm
import json as jason

pokemon_1 = rq.get("https://pokeapi.co/api/v2/pokemon/rayquaza")
pokemon_2 = rq.get("https://pokeapi.co/api/v2/pokemon/entei")
pokemon_3 = rq.get("https://pokeapi.co/api/v2/pokemon/gengar")
pokemon_4 = rq.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pokemon_5 = rq.get("https://pokeapi.co/api/v2/pokemon/blastoise")

pokemon_pool = [{pokemon_1.json()},{pokemon_2.json()},{pokemon_3.json()},{pokemon_4.json()},{pokemon_5.json()}]
rdm.shuffle(pokemon_pool) 
random_pokemon = pokemon_pool[:1]
guess_pokemon = (random_pokemon)

print (guess_pokemon)
