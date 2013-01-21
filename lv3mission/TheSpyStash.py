import Panel as panel
import Mouse as mouse
import Keyboard as key
import Shortcut as sc
import Station as station
import Overview as overview

def run():
	print '--> mission The Spy Stash'

	if not overview.activateAccelerationGate():
		return False

	print '<-- mission The Spy Stash\n'