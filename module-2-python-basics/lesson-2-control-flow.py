"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Ignacio, Justine Paul T.
Date: 9-26-2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is basically doing something based on a condition.
If it is not raining, I will go outside, 
or if it is raining lightly, I will take an umbrella and go outside,
or else I will not go outside.

This is if, elif, and else in action respectively and the condition provided here is rain.
In programming, we can use numbers using <, >, ==, <=, and, >= to create conditions.
We can also use True or False for this!


============================================
KEY VOCABULARY
============================================
- condition: This is what needs to be fulfilled before the code block is executed
- if / elif / else: These are chained together to create more complex yes or no decision making
- comparison operator: The things used to create conditions like <, >, ==, <=, and, >=
- boolean expression: True or False conditions
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

age = 17
are_you_legal = age >= 21 
are_you_20 = age == 20

if are_you_legal:
    print("Please enjoy your stay! <3")
elif are_you_20:
    print(f"You're {age} Comeback next year.")
else:
    print(f"Come on now, you're basically a kid at {age} years old!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I ALWAYS forget the colon when typing out functions, if else, match case, etc.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Control flow adds a deep level of decision making to the script and it is 
another foundational function of python that is used everywhere.
"""