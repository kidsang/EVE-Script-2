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
	print '--> mission Smuggler lnterteption'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('battle'):
		return False

	# 2 pockets
	for i in range(2):

		if not overview.activateAccelerationGate():
			return False

		print 'pocket ' + str(i+1)

		if not drones.launchSmall():
			return False

		ship.enableAfterburn()	

		overview.seekAndDestory()

		if not drones.back():
			return False

	# loot grustas personal transport
	if not overview.pickTarget('guristas_personnel'):
		return False


	print '<-- mission Smuggler lnterteption\n'
	return True