import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import Pilot as pilot
import time
from Finder import *

def enterStarMap():
	print '--> enter star map'
	key.pressEx(sc.Map)
	begin = time.time()
	while findAtProgressBar('initializing_map') or time.time() - begin < 3:
		time.sleep(0.5)
	mouse.moveToP(panel.center(panel.Full))
	mouse.wheel(100)
	print '<-- enter star map\n'

def exitStarMap():
	print '--> exit star map'
	key.pressEx(sc.Map)
	time.sleep(2)
	print '<-- exit star map\n'

def openMissionMenu():
	print '--> open mission menu'

	result = findAtInfo('agent_mission')
	# if not result:
	# 	result = findAtInfo('mission_head')
	# 	if result:
	# 		mouse.leftClickAtP(result)
	# 		time.sleep(1)

	while not result:
		result = findAtInfo('agent_mission')
		time.sleep(1)
	mouse.leftClickAt(result[0] + 60, result[1] + 30)
	time.sleep(1)
	print '<-- open mission menu\n'


def setMissionWaypoint(retry = False):
	print '--> set mission waypoint'

	enterStarMap()

	openMissionMenu()

	while True:
		result = findAtInfo('set_destination')
		if not result and not retry:
			return False
		elif not result:
			time.sleep(1)
			mouse.leftClickAtP(panel.center(panel.Full))
		else:
			break

	mouse.leftClickAtP(result)

	exitStarMap()

	print '<-- set mission waypoint\n'
	return True

def warpToMissionLocation():
	print '--> warp to mission location'

	enterStarMap()

	mouse.moveToP(panel.center(panel.Full))
	mouse.leftDown()
	mouse.move(500, 200)
	mouse.leftUp()

	openMissionMenu()

	result = findAtInfo('warp_to_location')
	while not result:
		result = findAtInfo('warp_to_location')
		time.sleep(1)
	mouse.leftClickAtP(result)

	time.sleep(1)
	
	print 'wait to activate gate'
	while not findAtDashboard('warp_drive_active'):
		result = findAtFull('close')
		if not result:
			result = findAtFull('ok')
		if result:
			mouse.leftClickAtP(result)
			mouse.moveTo(result[0], result[1] - 200)
		time.sleep(1)

	print 'wait until reach location'
	while findAtDashboard('warp_drive_active'):
		time.sleep(0.5)

	result = findAtFull('close')
	if not result:
		result = findAtFull('ok')
	if result:
		mouse.leftClickAtP(result)
		mouse.moveTo(result[0], result[1] - 200)
	time.sleep(1)

	while findAtDashboard('warp_drive_active'):
		time.sleep(0.5)

	exitStarMap()

	print '<-- warp to mission location\n'
	return True

def backToAgentStation():
	print '--> back to agent station'

	if setMissionWaypoint():
		pilot.autopilot()
	else:
		result = findAtInfo('dock')
		while not result:
			result = findAtInfo('dock')
			time.sleep(0.5)
		mouse.leftClickAtP(result)

		exitStarMap()

		print 'wait until reach station'
		time.sleep(10)
		while not findAtMenu('undock'):
			time.sleep(1)

		time.sleep(4)

	print '<-- back to agent station\n'
	return True

def openMissionDetails():
	enterStarMap()

	print '--> open mission detail'

	openMissionMenu()

	result = findAtInfo('read_details')
	while not result:
		result = findAtInfo('read_details')
		time.sleep(0.5)
	mouse.leftClickAtP(result)

	print 'wait until find mission objective'
	while not findAtMissionDetails('o'):
		mouse.leftClickAt(panel.MissionDetails[0] + 20, panel.MissionDetails[1] + 20)
		mouse.wheel(-20)

	print '<-- open mission detail\n'

	exitStarMap()
	return True

def missionObjectiveComplete():
	print '--> judge if mission complete'

	print 'wait until mission complete'
	while not findAtMissionDetails('v'):
		time.sleep(1)

	mouse.moveToP(panel.center(panel.MissionDetails))
	result = None
	while not result:
		time.sleep(0.5)
		result = findAtMissionDetails('x')
	mouse.leftClickAtP(result)

	print '<-- judge if mission complete\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	backToAgentStation()
