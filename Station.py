import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Picture as pic
import time

def find(rect, source, threshould):
	path = 'img/' + source + '.bmp'
	result = pic.findImgR(rect, path, threshould)
	if not result:
		print 'can not find "' + source + '"!'
	return result

def findAtMenu(source, threshould = 0.5):
	return find(panel.Menu, source, threshould)

def findAtProgressBar(source, threshould = 0.5):
	return find(panel.ProgressBar, source, threshould)

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
	print '<-- repair\n'

if __name__ == '__main__':
	undock()

