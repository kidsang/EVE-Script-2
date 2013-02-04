import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time
from Finder import *

def enableDefense():
	print '--> enable defense'
	key.pressEx(sc.LowSlot1)
	key.pressEx(sc.LowSlot2)
	key.pressEx(sc.LowSlot3)
	print '<-- enable defense\n'
	return True

def enableAfterburn():
	print '--> enable afterburn'
	key.pressEx(sc.MiddleSlot1)
	print '<-- enable afterburn\n'
	return True

def approach():
	print '--> approaching target'
	key.pressEx(sc.Approach)
	print '<-- approaching target\n'
	return True

def approachFor(second):
	print '--> approaching target'

	key.pressEx(sc.Approach)

	while second > 0:
		time.sleep(1)
		second -= 1
		if second % 5 == 0:
			print str(second) + "second's left"

	print '<-- approaching target\n'
	return True

def fireOnce():
	print '--> establishing hatred'
	key.pressEx(sc.HeightSlot1)
	time.sleep(1)
	key.pressEx(sc.HeightSlot1)
	print '<-- establishing hatred\n'
	return True

def mine():
	print '--> mine'
	key.pressEx(sc.HeightSlot2)
	key.pressEx(sc.HeightSlot3)
	print '<-- mine\n'
	return True


if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	enableAfterburn()
