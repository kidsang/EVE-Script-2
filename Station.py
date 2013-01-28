import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time
from Finder import *

def undock():
	print '--> undock'

	result = findAtMenu('undock')
	if not result:
		return False
	mouse.leftClickAtP(result)
	mouse.moveTo(result[0] + 200, result[1])

	print 'wait until undock'
	while findAtMenu('undock'):
		time.sleep(0.5)

	print 'wait until entering space'
	begin = time.time()
	while not findAtProgressBar('entering_space') and time.time() - begin < 10:
		time.sleep(0.1)

	time.sleep(3)

	print '<-- undock\n'
	return True

def repair():
	print '--> repair'

	result = findAtStationServices('repair_shop')
	if not result:
		return
	mouse.leftClickAtP(result)

	print 'wait until open repair facilities'
	result = None
	while not result:
		result = findAtFull('repair_facilities')
		time.sleep(0.2)
	mouse.leftClickAt(result[0], result[1] + 70)
	key.pressEx('ctrl+a')

	result = findAtFull('repair_item')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print 'wait...'
	while not findAtFull('pick_new_item'):
		time.sleep(0.2)

	result = findAtFull('repair_all')
	if result:
		mouse.leftClickAtP(result)
		print 'repairing...'
		result = findAtFull('ok')
		if not result:
			result = findAtFull('yes')
		mouse.leftClickAtP(result)
		result = findAtFull('repair_facilities')
		mouse.moveToP(result)
	else:
		print 'nothing to repair'

	result = findAtFull('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- repair\n'
	return True

def openInventory():
	print '--> open inventory'

	key.pressEx(sc.Inventory)
	mouse.moveToP(panel.center(panel.Inventory))
	while not findAtInventory('x'):
		time.sleep(0.2)

	print '<-- open inventory\n'
	return True

def closeInventory():
	print '--> close inventory'

	key.pressEx(sc.Inventory)
	time.sleep(1)

	print '<-- close inventory\n'
	return True


def loadItem(item):
    print '--> load item ' + item

    result = findAtInventory('item_hangar', 0.5)
    if not result:
    	return False
    mouse.leftClickAtP(result)
    time.sleep(2)

    result = findAtInventory(item)
    while not result:
        mouse.moveToP(panel.center(panel.Inventory))
        mouse.wheel(-12)
        mouse.moveTo(100, 100)
        result = findAtInventory(item)

    mouse.leftDownAtP(result)
    result = findAtInventory('ship', 0.5)
    if not result:
    	mouse.leftUp()
    	return False
    mouse.moveToP(result)
    mouse.leftUp()
    time.sleep(1)

    print '<-- load item ' + item + '\n'
    return True

def unloadItem(item):
    print '--> unload item ' + item

    result = findAtInventory('ship', 0.5)
    if not result:
    	return False
    mouse.leftClickAtP(result)
    time.sleep(2)

    result = findAtInventory(item)
    while not result:
        mouse.moveToP(panel.center(panel.Inventory))
        mouse.wheel(-12)
        mouse.moveTo(100, 100)
        result = findAtInventory(item)

    mouse.leftDownAtP(result)
    result = findAtInventory('item_hangar', 0.5)
    if not result:
    	mouse.leftUp()
    	return False
    mouse.moveToP(result)
    mouse.leftUp()
    time.sleep(1)

    print '<-- unload item ' + item + '\n'
    return True

def activateShip(ship):
	print '--> activate ship "' + ship + '"'

	key.pressEx(sc.ShipHangar)
	time.sleep(3)

	result = findAtInventory(ship)
	if not result:
		print 'can not find ' + ship
		return False
	mouse.rightClickAtP(result)
	mouse.moveTo(result[0] + 200, result[1])

	result = findAtInventory('make_active')
	if result:
		mouse.leftClickAtP(result)

	key.pressEx(sc.ShipHangar)
	time.sleep(2)

	print '<-- activate ship "' + ship + '"\n'
	return True

def startConversation(agent):
	print '--> start conversation'

	result = pic.findImgR(panel.StationServices, agent)
	if not result:
		return False
	mouse.doubleClickAtP(result)

	print 'wait until conversation start'
	while not findAtMissionLeft('info'):
		time.sleep(0.2)

	print '<-- start conversation\n'
	return True

def acceptMission():
	print '--> accept mission'

	result = findAtMissionRight('accept')
	if not result:
		return False
	mouse.leftClickAtP(result)
	mouse.moveTo(result[0], result[1] - 80)

	print 'wait until accepting mission'
	while not findAtMissionRight('complete_mission'):
		time.sleep(0.2)
	time.sleep(0.5)

	result = findAtMissionRight('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- accept mission\n'
	return True

def completeMission():
	print '--> complete mission\n'

	result = findAtMissionRight('complete_mission')
	if not result:
		return False
	mouse.leftClickAtP(result)
	mouse.moveTo(result[0], result[1] - 100)

	print 'wait until complete mission'
	while not findAtMissionRight('request_mission'):
		time.sleep(0.2)

	result = findAtMissionRight('x')
	if not result:
		return False
	mouse.leftClickAtP(result)

	print '<-- complete mission\n'
	return True


if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	repair()


