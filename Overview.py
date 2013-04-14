import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import General as general
import Ship as ship
import time
import random
from Finder import *

def switchTo(name):
	print '--> switch overview setting to ' + name

	trycount = 0
	success = False
	while not success and trycount < 3:
		success = True
		trycount += 1
		result = findAtOverview('overview')
		if not result:
			success = False
		mouse.leftClickAtP(result)
		mouse.moveTo(result[0] - 400, result[1])
		time.sleep(0.5)

		result = findAtOverview(name)
		if not result:
			success = False
		mouse.leftClickAtP(result)
		time.sleep(0.5)

		if not success:
			mouse.leftClickAtP(panel.center(panel.Full))

	if not success:
		return False

	print '<-- switch overview setting to ' + name + '\n'
	return True


def findTarget(target, threashould = 0.1):
	print '--> find target "' + target + '"'
	count = 0
	result = findAtOverview(target, threashould)
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

	result = findTarget(target)
	if not result:
		return False

	print '--> lock target "' + target + '"'

	mouse.leftClickAtP(result)
	key.pressEx(sc.Lock)
	print 'wait for ' + str(wait) + ' seconds'
	time.sleep(wait)

	print '<-- lock target "' + target + '"\n'
	return True

def findEnemy():
	print '--> find enemy'
	count = 0
	result = pic.findColorR(panel.Overview, 'c11313')
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
		result = pic.findColorR(panel.Overview, 'c11313')

	if not result:
		print 'can not find enemy.'
	else:
		print 'target finded.'

	print '<-- find enemy'
	return result

def lockEnemy(wait = 5):
	print '--> lock enemy'

	result = findEnemy()
	if not result:
		return False

	mouse.leftClickAtP(result)
	key.pressEx(sc.Lock)
	print 'wait for ' + str(wait) + ' seconds'
	time.sleep(wait)

	print '<-- lock enemy'
	return True

def handleDangerousAction():
	result = findAtFull('dangerous')
	if result:
		mouse.moveToP(result)
		result = None
		while not result:
			result = findAtFull('x')
		mouse.leftClickAtP(result)
		key.pressEx(sc.Unlock)
		return True
	else:
		return False

def activateAccelerationGate():
	switchTo('pilot')
	general.enterStarMap()

	print '--> activate acceleration gate\n'

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
		handleDangerousAction();
		key.pressEx(sc.Activate)
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

	print '<-- activate acceleration gate\n'

	general.exitStarMap()
	
	return True

def pickWreck():
	print '--> picking wreck'

	result = findTarget('wreck')
	if not result:
		return False
	mouse.doubleClickAtP(result)

	print 'wait until cargo open'
	result = None
	begin = time.time()
	while not result and time.time() - begin < 120:
		time.sleep(0.2)
		result = findAtFull('loot_all')
	if not result:
		return False
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
	begin = time.time()
	while not result and time.time() - begin < 240:
		time.sleep(0.2)
		result = findAtFull('loot_all')
	if not result:
		return False
	mouse.leftClickAtP(result)

	time.sleep(2)
	result = findAtFull('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- picking cargo\n'
	return True

def pickTarget(target):
	print '--> picking wreck'

	result = findTarget(target)
	if not result:
		return False
	mouse.doubleClickAtP(result)

	print 'wait until cargo open'
	result = None
	begin = time.time()
	while not result and time.time() - begin < 120:
		time.sleep(0.2)
		result = findAtFull('loot_all')
	if not result:
		return False
	mouse.leftClickAtP(result)

	time.sleep(2)
	result = findAtFull('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- picking wreck\n'
	return True

def seekAndDestory():

	switchTo('battle')

	print '--> seek and destory'

	while not findAtMissionDetails('v'):
		# if findAtDrones('fighting'):
		# 	time.sleep(5)
		# elif lockEnemy():
		if lockEnemy():
			mouse.moveTo(200, 200)
			time.sleep(10)
			ship.approach()
			ship.fireOnce()
			time.sleep(5)
		else:
			break

	print '<-- seek and destory\n'

	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	handleDangerousAction()
