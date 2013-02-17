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
	overview.lockEnemy(25)

	ship.enableAfterburn()	

	ship.approachFor(160)

	ship.fireOnce()

	if not drones.launchSmall():
		return False

	overview.seekAndDestory()

	if not drones.back():
		return False


	print '<-- mission The Score\n'
	return True