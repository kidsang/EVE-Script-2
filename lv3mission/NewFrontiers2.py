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
	print '--> mission New Frontiers - Raw Materials (2 of 7)'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('battle'):
		return False

	ship.enableAfterburn()

	if not overview.activateAccelerationGate():
		return False

	print 'pocket 1'

	if not drones.launchSentry():
		return False

	if not overview.lockTarget('drone_energy', 25):
		return False

	drones.engage()

	time.sleep(160)

	if not drones.back():
		return False

	mouse.moveTo(100, 100)

	result = findAtDrones('sentry')
	if result:
		mouse.leftClickAtP(result)

	if not drones.launchSmall():
		return False

	ship.enableAfterburn()

	overview.seekAndDestory()

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('delainens', 1):
		return False

	ship.approachFor(30)

	drones.engage()

	while not overview.pickCargo():
		pass

	if not drones.back():
		return False

	print '<-- mission New Frontiers - Raw Materials (2 of 7)\n'
	return True
