import pygame, my, input, ui, map, building, mob, item, random

def spendResource(resource, quantity):
	"""Spend a resource by subtracting from global resource count and subtracting from any stored buildings"""
	for building in my.storageBuildings.sprites():
		if building.resources[resource]:
			excess = building.removeResource(resource, quantity)
		if not excess:
			break

class Handler:
	"""Keep the main.runGame() function nice and tidy"""
	def __init__(self):
		my.ticks = 0
		my.tick = []
		for i in range(20):
			my.tick.append(False)
		my.map = map.Map()
		my.map.completeGen()
		my.input = input.Input()
		my.camera = map.Camera()
		my.hud = ui.Hud()
		my.mode = 'look' 
		my.resources = {'wood': my.STARTRESOURCES['wood'], 
						'iron': my.STARTRESOURCES['iron'], 'cheese': my.STARTRESOURCES['cheese']}
		my.maxResources = {'wood': my.STARTMAXRESOURCES['wood'], 
						'iron': my.STARTMAXRESOURCES['iron'], 'cheese': my.STARTMAXRESOURCES['cheese']}
		my.updateSurf = True
		my.gameRunning = True
		my.statusMessage = 'None'
		self.sunx = int(my.MAPWIDTH / 2)
		my.sunPos = (self.sunx, my.MAPHEIGHT + 10)
		for i in range(0):
			mob.Human((random.randint(5, 25), random.randint(5, 25)), None)
		for i in range(0):
			mob.Human((random.randint(5, 25), random.randint(5, 25)), 'woodcutter')
		for i in range(20):
			mob.Human((random.randint(5, 25), random.randint(5, 25)), 'builder')


	def update(self):
		my.ticks += 1
		for i in range(1, 20):
			if my.ticks % i == 0:
				my.tick[i] = True
			else:
				my.tick[i] = False
		self.sunx += my.SUNMOVESPEED
		if self.sunx > my.MAPWIDTH: self.sunx = 0
		my.sunPos = (self.sunx, my.MAPHEIGHT + 10)
		my.input.get()
		my.map.update()
		building.updateBuildings()
		item.update()
		mob.updateMobs()
		my.camera.update()
		my.hud.update()

		pygame.display.update()
		my.FPSCLOCK.tick(my.FPS)
		pygame.display.set_caption('Real time strategy' + ' ' * 10 + 'FPS: ' + str(int(my.FPSCLOCK.get_fps())))
		my.input.checkForQuit()

		for key in my.resources.keys():
			if my.resources[key] > my.maxResources[key]:
				my.resources[key] = my.maxResources[key]
			if my.resources[key] < 0:
				my.resources[key] = 0
