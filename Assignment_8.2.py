# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Abigail Kraska
# Creation Date: 7-28-21
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
  print('''You are in a land full of dragons. In front of you,you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.''')
  #print()
  #commented out second print because it was unnecessary.
def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':
	  #print('Which cave will you go into? (1 or 2)')
	  #cave = input()
    cave=input('Which cave will you go into? (1 or 2)')
  #rewrote the statement to be more concise. Moved the while statement one tab space to the left.
  #return caves
  return cave
  #typo. author wrote caves instead of cave 

#def checkCave(chosenCave)
def checkCave(cave):
  #replaced chosenCave with cave from the chooseCave function
  print('You approach the cave...')
  time.sleep(2)
  print('It is dark and spooky...')
	#sleep for 2 seconds
	#time.sleep(3)
  time.sleep(2)
  #changed the three to a two
  print('A large dragon jumps out in front of you! He opens his jaws and...')
  print()
	#sleep for 2 seconds
  time.sleep(2)
  friendlyCave = random.randint(1, 2)

  #if chosenCave == str(friendlyCave):
  if cave == str(friendlyCave):
    #replaced chosenCave with cave here also.
	  print('Gives you his treasure!')
  else:
	#print 'Gobbles you down in one bite!'
    print ('Gobbles you down in one bite!')
  #Added parenthensis around the print statement. 

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': #put two equals signs
  displayIntro()
	#caveNumber = choosecave()
  caveNumber = chooseCave()
  #had to capitalize cave because the case was incorrect.
  checkCave(caveNumber)
  #checkCave(chooseCave())
  #commented out the previous statement because it would loop the program twice before asking if I wanted to play again instead of asking after every time.
	#print('Do you want to play again? (yes or no)')
	#playAgain = input()
  playAgain=input('Do you want to play again? (yes or no)') 
#I rewrote the code for the input because I feel like this is a more concise way to do it.
  if playAgain == "no":
		#print("Thanks for planing")
    print("Thanks for playing")
    #I fixed the typo in the output statement.

