

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
print(myString.count('l'))

s = 'python is pythonic'
print(s.count('python'))

# We’re going to define a few useful methods for you:
# * getNumberBetween(prompt, min, max)) repeatedly asks the user for a number between min and max with the prompt prompt

# * spinWheel() simulates spinning the wheel and returns a dictionary with a random prize

# * getRandomCategoryAndPhrase() returns a tuple with a random category and phrase for players to guess

# * obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess

import json 
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
  userinp = input(prompt) # ask the first time
  while True:
    try:
      n = int(userinp) # try casting to an integer
      if n < min:
        errmessage = 'Must be at least {}'.format(min)
      elif n > max:
        errrmessage = 'Must be less than {}'.format(max)
      else:
        return n
    except ValueError: # the user didn't enter a number
      errmessage = '{} is not a number.'.format(userinp)

    # If we haven't gotten a number yet, add the eorror message and ask again
    userinp = input('{}\n{}'.format(errmessage, prompt))

getNumberBetween('Enter number between 1 and 10', 1, 10)

