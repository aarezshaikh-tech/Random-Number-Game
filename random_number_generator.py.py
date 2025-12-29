import random


top_range_number = input("type a number you bitch ! ")

# FIX 1: handle the NOT-a-number case
if not top_range_number.isdigit():
    print("learn numbers dumbass")
    quit()

# convert AFTER we know it's a number
top_range_number = int(top_range_number)

# FIX 2: this is now safe because it's an int
if top_range_number <= 0:
    print("dumb ass choice a number which is greater than a 0 next time ")
    quit()

# FIX 3: remove the useless else + quit that stopped the program

random_number = random.randint(0, top_range_number)
print(random_number)

while True:
    print("tim")
    break
