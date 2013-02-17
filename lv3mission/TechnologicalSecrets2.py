import sys
sys.path.append('..')

import Panel as panel
import Picture as pic
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Station as station
import Overview as overview
import General as general
import Drones as drones
import Ship as ship
import Pilot as pilot
import time
from Finder import *

agent = 'img/agent.bmp'
def run():
	print '--> mission Technological Secrets 2'

	# this is a transport mission
	if not (station.openInventory() \
		and station.loadItem('dna_sample') \
		and station.closeInventory()):
		return False

	if not station.undock():
		return False

	pilot.autopilot()

	if not general.setMissionWaypoint():
		return False

	if not station.startConversation(agent):
		return False

	if not station.completeMission():
		return False

	if not station.undock():
		return False

	pilot.autopilot()

	print '<-- mission Technological Secrets 2\n'
	return True

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	run()