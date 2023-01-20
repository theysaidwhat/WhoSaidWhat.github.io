import wikiquotes
import os
import random
from better_profanity import profanity
#To Do List:
#Score (and deletes text) and Replay
#Github website
#Catagories: Authors, Historical Figures, Comedians, Actors, Political Figures, All, Misc.
#Ask people they want quotes from and add them to list
#If quote length is over 100 words, cut it off
#Leaderboard
#Censorship
#Timer

print("Welcome to the wonderful world of Who Said What!  I'll give you a quote and you need to guess who it is from the 4 options of people I give you!  You can either answer with their number or their name!  Have fun!\n")

listofpeople = ["Gandhi", "Martin Luther King Jr.", "Kanye West", "Adolf Hitler", "Joeseph Stalin", "Alex Jones", "Donald Trump", "Joe Biden", "Barack Obama", "Dave Chappelle", "Julius Caesar", "Augustus", "Adam Sandler", "Will Smith", "Bill Clinton", "William Shakespeare", "Abraham Lincoln", "George Washington", "Aristotle", "Thomas Jefferson", "Albert Einstein", "Alexander Hamilton", "Richard Nixon", "Volodymyr Zelenskyy", "Jesus"]
randomperson = random.choice(listofpeople)
listofpeople.remove(randomperson)
wrongperson1 = random.choice(listofpeople)
listofpeople.remove(wrongperson1)
wrongperson2 = random.choice(listofpeople)
listofpeople.remove(wrongperson2)
wrongperson3 = random.choice(listofpeople)
listofpeople.remove(wrongperson3)


a = wikiquotes.random_quote(str(randomperson), "english")
censoredquote = profanity.censor(a)
print(censoredquote + "\n")

words = [randomperson, wrongperson1, wrongperson2, wrongperson3]

for i in range(len(words)):
    random_index = random.randrange(len(words))
    print(str(i+1) + ": " + words[random_index])
    if i == 0:
      place1 = words[random_index]
    if i == 1:
      place2 = words[random_index]
    if i == 2:
      place3 = words[random_index]
    if i == 3:
      place4 = words[random_index]
    del words[random_index]

if place1 == randomperson:
  correctnumber = str("1")
if place2 == randomperson:
  correctnumber = str("2")
if place3 == randomperson:
  correctnumber = str("3")
if place4 == randomperson:
  correctnumber = str("4")

answer = input("Who Do You Think It Is? \n")
if answer == randomperson or answer == str(correctnumber):
  print("Correct!")
elif answer != randomperson:
  print("Wrong!  It was " + randomperson + "!")
else:
  print("ERROR")