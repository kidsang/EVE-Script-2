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
	print '--> mission The Spy Stash'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('battle'):
		return False

	if not overview.activateAccelerationGate():
		return False

	# pocket 1 direct access

	ship.enableAfterburn()	

	if not overview.activateAccelerationGate():
		return False

	# pocket 2
	if not drones.launchSmall():
		return False

	ship.enableAfterburn()	

	overview.seekAndDestory()

	if not drones.back():
		return False

	result = findAtOverview('officers')
	if not result:
		return False
	mouse.doubleClickAtP(result)

	print 'wait until cargo open'
	result = None
	while not result:
		time.sleep(0.5)
		result = findAtFull('report')
	mouse.leftDownAtP(result)

	result = findAtFull('ship', 0.5)
	if not result:
		mouse.leftUp()
		return False
	mouse.moveToP(result)
	mouse.leftUp()
	time.sleep(2)

	result = findAtFull('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- mission The Spy Stash\n'
	return True
