import time
import random

print('-'*65)
print('Ro Pa Sc')
print()
question= input ('Ready? ')
time.sleep(1)
print('*rock*')
time.sleep(1)
print('paper')
time.sleep(1)
print('scissors')
time.sleep(1)
print('shoot!')
time.sleep(1)
print()
print()
print()
print()
print()
choice= random.randint(1,3)

if choice == 1:
	comp_pick = 'cpu:rock'
	print(comp_pick);
elif choice == 2 :
	comp_pick = 'cpu:paper'
	print(comp_pick);
elif choice == 3 :
	comp_pick = 'cpu:scissors'
	print (comp_pick)

if question == 'rock' and comp_pick == 'cpu:rock':
	print('Draw')
if question == 'paper' and comp_pick == 'cpu:rock':
	print('YOU WIN!')
if question == 'scissors' and comp_pick == 'cpu:rock':
	print('you lose')
if question == 'rock' and comp_pick == 'cpu:paper':
	print('you lose')
if question == 'paper' and comp_pick == 'cpu:paper':
	print('draw')
if question == 'scissors' and comp_pick == 'cpu:paper':
	print('YOU WIN!')
if question == 'rock' and comp_pick == 'cpu:scissors':
	print('YOU WIN!')
if question == 'paper' and comp_pick == 'cpu:scissors':
	print('YOU lose :(')
if question == 'scissors' and comp_pick == 'cpu:scissors':
	print('draw')


print('-'*65)