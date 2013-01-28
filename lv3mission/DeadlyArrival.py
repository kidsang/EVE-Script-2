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
	print '--> mission Deadly Arrival'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('lco'):
		return False

	if not overview.lockTarget('ruined_structure'):
		return False

	if not ship.approach():
		return False

	if not ship.enableAfterburn():
		return False

	if not general.openMissionDetails():
		return False

	if not general.missionObjectiveComplete():
		return False

	print '<-- mission Deadly Arrival\n'
	return True