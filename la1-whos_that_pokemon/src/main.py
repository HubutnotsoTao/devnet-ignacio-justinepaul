#Made by Justine Paul T. Ignacio
import requests as rqs
import random as rd

#User interface
def user_menu():
    while True:
        try:
            user_input = int(input("===User Menu===\nSelect your choice:\n[1]Play the guessing game!\n[2]Exit\nYour choice: "))
            if user_input == 1:
                pokemon_guessing_game()
            elif user_input == 2:
                print("See you again!")
                return False
            else:
                print("Please enter a valid choice!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def pokemon_guessing_game():
    #List of pokemons in the guessing game
    pokemon_pool = ["blastoise","rayquaza","charizard","entei","dialga","palkia","gyarados","dragonite"]

    #Generate a number based on the length of the list -1 to account for index 0
    random_choice = rd.randint(0, len(pokemon_pool) - 1)
    random_pokemon = pokemon_pool[random_choice]

    #Get the pokemon information via pokeapi requests based on random pokemon
    get_pokemon = rqs.get(f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}")
    pokemon = get_pokemon.json()

    pokemon_name = pokemon["name"]
    pokemon_height = pokemon["height"]
    pokemon_weight = pokemon["weight"]

    while True:
        print(f"===Welcome to Who's That Pokemon!===\n Your mystery pokemon weighs in at {pokemon_weight/10}kg and is {pokemon_height}m tall.")
        user_guess = input("Guess the pokemon!: ").strip().lower()

        if user_guess == pokemon_name:
            print(f"===Congratulations your guess is correct!===\nThe pokemon is\nName: {pokemon_name}\n{pokemon_weight/10} KG\nHeight: {pokemon_height} M")
            
            while True:
                user_continuation = int(input("[1]Do you want to guess again?\n[2]Exit to menu\nYour choice: "))
                if user_continuation == 1:
                    return pokemon_guessing_game()
                elif user_continuation == 2:
                    return user_menu
                else:
                    print("Please select a valid input!")
        else:
            print("===Your guess was incorrect!===")
            while True:
                user_continuation = int(input("[1]Keep Guessing?\n[2]Yield\nYour choice: "))
                if user_continuation == 1:
                    break
                elif user_continuation == 2:
                    print(f"The pokemon was {pokemon_name}.\nBetter luck next time!")
                    return user_menu()
                else:
                    print("Please select a valid option!")\
        
                

def main_loop():
    while True:
        user_menu()
        return

user_menu()
