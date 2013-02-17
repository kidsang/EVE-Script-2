import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time
from Finder import *

def _launch(group):

	# result = None
	# while not result:
	# 	mouse.moveToP(panel.center(panel.Drones))
	# 	mouse.wheel(-100)
	# 	mouse.moveToP(panel.center(panel.Full))
	# 	result = findAtDrones('local_space')
	# mouse.leftClickAtP(result)

	result = None
	while not result:
		mouse.moveToP(panel.center(panel.Drones))
		mouse.wheel(100)
		mouse.moveToP(panel.center(panel.Full))
		result = findAtDrones('bay')

	if group == None:
		mouse.rightClickAtP(result)
	else:
		if not findAtDrones(group):
			mouse.leftClickAtP(result)
		result = findAtDrones(group)
		while not result:
			time.sleep(0.5)
			result = findAtDrones(group)
		mouse.rightClickAtP(result)

	result = findAtDrones('launch_drones')
	while not result:
		time.sleep(0.5)
		result = findAtDrones('launch_drones')
	mouse.leftClickAtP(result)

	print 'wait until drones launching..'
	mouse.moveToP(panel.center(panel.Full))
	# time.sleep(5)
	while not findAtDrones('idle') and not findAtDrones('fighting') and not findAtDrones('returning'):
		mouse.moveToP(panel.center(panel.Drones))
		mouse.wheel(-100)
		mouse.moveToP(panel.center(panel.Full))
		if not findAtDrones('idle') and not findAtDrones('fighting') and not findAtDrones('returning'):
			result = findAtDrones('local_space')
			if result:
				mouse.leftClickAtP(result)
				mouse.wheel(-100)
				mouse.leftClickAt(result[0], result[1] + 20)

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

	mouse.moveToP(panel.center(panel.Drones))
	mouse.wheel(-100)
	mouse.moveToP(panel.center(panel.Full))

	print 'wait until drones return'
	while findAtDrones('returning') or findAtDrones('fighting') or findAtDrones('idle'):
		key.pressEx(sc.DronesReturn)
		time.sleep(0.2)

	# result = None
	# while not result:
	# 	result = findAtDrones('local_space')
	# mouse.leftClickAtP(result)

	print '<-- drones return\n'
	return True

def engage():
	print '--> drones engaging\n'
	
	key.pressEx(sc.DronesEngage)

	while not findAtDrones('fighting'):
		key.pressEx(sc.DronesEngage)
		time.sleep(0.2)

	print '<-- drones engaging\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	launchSmall()
	back()
	launchSmall()
	back()
