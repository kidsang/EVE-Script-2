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
	print '--> mission Silence The Informant'

	if not ship.enableDefense():
		return False

	if not general.openMissionDetails():
		return False

	if not overview.activateAccelerationGate():
		return False

	print 'pocket 1'

	if not drones.launchSmall():
		return False

	ship.enableAfterburn()

	overview.seekAndDestory()

	if not drones.back():
		return False

	if not overview.activateAccelerationGate():
		return False

	print 'pocket 2'
	result = None
	begin = time.time()
	while not result and time.time() - begin < 4:
		time.sleep(0.5)
		result = findAtFull('close')
	if result:
		mouse.leftClickAtP(result)

	if not drones.launchSmall():
		return False

	ship.enableAfterburn()

	overview.seekAndDestory()

	if not drones.back():
		return False

	if not overview.activateAccelerationGate():
		return False

	print 'pocket 3'
	result = None
	begin = time.time()
	while not result and time.time() - begin < 4:
		time.sleep(0.5)
		result = findAtFull('close')
	if result:
		mouse.leftClickAtP(result)

	if not drones.launchSmall():
		return False

	ship.enableAfterburn()

	overview.seekAndDestory()

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission Silence The Informant\n'
	return True
