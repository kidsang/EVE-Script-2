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
	print '--> mission Intercept The Sabateurs'

	if not ship.enableDefense():
		return False

	if not drones.launchSmall():
		return False

	if not overview.switchTo('battle'):
		return False

	overview.seekAndDestory()

	if not drones.back():
		return False

	ship.enableAfterburn()

	if not overview.activateAccelerationGate():
		return False

	# pocket 1

	drones.launchSmall()

	if not overview.lockTarget('transport', 1):
		return False

	ship.enableAfterburn()

	ship.approachFor(240)

	general.openMissionDetails()

	if not overview.lockTarget('transport', 15):
		return False

	seekAndDestory()

	while not overview.pickCargo():
		pass

	general.missionObjectiveComplete()

	drones.back()

	print '<-- mission Intercept The Sabateurs\n'
	return True
