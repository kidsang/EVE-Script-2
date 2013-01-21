import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time

def find(source, threshould = 0.5):
	path = ''
	if __name__ != '__main__':
		path += '../'
	path += 'img/' + source + '.bmp'
	result = pic.findImgR(panel.Drones, path, threshould)
	if not result:
		print 'can not find "' + source + '"!'
	return result

def _launch(group):

	result = find('bay')
	if not result:
		return False

	if group == None:
		mouse.rightClickAtP(result)
	else:
		if not find(group):
			mouse.leftClickAtP(result)
		result = find(group)
		if not result:
			return False
		mouse.rightClickAtP(result)

	result = find('launch_drones')
	if not result:
		return False
	mouse.leftClickAtP(result)
	print 'wait until drones launching..'
	time.sleep(5)

	result = find('local_space')
	if not result:
		return False
	mouse.leftClickAtP(result)
	if not find('idle') and not find('fighting') and not find('returning'):
		mouse.leftClickAt(result[0], result[1] + 20)

	return True

def launch():
	print '--> launch drones'
	ret = _launch(None)
	print '<-- launch drones\n'
	return ret

def launchSmall():
	print '--> launch drones in group "small"'
	ret = _launch('sentry')
	print '<-- launch drones in group "small"\n'
	return ret

def launchSmall():
	print '--> launch drones in group "sentry"'
	ret = _launch('small')
	print '<-- launch drones in group "sentry"\n'
	return ret

def back():
	print '--> drones return'

	key.pressEx(sc.DronesReturn)
	key.pressEx(sc.DronesReturn)
	key.pressEx(sc.DronesReturn)

	print 'wait until drones return'
	while find('returning') or find('fighting') or find('idle'):
		time.sleep(0.1)

	result = find('local_space')
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
