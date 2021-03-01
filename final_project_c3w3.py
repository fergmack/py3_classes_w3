# We’re going to define a few useful methods for you:

# getNumberBetween(prompt, min, max)) repeatedly asks the user for a number between min and max with the prompt prompt

# spinWheel() simulates spinning the wheel and returns a dictionary with a random prize

# getRandomCategoryAndPhrase() returns a tuple with a random category and phrase for players to guess

# obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess

# Take some time to read their implementations below.



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
    userinp = input(prompt)  # ask the first time
    while True:
        try:
            n = int(userinp)  # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be less than {}'.format(max)
            else:
                return n
        except ValueError:  # the user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the eorror message and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))


# getNumberBetween('Enter number between 1 and 10: ', 1, 10)

# ---------------------------------------
# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
# prizes


def spinWheel():
    with open('wheel.json', 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)


# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")

phrases_json = {
    'Star & Role': [
        'Adam Sandler As Happy Gilmore', 'Anthony Hopkins As Nixon',
        'Bob Denver As Gilligan', 'Candice Bergen As Murphy Brown',
        'Don Johnson As Nash Bridges', 'Eddie Murphy As The Nutty Professor',
        'Elizabeth Taylor & Richard Burton In Cleopatra'
    ]
}


def getRandomCategoryAndPhrase():
    with open("phrases.json", "r") as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase = random.choice(phrases[category])
        return (category, phrase.upper())


# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"


def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv + '_'
        else:
            rv = rv + s
    return rv


# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
  Category: {}
  Phrase:   {}
  Guessed:  {}
  """.format(category, obscuredPhrase, ', '.join(sorted(guessed)))


category, phrase = getRandomCategoryAndPhrase()
guessed = []
for x in range(random.randint(10, 20)):
    randomLetter = random.choice(LETTERS)
    if randomLetter not in guessed:
        guessed.append(randomLetter)

print("geRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))

# -------------------------
print("\n{}\n".format("-" * 5))
# -------------------------

print("obscurePhrase('{}', [{}])\n -> {}".format(
  phrase,  
  
  # loops through all the guessed letters and seperates them with a , 
  ','.join(["'{}'".format(c) for c in guessed]) , 
  
  obscurePhrase(phrase, guessed)
)
)
# -------------------------
print("\n{}\n".format("-"*5))
# -------------------------
obscured_phrase = obscurePhrase(phrase, guessed)

print(
      "showBoard( '{}', '{}', [{}]\n -> {} )".format(
          phrase, 
          obscured_phrase, 
          ', '.join( [ "'{}'".format(c) for c in guessed]), 
          showBoard(phrase, obscured_phrase, guessed)
      )
)

# -------------------------
print("\n{}\n".format("-"*5))
# -------------------------
num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))

for x in range(num_times_to_spin):
  print("\n{}\n".format("-"*2))
  print("spinWheel()")
  print(spinWheel())

  
print("\n{}\n".format("-"*5))

print("In 2 seconds, it will run getNumbersBetween ('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10) ")

# ----- UNCOMMENT BELOW 
# time.sleep(2)
# print(getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10: ', 1, 10))

# Task =================================================
print("="*25)
# Part A: WOFPlayer

# We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. 

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

class WORPlayer():

  def __init__(self, name):   
    self.name = name  
    self.prizeMoney = 0
    self.prizes = []

  # methods
  def addMoney(self, amt):
    self.prizeMoney += amt 

  def goBankrupt(self):
    self.prizeMoney = 0 

  def addPrize(self, prize):
    self.prizes.append(prize)

  def __str__(self):
    return "{} ({}) ".format(self.name, self.prizeMoney)

# a quick test to see if the Class works 
# x = WORPlayer(name='john')
# print(x)

# Part B: WOFHumanPlayer
# Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a human player. In addition to having all of the instance variables and methods that WOFPlayer has, WOFHumanPlayer should have an additional method:
# .getMove(category, obscuredPhrase, guessed)

class WOFHumanPlayer(WORPlayer):
  def getMove(self, category, obscuredPhrase, guessed):
    prompt =  input(
      """{name} has ${prizeMoney}

      Category: {category}
      Phrase: {obscured_phrase}
      Guessed: {guessed}

      Guess a letter, phrase, or type 'exit' or pass:

    )""".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
    return prompt

# Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a computer player.

class WOFComputerPlayer(WOFPlayer):
  # a list of English characters sorted from least frequent 
  SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

  def __init__(self, name, difficulty):
    self.name = name 
    self.difficulty = difficulty 
    self.prizemoney = 0
    self.prizes = []

  # methods 
  def smartCoinFlip(self):
    if random.randit(1, 10) > self.difficulty 
      return True 
    else:
      return False

  def getPossibleLetters(guessed): 
   
    # return list
        LEFT OFF 

# def getPossibleLetters(self, guessed=[]):
# lst = []
# for i in LETTERS:
# if self.prizeMoney < VOWEL_COST:
#     if i not in guessed and i not in VOWELS:
#         lst.append(i)
# else:
#     if i not in guessed:
#         lst.append(i)
