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
	print '--> mission What Comes Around Goes Around'

	if not ship.enableDefense():
		return False

	if not drones.launchSmall():
		return False

	result = None
	begin = time.time()
	while not result and time.time() - begin < 10:
		time.sleep(0.2)
		result = findAtFull('close')
		mouse.leftClickAtP(result)

	if not general.openMissionDetails():
		return False

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission What Comes Around Goes Around\n'
	return True