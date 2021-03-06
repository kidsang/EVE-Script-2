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
	print '--> mission Cut Throat Competition'

	if not ship.enableDefense():
		return False

	if not drones.launchSmall():
		return False

	if not general.openMissionDetails():
		return False

	overview.seekAndDestory()

	if not drones.back():
		return False

	if not overview.activateAccelerationGate():
		return False

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('repair_outpost', 15):
		return False

	if not drones.launchSmall():
		return False

	ship.fireOnce()

	drones.engage()

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission Cut Throat Competition\n'
	return True
