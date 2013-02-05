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

	if not ship.enableDefense():
		return False

	if not drones.launchSentry():
		return False

	if not overview.switchTo('battle'):
		return False

	# kill small

	count = 0
	while count < 4:
		result = overview.lockTarget('s', 1)
		if result:
			count += 1

	begin = time.time()
	while time.time() - begin < 120:
		if findAtDrones('idle'):
			drones.engage()
		result = findAtFull('close')
		if result:
			mouse.leftClickAtP(result)

	if not drones.back():
		return False

	result = findAtDrones('sentry')
	if result:
		mouse.leftClickAtP(result)

	# seek and destory

	if not general.openMissionDetails():
		return False

	ship.enableAfterburn()

	if not drones.launchSmall():
		return False

	overview.seekAndDestory()


	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission Eliminate the Pirate Campers\n'
	return True

