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
import time
from Finder import *

def run():
	print '--> mission The Damsel In Distress'

	if not ship.enableDefense():
		return False

	if not overview.switchTo('lcs'):
		return False

	if not overview.lockTarget('pleasure_hub'):
		return False

	if not ship.approach():
		return False

	if not ship.enableAfterburn():
		return False

	if not drones.launchSmall():
		return False

	if not ship.fireOnce():
		return False

	if not drones.engage():
		return False

	#there are two cargos
	count = 0;
	while count < 2:
		if overview.pickCargo():
			count += 1
			time.sleep(2)

	if not drones.back():
		return False

	print '<-- mission The Damsel In Distress\n'
	return True