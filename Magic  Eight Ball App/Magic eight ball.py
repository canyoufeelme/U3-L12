import time
import random

print('-'*63)
print('Hello queer traveler! I am a Magic Eight Ball!')
print()
question = input('What is your question? ')
time.sleep(0.7)
print('Shaking!')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice = random.randint(1,6)

if choice ==1:
	print('Hell yeah!')
elif choice == 2:
	print('Negative my friend!')
elif choice == 3:
	print('Ask again dude.')
elif choice == 4:
	print('I really couldnt say:/')
elif choice == 5:
	print('Yes! Yes! Yes!')
else:
	print('Kawaii desuka!')
