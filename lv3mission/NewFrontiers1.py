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
	print '--> mission New Frontiers - Raw Materials (1 of 7)'

	if not ship.enableDefense():
		return False

	if not general.openMissionDetails():
		return False

	if not drones.launchSmall():
		return False

	if not overview.switchTo('mine'):
		return

	if not overview.lockTarget('green_arisite', 1):
		return False

	ship.enableAfterburn()

	ship.approachFor(70)

	ship.mine()

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission New Frontiers - Raw Materials (1 of 7)\n'
	return True
