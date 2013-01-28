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
	print '--> mission Eliminate the Pirate Campers'

	ship.enableDefense()

	result = None
	begin = time.time()
	while not result and time.time() - begin < 20:
		time.sleep(0.5)
		result = findAtFull('close')
	if result:
		mouse.leftClickAtP(result)

	ship.enableAfterburn()

	if not general.openMissionDetails():
		return False

	if not overview.switchTo('battle'):
		return False

	if not drones.launchSmall():
		return False

	while overview.lockTarget('s', 25):
		ship.approach()
		ship.fireOnce()

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission Eliminate the Pirate Campers\n'
	return True