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
	print '--> mission Break Their Will'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('repair_station'):
		return False

	if not general.openMissionDetails():
		return False

	if not drones.launchSentry():
		return False

	if not drones.engage():
		return False

	if not general.missionObjectiveComplete():
		return False

	if not drones.back():
		return False

	print '<-- mission Break Their Will\n'
	return True