# ------------ Part 1
import time 

# for x in range(2, 6):
#   print('Sleep {} seconds..'.format(x))
#   time.sleep(x) # sleep for x seconds

# print('Done!')

# -------------- Part 2
# random.randint(min, max) generates a random number between min and max (inclusive)
# random.choice(L) selects a random item from the list L
import random 

rand_number = random.randint(1, 10)
print('Random number between 1 and 10: {}'.format(rand_number))

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
print(letters)
rand_letter = random.choice(letters)
print('Random letter: {}'.format(rand_letter))

# --------------- Part 3
myString = "Hellow, World! 123"

print(myString.upper())
print(myString.lower())
