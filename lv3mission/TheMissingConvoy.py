
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
	print '--> mission The Missing Canvoy'

	ship.enableDefense()

	if not overview.activateAccelerationGate():
		return False

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('powerful_em', 1):
		return False

	ship.enableAfterburn()

	ship.approachFor(120)

	if not drones.launchSmall():
		return False

	ship.fireOnce()

	drones.engage()

	print 'wait for 80 sec'
	time.sleep(80)

	if not overview.lockTarget('lesser_drone_hive', 1):
		return False

	ship.approachFor(60)

	ship.fireOnce()

	drones.engage()

	while not overview.pickCargo():
		time.sleep(2)

	while overview.pickCargo():
		pass

	if not drones.back():
		return False

	print '<-- mission The Missing Canvoy\n'
	return True
