#import
import random

#list
list =['POW', 'B-BLAM' , 'KAPOW' , 'BOOM' , 'Blast' ]

user_input = input ("Guess what number between 1-2 am I thinking of? Guess wrong, and the bomb explodes!")

if user_input == '1':
    print('You won the 50% game. Well, 50% for the first time.')
else:

#the prompt to choose a word in the list
    noise = random.choice(list)

#print if failed
    print('A Random bomb!', noise , ', you just blew up!')
