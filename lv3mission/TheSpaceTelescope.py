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
	print '--> mission The Space Telescope'

	ship.enableDefense()

	if not overview.switchTo('battle'):
		return False

	if not overview.activateAccelerationGate():
		return False

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('guristas_space', 15):
		return False

	if not drones.launchSmall():
		return False

	ship.fireOnce()

	drones.engage()

	if not general.openMissionDetails():
		return False

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission The Space Telescope\n'
	return True