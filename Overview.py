import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import General as general
import time
import random
from Finder import *

def findTarget(target):
	print '--> find target "' + target + '"'
	count = 0
	result = None
	result = findAtOverview(target)
	while result == None and count < 10:
		if result:
			break
		x, y = panel.center(panel.Overview)
		y += random.random() * 200 - 100
		mouse.leftClickAt(x, y)
		if count < 5:
			mouse.wheel(-20)
		else:
			mouse.wheel(20)
		count += 1
		result = findAtOverview(target)

	if not result:
		print 'can not find target.'
	else:
		print 'target finded.'

	print '<-- find target "' + target + '"\n'
	return result

def lockTarget(target, wait = 5):
	print '--> lock target "' + target + '"'

	result = findTarget(target)
	if not result:
		return False

	mouse.leftClickAtP(result)
	key.pressEx(sc.Lock)
	time.sleep(wait)

	print '<-- lock target "' + target + '"\n'
	return True

def activateAccelerationGate():
	print '--> activate acceleration gate\n'

	general.enterStarMap()

	mouse.leftDownAtP(panel.center(panel.Full))
	mouse.move(500, 200)
	mouse.leftUp()

	result = findTarget('acceleration_gate')
	if not result:
		return False
	mouse.leftClickAtP(result)
	key.pressEx(sc.Activate)

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

	general.exitStarMap()

	print '<-- activate acceleration gate\n'
	return True

def pickWreck():
	print '--> picking wreck'

	result = findTarget('wreck')
	if not result:
		return False
	mouse.doubleClickAtP(result)

	print 'wait until cargo open'
	result = None
	while not result:
		time.sleep(0.2)
		result = findAtFull('loot_all')
	mouse.leftClickAtP(result)

	time.sleep(2)
	result = findAtFull('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- picking wreck\n'
	return True

def pickCargo():
	print '--> picking cargo'

	result = findTarget('cargo')
	if not result:
		return False
	mouse.doubleClickAtP(result)

	print 'wait until cargo open'
	result = None
	while not result:
		time.sleep(0.2)
		result = findAtFull('loot_all')
	mouse.leftClickAtP(result)

	time.sleep(2)
	result = findAtFull('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- picking cargo\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	activateAccelerationGate()
	pass
