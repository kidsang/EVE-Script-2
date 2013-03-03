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
	print '--> mission Unauthorized Military Presence'

	if not ship.enableDefense():
		return False

	if not general.openMissionDetails():
		return False

	ship.enableAfterburn()

	if not overview.activateAccelerationGate():
		return False

	if not overview.switchTo('battle'):
		return False

	if not overview.lockTarget('guristas_personnel'):
		return False

	if not ship.enableAfterburn():
		return False

	if not ship.approachFor(240):
		return False

	if not overview.lockTarget('guristas_personnel', 20):
		return False

	if not drones.launchSmall():
		return False

	if not ship.fireOnce():
		return False

	if not drones.engage():
		return False

	# mission item is in wreck
	while not findAtMissionDetails('v'):
		# collect
		overview.pickWreck()	

	if not general.missionObjectiveComplete():
		return False

	# sometimes we already has millitans
	# but the mission is not complete until all enemy dies
	overview.seekAndDestory()

	# just in case
	overview.pickTarget('guristas_personnel')

	if not drones.back():
		return False

	print '<-- mission Unauthorized Military Presence\n'
	return True
