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
	print '--> mission New Frontiers - Raw Materials (4 of 7)'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('battle'):
		return False

	if not overview.lockTarget('l', 10):
		return False

	ship.enableAfterburn()

	ship.approach()

	if not drones.launchSmall():
		return False

	ship.fireOnce()

	drones.engage()
	
	overview.seekAndDestory()

	while not overview.pickCargo():
		time.sleep(5)

	while overview.pickCargo():
		pass

	if not drones.back():
		return False

	print '<-- mission New Frontiers - Raw Materials (4 of 7)\n'
	return True
