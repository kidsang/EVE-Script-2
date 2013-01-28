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
	while findAtProgressBar('initializing_map') or time.time() - begin < 3:
		time.sleep(0.5)
	time.sleep(0.5)
	print '<-- enter star map\n'

def exitStarMap():
	print '--> exit star map'
	key.pressEx(sc.Map)
	time.sleep(2)
	print '<-- exit star map\n'

def enterBlack():
	print '--> enter black'
	enterStarMap()
	mouse.moveToP(panel.center(panel.Full))
	mouse.leftDown()
	mouse.move(500, 200)
	mouse.leftUp()
	print '<-- enter black\n'

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

def backToAgentStation():
	print '--> back to agent station'

	enterStarMap()

	result = findAtInfo('agent_mission')
	if not result:
		return False
	mouse.leftClickAt(result[0] + 20, result[1] + 33)
	time.sleep(1)

	result = findAtInfo('dock')
	if not result:
		return False
	mouse.leftClickAtP(result)

	exitStarMap()

	print 'wait until reach station'
	time.sleep(5)
	while not findAtMenu('undock'):
		time.sleep(1)

	time.sleep(4)

	print '<-- back to agent station\n'
	return True

def openMissionDetails():
	print '--> open mission detail'

	key.pressEx(sc.Journal)

	result = None
	while not result:
		time.sleep(0.2)
		result = findAtFull('accepted')
	mouse.doubleClickAtP(result)

	print 'wait to open mission details'
	while not findAtMissionDetails('mission_journal'):
		time.sleep(0.2)

	while not findAtMissionDetails('o'):
		mouse.leftClickAt(panel.MissionDetails[0] + 20, panel.MissionDetails[1] + 20)
		mouse.wheel(-20)

	key.pressEx(sc.Journal)
	key.pressEx(sc.Journal)

	print '<-- open mission detail\n'
	return True

def missionObjectiveComplete():
	print '--> judge if mission complete'

	print 'wait until mission complete'
	while not findAtMissionDetails('v'):
		time.sleep(1)

	mouse.moveToP(panel.center(panel.MissionDetails))
	time.sleep(0.5)
	result = findAtMissionDetails('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- judge if mission complete\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	openMissionDetails()
