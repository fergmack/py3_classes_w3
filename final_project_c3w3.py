# Finally a working version
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():

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
    return "{} (${})".format(self.name, self.prizeMoney)

# a quick test to see if the Class works 
# x = WOFPlayer(name='john')
# print(x)

# Part B: WOFHumanPlayer
# Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A). This class is going to represent a human player. In addition to having all of the instance variables and methods that WOFPlayer has, WOFHumanPlayer should have an additional method:
# .getMove(category, obscuredPhrase, guessed)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
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

    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty = difficulty
        self.name = name

    def smartCoinFlip(self):
        rand_number = random.randint(1,10)
        if rand_number > self.difficulty:
            return True
        elif rand_number <= self.difficulty:
            return False

    def getPossibleLetters(self, guessed):
        lst_let = []
        if self.prizeMoney >= VOWEL_COST:
            for letter in LETTERS:
                if letter not in guessed:
                    lst_let.append(letter)
                else:
                    continue
        elif self.prizeMoney < VOWEL_COST:
            for letter in LETTERS:
                if letter not in guessed and letter not in VOWELS:
                    lst_let.append(letter)
                else:
                    continue
        return lst_let

    def getMove(self, category, obscuredPhrase, guessed):
        letters_available = self.getPossibleLetters(guessed)
        #reverse SORTED_FREQUENCIES in order to iterate through, [0] to end
        rev_SORT_FREQ = self.SORTED_FREQUENCIES[::-1]

        if letters_available == []:
            return "pass"
        elif self.smartCoinFlip():
            for letter in rev_SORT_FREQ:
                if letter in letters_available:
                    return letter
                else:
                    continue
            return "pass"
        else:
            whatsleft = random.choice(letters_available)
            return whatsleft
