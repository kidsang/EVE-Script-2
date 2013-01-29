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
	print '--> mission Cargo Deliver'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('battle'):
		return False

	ship.enableAfterburn()

	while not overview.pickCargo():
		pass


	print '<-- mission Cargo Deliver\n'
	return True