import time
import Keyboard as key
import Mouse as mouse
import Picture as pic
import Panel as panel
import Shortcut as sc
import Overview as overview
import random
from Finder import *

def autopilot():
    print '--> autopilot'

    overview.switchTo('pilot')

    while True:
        print 'try to find target stargate or station'
        finded = ''
        result = None
        for retry in range(7):
            mouse.moveToP(panel.center(panel.Full))
            print 'try: ' + str(retry + 1)
            result = find(panel.Overview, 'target_station', 0.2)
            if result:
                print 'station finded'
                finded = 'station'
                break
            result = find(panel.Overview, 'target_star_gate', 0.2)
            if result:
                print 'stargate finded'
                finded = 'gate'
                break
            x, y = panel.center(panel.Overview)
            y += random.random() * 200 - 100
            mouse.leftClickAt(x, y)
            mouse.wheel(-12)

        if finded == '':
            print "can't find any waypoint"
            print '<-- autopilot\n'
            return False

        if finded == 'station':
            print 'docking...'
            mouse.leftClickAtP(result)
            key.pressEx(sc.Activate)
            print 'wait until entering station'
            begin = time.time()
            while not find(panel.ProgressBar, 'entering_station', 0.1) and time.time() - begin < 80:
                time.sleep(0.1)
            print 'entering station'
            time.sleep(4)
            print '<-- autopilot\n'
            return True

        if finded == 'gate':
            print 'jump...'
            mouse.leftClickAtP(result)
            key.pressEx(sc.Warp)
            time.sleep(1)
            key.pressEx(sc.Activate)
            print 'wait until entering space'
            begin = time.time()
            while not find(panel.ProgressBar, 'entering_space', 0.1) and time.time() - begin < 80:
                time.sleep(0.1)
            print 'entering space'
            time.sleep(4)


if __name__ == '__main__':
    mouse.leftClickAtP(panel.center(panel.Full))
    autopilot()
    pass
