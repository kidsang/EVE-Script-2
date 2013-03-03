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
	print '--> mission The Score'

	if not ship.enableDefense():
		return False

	if not overview.activateAccelerationGate():
		return False

	# pocket 1

	if not drones.launchSmall():
		return False

	ship.enableAfterburn()	

	overview.seekAndDestory()

	if not drones.back():
		return False

	if not overview.activateAccelerationGate():
		return False

	# pocket 2
	if not overview.switchTo('battle'):
		return False

	for i in range(4):
		overview.lockTarget('s', 1)

	drones.launchSentry()

	time.sleep(20)

	begin = time.time()
	while time.time() - begin < 100:
		ship.fireOnce()
		drones.engage()
		overview.lockEnemy(1)

	drones.back()

	ship.enableAfterburn()	

	if not drones.launchSmall():
		return False

	ship.fireOnce()

	overview.seekAndDestory()

	if not drones.back():
		return False

	print '<-- mission The Score\n'
	return True