import sys
sys.path.append('..')

import Mouse as mouse
import Panel as panel
import Picture as pic
import Pilot as pilot
import Station as station
import General as general
import Overview as overview

import TheSpyStash as the_spy_stash

agent = 'img/agent.bmp'

battle = {
			'The Spg Stash':the_spy_stash,
		}

transport = {}


def run():
	print 'mission bot begin.\n'

	while True:

		# if not station.startConversation(agent):
		# 	print 'Error: Could not find target agent.'
		# 	return False

		# mission = pic.extractTextR(panel.MissionName).strip()
		# missionType = ''
		# if mission in battle:
		# 	missionType = 'b'
		# elif mission in transport:
		# 	missionType = 't'
		# else:
		# 	print 'Error: Cant find bot for mission \'' + mission + '\'.'
		# 	return False

		# if not station.acceptMission():
		# 	print 'Error: Accept mission failed.'
		# 	return False

		if not general.setMissionWaypoint():
			print 'Error: Cant set mission waypoint.'
			return False

		if missionType == 'b':
			if not runBattle(mission):
				return False
		elif missionType == 't':
			if not runTransport(mission):
				return False

		if not station.repair():
			print 'Error: repair faild'
			return False

def runBattle(mission):
	# bot = battle[mission]
	bot = the_spy_stash

	# if not station.undock():
	# 	return False

	# pilot.autopilot()

	if not general.warpToMissionLocation():
		return False

	return False

def runTransport(mission):
	return False

if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	# run()
	# runBattle('')
	# overview.activateAccelerationGate()


