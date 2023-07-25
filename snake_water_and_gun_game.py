# Snake Water Gun or Rock Paper Scissor
import random

def game(comp,you):

# if your and computer's choice is same declare a tie 
   
    if comp == you:
        return None

# all possiblities when computer chooses snake        
    elif comp == 's':
        if you == 'w':
          return False
        elif you == 'g':
            return True

# all possiblities when computer chooses water            
    elif comp ==  'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

# all possiblities when computer chooses gun            
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w': 
            True        
                        
x = random.randint(1,3) # Computer have three options to choose Snake,Water and Gun
if x == 1:
    comp ='s'
elif x == 2:
    comp = 'w'
elif x == 3:
    comp = 'g'    

you = input('your Turn:Snake(s) Water(w) or Gun(g) ?:')
a = game(comp,you)  # Function calling i.e. starting game here

print(f'Computer\'s choice:{comp}')
print(f'Your choice:{you}')

if a ==  None:
    print('The game is a tie')
elif a:
    print('You Win!')
else:
    print('You Loose!')    