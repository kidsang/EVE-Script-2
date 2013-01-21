import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time
from Finder import *

def enterStarMap():
	print '--> enter star map'
	key.pressEx(sc.Map)

	begin = time.time()
	while findAtProgressBar('initializing_map') or time.time() - begin < 2:
		time.sleep(0.2)
	print '<-- enter star map\n'

def exitStarMap():
	print '--> exit star map'
	key.pressEx(sc.Map)
	time.sleep(2)
	print '<-- exit star map\n'

def setMissionWaypoint():
	print '--> set mission waypoint'

	enterStarMap()

	result = findAtInfo('agent_mission')
	if not result:
		return False
	mouse.leftClickAt(result[0] + 20, result[1] + 33)
	time.sleep(1)

	result = findAtInfo('set_destination')
	if not result:
		return False
	mouse.leftClickAtP(result)

	exitStarMap()

	print '<-- set mission waypoint\n'
	return True

def warpToMissionLocation():
	print '--> warp to mission location'

	enterStarMap()

	result = findAtInfo('agent_mission')
	if not result:
		return False
	mouse.leftClickAt(result[0] + 20, result[1] + 33)
	time.sleep(1)

	result = findAtInfo('warp_to_location')
	if not result:
		return False
	mouse.leftClickAtP(result)

	time.sleep(1)

	mouse.moveToP(panel.center(panel.Full))
	mouse.leftDown()
	mouse.move(500, 200)
	mouse.leftUp()

	print 'wait until warp drive active'
	while not findAtDashboard('warp_drive_active'):
		time.sleep(0.5)
	print 'wait until reach location'
	while findAtDashboard('warp_drive_active'):
		time.sleep(0.2)

	exitStarMap()

	print '<-- warp to mission location\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
