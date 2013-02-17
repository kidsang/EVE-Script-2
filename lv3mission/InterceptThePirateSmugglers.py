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
	print '--> mission Intercept the Pirate Smugglers'

	result = None
	begin = time.time()
	while not result and time.time() - begin < 5:
		time.sleep(0.2)
		result = findAtFull('close')
	if result:
		mouse.leftClickAtP(result)	

	if not ship.enableDefense():
		return False

	if not drones.launchSmall():
		return False

	if not general.openMissionDetails():
		return False

	ship.enableAfterburn()	

	overview.seekAndDestory()

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission Intercept the Pirate Smugglers\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	run()