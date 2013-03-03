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

	overview.seekAndDestory()

	if not drones.back():
		return False

	ship.enableAfterburn()

	if not overview.activateAccelerationGate():
		return False

	# pocket 1
	# main enemies are 90km away
	# approach for 85 secs
	# mean while clean up nearby enemy

	drones.launchSmall()
	
	if not overview.switchTo('battle'):
		return False

	if not overview.lockEnemy(20):
		return False

	ship.fireOnce()

	if not overview.lockTarget('transport', 1):
		return False

	ship.enableAfterburn()

	ship.approachFor(85)

	# wait for stop
	begin = time.time()
	while time.time() - begin < 20:
		ship.stop()
		key.pressEx(sc.Unlock)

	mouse.moveToP(panel.center(panel.Drones))

	mouse.wheel(-100)

	while findAtDrones('fighting'):
		time.sleep(10)

	drones.back()

	# use sentry to destory all the smalls

	for i in range(6):
		overview.lockTarget('s', 1)

	drones.launchSentry()

	begin = time.time()
	while overview.lockTarget('s', 1) and time.time() - begin < 130:
		ship.fireOnce()
		drones.engage()

	drones.back()

	# do the rest

	ship.fireOnce()

	drones.launchSmall()

	overview.seekAndDestory()

	while not overview.pickCargo():
		pass

	drones.back()

	print '<-- mission Intercept The Sabateurs\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	run()