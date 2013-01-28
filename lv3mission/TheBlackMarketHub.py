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
	print '--> mission The Black Market Hub'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('battle'):
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

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('docked_bestower', 1):
		return False

	ship.approachFor(5)

	ship.enableAfterburn()	

	if not drones.launchSmall():
		return False

	ship.fireOnce()

	drones.engage()

	overview.switchTo('battle')

	while not overview.pickCargo():
		time.sleep(1)

	drones.back()

	print '<-- mission The Black Market Hub\n'
	return True
