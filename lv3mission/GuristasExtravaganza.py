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
	print '--> mission Guristas Extravaganza'

	if not ship.enableDefense():
		return False

	# pocket 1 - 3
	for i in range(3):

		if not overview.activateAccelerationGate():
			return False

		print 'pocket ' + str(i+1)

		if not drones.launchSmall():
			return False

		ship.enableAfterburn()	

		overview.seekAndDestory()

		if not drones.back():
			return False

	# in pocket 3, we must destory the powerfull em force field to continue

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('em_forcefield'):
		return False

	if not drones.launchSmall():
		return False

	if not drones.engage():
		return False

	print 'wait until force field destoried'
	time.sleep(20)
	while findAtDrones('fighting'):
		time.sleep(1)

	if not drones.back():
		return False

	# pocket 4 - 5
	for i in range(2):

		if not overview.activateAccelerationGate():
			return False

		print 'pocket ' + str(i+4)

		if not drones.launchSmall():
			return False

		ship.enableAfterburn()	

		overview.seekAndDestory()

		if not drones.back():
			return False

	print '<-- mission Guristas Extravaganza\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	run()