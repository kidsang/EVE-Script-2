import sys
sys.path.append('..')

import Panel as panel
import Picture as pic
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Station as station
import Overview as overview
import General as general
import Drones as drones
import Ship as ship
import time
from Finder import *

def run():
	print '--> mission Pick Your Position'

	if not overview.switchTo('battle'):
		return False

	if not overview.activateAccelerationGate():
		return False

	# pocket 1
	result = None
	while not result:
		time.sleep(0.5)
		result = findAtFull('close')
	mouse.leftClickAtP(result)

	if not overview.pickCargo():
		return False

	result = None
	while not result:
		time.sleep(0.5)
		result = findAtFull('close')
	mouse.leftClickAtP(result)

	if not overview.activateAccelerationGate():
		return False

	# back to pocket 0
	# double click will not open it!
	result = findTarget('cargo')
	if not result:
		return False
	mouse.leftClickAtP(result)
	ship.approach()

	result = findAtSelectedItem('cargo_small')
	if not result:
		result = findAtSelectedItem('cargo_big')
		if not result:
			return False
	mouse.leftClickAtP(result)

	# print 'wait until cargo open'
	# result = None
	# while not findAtFull('loot_all'):
	# 	time.sleep(0.2)
	# result = findAtFull('x')
	# if not result:
	# 	return False
	# mouse.leftClickAtP(result)

	time.sleep(1)
	mouse.moveTo(200, 200)
	result = findAtFull('close')
	if result:
		mouse.leftClickAtP(result)

	# key.pressEx(sc.Inventory)

	print '<-- mission Pick Your Position\n'
	return True