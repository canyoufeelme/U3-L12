health = 100

if health == 100:
	print('You are at full health.')
if health >= 20:
	print('You have taken some minor damage. Health at ' + str(health))
if health >= 1:
	print('You only have ' + str(health) + ' health. Critical warning!')
if health == 0:
	print('You have died :(')