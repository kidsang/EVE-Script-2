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

	if not overview.activateAccelerationGate():
		return False

	if not overview.switchTo('battle'):
		return False

	# pocket 1
	result = None
	while not result:
		time.sleep(0.5)
		result = findAtFull('close')
	mouse.leftClickAtP(result)

	if not overview.pickTarget('minmatar_emissary_1'):
		return False

	result = None
	while not result:
		time.sleep(0.5)
		result = findAtFull('close')
	mouse.leftClickAtP(result)

	if not overview.activateAccelerationGate():
		return False
		
	if not overview.switchTo('battle'):
		return False

	# back to pocket 0
	# double click will not open it!
	result = overview.findTarget('cargo')
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

	print 'wait until cargo open'
	while not findAtFull('loot_all'):
		time.sleep(0.2)
		mouse.leftClickAtP(result)


	result = findAtFull('ship')
	while not result:
		result = findAtFull('ship')
	mouse.leftClickAtP(result)

	result = findAtFull('minmatar_emissary')
	while not result:
		result = findAtFull('minmatar_emissary')
	mouse.leftDownAtP(result)

	result = findAtFull('ship_hl')
	while not result:
		result = findAtFull('ship_hl')
	mouse.moveTo(result[0] + 40, result[1] + 60)
	mouse.leftUp()

	result = findAtFull('close')
	while not result:
		result = findAtFull('close')
	mouse.leftClickAtP(result)

	time.sleep(1)
	result = findAtFull('ship_hl')
	if not result:
		result = findAtFull('ship')
	if result:
		mouse.moveToP(result)

	result = findAtFull('x')
	if result:
		mouse.leftClickAtP(result)

	print '<-- mission Pick Your Position\n'
	return True