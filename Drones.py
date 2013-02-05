import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time
from Finder import *

def _launch(group):

	result = findAtDrones('local_space')
	if not result:
		return False
	mouse.leftClickAtP(result)

	result = findAtDrones('bay')
	if not result:
		return False

	if group == None:
		mouse.rightClickAtP(result)
	else:
		if not findAtDrones(group):
			mouse.leftClickAtP(result)
		result = findAtDrones(group)
		if not result:
			return False
		mouse.rightClickAtP(result)

	result = findAtDrones('launch_drones')
	if not result:
		return False
	mouse.leftClickAtP(result)
	print 'wait until drones launching..'
	mouse.moveTo(result[0] + 300, result[1])
	time.sleep(5)

	while not findAtDrones('idle') and not findAtDrones('fighting') and not findAtDrones('returning'):
		mouse.moveToP(panel.center(panel.Drones))
		mouse.wheel(-100)
		mouse.moveToP(panel.center(panel.Full))
		result = findAtDrones('local_space')
		if result:
			mouse.leftClickAt(result[0], result[1] + 20)

	mouse.moveToP(panel.center(panel.Drones))
	mouse.wheel(-100)
	mouse.moveToP(panel.center(panel.Full))

	return True

def launch():
	print '--> launch drones'
	ret = _launch(None)
	print '<-- launch drones\n'
	return ret

def launchSmall():
	print '--> launch drones in group "small"'
	ret = _launch('small')
	print '<-- launch drones in group "small"\n'
	return ret

def launchSentry():
	print '--> launch drones in group "sentry"'
	ret = _launch('sentry')
	print '<-- launch drones in group "sentry"\n'
	return ret

def back():
	print '--> drones return'

	key.pressEx(sc.DronesReturn)
	key.pressEx(sc.DronesReturn)
	key.pressEx(sc.DronesReturn)

	print 'wait until drones return'
	while findAtDrones('returning') or findAtDrones('fighting') or findAtDrones('idle'):
		time.sleep(0.1)

	result = findAtDrones('local_space')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- drones return\n'
	return True

def engage():
	print '--> drones engaging\n'
	key.pressEx(sc.DronesEngage)
	key.pressEx(sc.DronesEngage)
	key.pressEx(sc.DronesEngage)
	print '<-- drones engaging\n'
	return True

if __name__ == '__main__':
	launch()
	back()
