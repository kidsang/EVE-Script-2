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
	print '--> mission TheSevensPrisionFacility'

	if not ship.enableDefense():
		return False

	if not drones.launchSmall():
		return False

	ship.enableAfterburn()

	overview.seekAndDestory()

	if not drones.back():
		return False

	print '<-- mission TheSevensPrisionFacility\n'
	return True
