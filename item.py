import pygame, my

my.allItems = pygame.sprite.Group()
my.itemsOnTheFloor = pygame.sprite.Group()


def update():
	"""Keep my.handler.update() tidy"""
	for item in my.allItems.sprites():
		item.update()

def loadImg(name):
	return pygame.image.load('assets/items/' + name  + '.png').convert_alpha()


class Item(pygame.sprite.Sprite):
	"""Base class for items dropped when resources are harvested etc"""
	IMG = {}
	for item in ['wood']:
		IMG[item] = loadImg(item)
	def __init__(self, name, quantity, coords, imageName=None):
		# imageName need only be specified if it's not the same as the item name
		pygame.sprite.Sprite.__init__(self)
		self.add(my.allItems)
		self.add(my.itemsOnTheFloor)
		self.name, self.quantity, self.coords = name, quantity, coords
		self.rect = pygame.Rect(my.map.cellsToPixels(self.coords), (my.CELLSIZE, my.CELLSIZE))
		if not imageName:
			imageName = self.name
		self.image = Item.IMG[imageName]
		self.bob = 10 # item will float up and down on the spot
		self.bobDir = 'up'
		self.reserved = False
		self.beingCarried = False
		self.lastCoords = None


	def update(self):
		if self.coords != self.lastCoords:
			self.rect.topleft = my.map.cellsToPixels(self.coords)
		if not self.beingCarried:
			if my.ticks % 4 == 0:
				if self.bobDir == 'up': move = 1
				else: move = -1
				self.rect.move_ip(0, move)		
				if self.bobDir == 'up':
					self.bob += 1
				elif self.bobDir == 'down':
					self.bob -= 1
				if self.bob > 5:
					self.bobDir = 'down'
				elif self.bob < -5:
					self.bobDir = 'up'
			if not self.beingCarried: my.surf.blit(self.image, self.rect)
		if self.beingCarried:
			self.coords = None
			self.remove(my.itemsOnTheFloor)
		self.lastCoords = self.coords




class Wood(Item):
	def __init__(self, quantity, coords):
		Item.__init__(self, 'wood', quantity, coords)


	def update(self):
		Item.update(self)


class Fish(Item):
	def __init__(self, quantity, coords):
		Item.__init__(self, 'fish', quantity, coords)


	def update(self):
		Item.update(self)
