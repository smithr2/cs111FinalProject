import random

def randomWeapon():
	adjectiveListOne = ['Broken', 'Short', 'Long',  'Great']
	adjectiveListTwo = ['Heavy', 'Light', 'Stone', 'Copper', 'Curved', 'Big', 'Fat', 'Ancient', 'Steel', 'Gold', 'Slimy', 'Flaming']
	weaponList = ['Club', 'Dagger', 'Sword', 'Bow', 'Flail']
	qualifiers = ['', '', '', '', '', '', '', '', '', '', 'of Flailing', 'of Eternal Sorrow', 'of Smashing', 'of Destruction', 'of Holy Might', 'of Light', ]
	lenOne = len(adjectiveListOne) - 1
	lenTwo = len(adjectiveListTwo) -1
	lenWeapons = len(weaponList) - 1
	lenQualifiers = len(qualifiers) -1
	randomOne = random.randint(0, lenOne)
	randomTwo = random.randint(0, lenTwo)
	randomWep = random.randint(0, lenWeapons)
	randomQualifier = random.randint(0, lenQualifiers)
	adjectiveOne = adjectiveListOne[randomOne]
	adjectiveTwo = adjectiveListTwo[randomTwo]
	weaponType = weaponList[randomWep]
	qualifier = qualifiers[randomQualifier]
	weapon = adjectiveOne + adjectiveTwo + weaponType + qualifier
	printedName = adjectiveOne + ' ' + adjectiveTwo + ' ' + weaponType + ' '+ qualifier
	critRange = 20
	damageDie = 6
	modifier = 0
	value = 10
	if adjectiveOne == 'Broken':
		critRange -= 2
		modifier -= 2
		value = 0
	elif adjectiveOne == 'Short':
		damageDie -= 1
		modifier += 1
	elif adjectiveOne == 'Long':
		damageDie += 1
	elif adjectiveOne == 'Great':
		damageDie += 2
		modifier -= 1
		critRange -= 1
		value *= 2
	print(printedName)
	w = Weapon(printedName, value, damageDie, critRange, modifier)
	return w
	
def randomSpace(direction, x, y):
	wallList = [0, 0, 0, 0]
	for i in range(4):
		wallList[i] = random.randint(0,1)
	oppositeDirDict = {'n': 2, 'e': 3, 's': 0, 'w':1}
	wallList[oppositeDirDict[direction]] = 1
	descriptionList = ['You are in a low, dark, room']
	descriptionLength = len(descriptionList) - 1
	randomDescription = random.randint(0, descriptionLength)
	description = descriptionList[randomDescription]
	s = Space(x, y, description, wallList)
	print(description, wallList, 'x:', x, 'y:', y)
	return s
	
class Item():
	def __init__(self, name, value):
		self.name = name
		self.value = value
		
class Weapon(Item):
    def __init__(self, name, value, damageDie, critRange, modifier):
        self.damageDie = damageDie
        self.critRange = critRange
        self.modifier = modifier
        super().__init__(name, value)
    def print(self):
    	print(str(self.name), 'Value:', str(self.value), 'Damage Die:', str(self.damageDie), 'Critical Range:', str(self.critRange), 'Modifier:', str(self.modifier))
        
        
class Creature():
	def __init__(self, name, maxHP, currHP, level):
		self.maxHP = maxHP
		self.currHP = currHP
		self.level = level
		
class Space():
	def __init__(self, x, y, description, wallList):
		self.description = description
		self.wallList = wallList
		self.x = x
		self.y = y
	
	def getDescription(self):
		return self.description
	
	def isWall(self, direction):
		dirDict = {'n': 0, 'e': 1, 's': 2, 'w':3}
		if self.wallList[dirDict[direction]] == 0:
			return True
		elif self.wallList[dirDict[direction]] == 1:
			return False
			
def test():
	list =[]
	for i in range(10):
		list.append(randomWeapon())
	for item in list:
		item.print()

def play():
	spaceList = []
	randomx = random.randint(20, 30)
	randomy = random.randint(20, 30)
	for i in range(randomx):
		spaceList.append([])
		for j in range(randomy):
			spaceList[i].append(None)
	x = randomx//2
	y = randomy//2
	q = 0
	counter = 0
	spaceList[x][y] = Space(x, y, 'You find yourself in a wide, open room, lit by torches. Passages lead off to the north, south, east, and west', [1,1,1,1])
	while q == 0:
		print('x', x)
		print('y', y)
		currSpace = spaceList[x][y]
		print(currSpace.getDescription())
		if counter == 0:
			move = input('What would you like to do? Use n, e, s, w to move')
		else:
			move = input('What would you like to do?')
		move = move.lower()
		
		if move == 'n':
			if not currSpace.isWall(move):
				print('You move north')
				y += 1
				print(y)
				print("<",x,",",y,",",(spaceList[x][y] == None),">")
				if spaceList[x][y] == None:
					spaceList[x][y] = randomSpace(move, x, y)
			else:
				print('There is a wall there!')
		elif move == 'e':
			if not currSpace.isWall(move):
				print('You move east')
				x += 1
				if spaceList[x][y] == None:
					spaceList[x][y] = randomSpace(move, x, y)
			else:
				print('There is a wall there!')
		elif move == 's':
			if not currSpace.isWall(move):
				print('You move south')
				y -= 1
				print("<",x,",",y,",",(spaceList[x][y] == None),">")
				if spaceList[x][y] == None:
					spaceList[x][y] = randomSpace(move, x, y)
			else:
				print('There is a wall there!')
		elif move == 'w':
			if not currSpace.isWall(move):
				print('You move west')
				x -= 1
				if spaceList[x][y] == None:
					spaceList[x][y] = randomSpace(move, x, y)
			else:
				print('There is a wall there!')
		else:
			print('something got messed up')
			q += 1
		counter += 1
				
				
				
				       