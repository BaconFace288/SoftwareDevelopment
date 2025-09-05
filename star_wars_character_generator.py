# Needs to ask  Name, Species, Occupation, Main Weapon, home planet,  and Sidekick

character_name = input('Enter the name of your character: ')
species = input("What species is your character? (e.g., Human, Wookiee, Twi'lek): ")
occupation = input("What is your character's occupation? (e.g., Jedi, Sith, Smuggler): ")
weapon = input("What is your character's main weapon?: ")
home_planet = input("Which planet does your character come from?: ")
sidekick = input("Who is your character's sidekick or companion? (e.g., R2-D2, Chewbacca): ")

print("\n----------STAR WARS CHARACTER BIO----------")#43
print(f"Name: {character_name}")
print(f"Species: {species}")
print(f"Occupation: {occupation}")
print(f"Weapon of Choice: {weapon}")
print(f"Home Planet: {home_planet}")
print(f"Sidekick: {sidekick}")
print("------------------------------------------\n")

import random

sidekick = ["R2-D2", "Chewbacca", "BB-8", "K-250", "C-3PO"]
sidekick = random.choice(sidekick)

if occupation.lower() == "jedi":
    print(f"{character_name} upholds the values of the Jedi Order and fights for peace!")
elif occupation.lower() == "sith":
    print(f"{character_name} is seduced by the dark side of the force!")
else:
    print(f"{character_name} is just trying to get by.")
