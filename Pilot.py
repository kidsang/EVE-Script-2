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
        for retry in range(3):
            print 'try: ' + str(retry + 1)
            result = findAtOverview('target_station', 0.2)
            if result:
                print 'station finded'
                finded = 'station'
                break
            result = findAtOverview('target_star_gate', 0.2)
            if result:
                print 'stargate finded'
                finded = 'gate'
                break
            x, y = panel.center(panel.Overview)
            y += random.random() * 200 - 100
            mouse.leftClickAt(x, y)
            mouse.wheel(-12)
            mouse.moveToP(panel.center(panel.Full))

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
            result = findAtProgressBar('entering_station', 0.1) 
            while not result and time.time() - begin < 80:
                result = findAtProgressBar('entering_station', 0.1) 
                time.sleep(0.1)
            if result:
                print 'entering station'
                time.sleep(4)
                print '<-- autopilot\n'
                return True

        if finded == 'gate':
            print 'jump...'
            mouse.leftClickAtP(result)
            key.pressEx(sc.Activate)
            print 'wait until entering space'
            begin = time.time()
            result = findAtProgressBar('entering_space', 0.1)
            while not result  and time.time() - begin < 80:
                result = findAtProgressBar('entering_space', 0.1)
                time.sleep(0.1)
            if result:
                print 'entering space'
                time.sleep(3)


if __name__ == '__main__':
    mouse.leftClickAtP(panel.center(panel.Full))
    autopilot()
    pass
