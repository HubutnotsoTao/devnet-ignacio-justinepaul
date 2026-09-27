"""
Module 2 — Lesson 4: Functions
Student: Ignacio, Justine Paul T.
Date: 9-27-2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Functions is basically a recipe, it tells you exactly how to do something and it's written 
so you can follow the steps whenever you need to.

============================================
KEY VOCABULARY
============================================
- function: function is a defined code blcok that can be run by calling the name of the function.
- parameter: parameter is a variable that the function can use
- return value: return value signifies the end of a function and something that they will output


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
user_choice = 0
name = ""

def menu(name):

    print("[1]Greeting\n[2]Add name\n[3]Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        greet(name)
        
    elif user_choice == 2:
        name = add_name()
            
    elif user_choice == 3:
        print(f"Thank you for visitin {name}!")
        return False, name #End the while loop
    
    else:
        print("Please enter a valid option")

    return True, name

def greet(name):
    if name:
        print("Greetings " + name)
    else:
        print("Please enter a name <3")
    return

def add_name():
    try:
        name = input("Enter your name: ").strip()
        return name
    except:
        print("Please enter a valid input!")

def main_loop():
    name = ""
    running = True

    while running:
        running, name = menu(name)

main_loop()
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================

"""
