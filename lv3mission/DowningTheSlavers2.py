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
	print '--> mission Dawning The Slavers (2 of 2)'

	# if not ship.enableDefense():
	# 	return False

	result = None
	while not result:
		time.sleep(0.5)
		result = findAtFull('close')
	mouse.leftClickAtP(result)

	if not drones.launchSmall():
		return False

	overview.seekAndDestory()

	if not drones.back():
		return False	

	if not overview.switchTo('battle'):
		return False

	if not overview.activateAccelerationGate():
		return False

	if not drones.launchSmall():
		return False

	overview.seekAndDestory()

	if not drones.back():
		return False	

	print '<-- mission Dawning The Slavers (2 of 2)\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	run()