

# 1) The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the string “Did not get gold”.

# TODO - add the name of the country to the list with 'did not get gold' .eg. add chile to the list 

gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
  try:
    country_gold.append(gold[x])
  except:
    country_gold.append("Did not get gold")

# print(country_gold)

# 2) Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.

di = [
  {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
 {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, 
 {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, 
 {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0

# the problem is that 'Puppies' is not in the 3rd dictionary
# uncomment below to see error

# for diction in di:
    # total = total + diction['Puppies']
    # print(diction['Puppies'])

# print("Total number of puppies:", total) 
for diction in di:
  try:
    total = total + diction['Puppies']
  except KeyError:
    continue


print("Total number of puppies:", total)

# 3) The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string “Error” appear in the remainder.
numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainder = []

for n in numb:
  try:
    remainder.append(36 % n )
  except ZeroDivisionError:
    remainder.append('Error')

print(remainder)
