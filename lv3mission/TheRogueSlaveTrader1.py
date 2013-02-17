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
	print '--> mission The Rogue Slave Trader (1 of 2)'

	if not ship.enableDefense():
		return False

	if not drones.launchSmall():
		return False

	overview.seekAndDestory()

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('slave_pen'):
		return False

	ship.approach()

	ship.enableAfterburn()

	time.sleep(10)

	if not drones.engage():
		return False

	while not overview.pickCargo():
		pass

	if not drones.back():
		return False

	print '<-- mission The Rogue Slave Trader (1 of 2)\n'
	return True
