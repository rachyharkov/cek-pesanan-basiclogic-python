
"""
    Checking things using python by Rachmad Nur Hayat
    11:43 27/02/2022

    This is a program that will check if we have a certain thing
    
    there is no copyright, you can do whatever you want with this (if u are student, but u better tell your teacher that you didnt make all of these and just modified it a bit lol)
    
    u are college student? a'ight whatever....
"""


foods = ['artichoke', 'brioche', 'caramel']
drinks = ['tea', 'coffee', 'water']
desserts = ['flan', 'ice cream', 'pie', 'cake']

foodiwant = input("What do you want to eat? ")
drinkiwant = input("What do you want to drink? ")
dessertiwant = input("What do you want to eat after ur dinner? ")

arrayofthingsiwant = {
    'food': '',
    'drink': '',
    'dessert': ''
}

def tellthemthatwedonthavethat(thing):
    print("Sorry we don't have that " + thing)

def tellthemthatwehaveit(thing):
    print("We have that " + thing)

for f in foods:
    if f == foodiwant:
        arrayofthingsiwant.update({'food': f})
        break

for d in drinks:
    if d == drinkiwant:
        arrayofthingsiwant.update({'drink': d})
        break

for des in desserts:
    if des == dessertiwant:
        arrayofthingsiwant.update({'dessert': des})
        break

for key, value in arrayofthingsiwant.items():
    if value == '':
        tellthemthatwedonthavethat(key)
    else:
        tellthemthatwehaveit(value)
