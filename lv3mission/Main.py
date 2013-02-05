import sys
sys.path.append('..')

import Mouse as mouse
import Panel as panel
import Picture as pic
import Pilot as pilot
import Station as station
import General as general
import Overview as overview
from Finder import *
import time

import TheSpyStash as the_spy_stash
import EliminateThePirateCampers as eliminate_the_pirate_campers
import TheDamselInDistress as the_damsel_in_distress
import PickYourPosition as pick_your_position
import PirateInvasion as pirate_invasion
import DeadlyArrival as deadly_arrival
import RogueDroneHarassment as rouge_drone_harassment
import TechnologicalSecrets1 as technological_secrets_1
import TechnologicalSecrets2 as technological_secrets_2
import TechnologicalSecrets3 as technological_secrets_3
import TheGuristasSpies as the_guristas_spies
import SuccessComesAtAPrice as success_comes_at_a_price
import SeekAndDestory as seek_and_destory
import BreakTheirWill as break_their_will
import GuristasExtravaganza as guristas_extravaganza
import StopTheThief as stop_the_thief
import Smugglerlnterteption as smuggler_lnterteption
import InterceptThePirateSmugglers as intercept_the_pirate_smugglers
import WhatComesAroundGoesAround as what_comes_around_goes_around
import DuoOfDeath as duo_of_death
import TheScore as the_score
import TheBlackMarketHub as the_black_market_hub
import UnauthorizedMilitaryPresence as unauthorized_military_presence
import InterceptTheSabateurs as intercept_the_sabateurs
import CargoDeliver as cargo_deliver
import TheRogueSlaveTrader1 as the_rogue_slave_trade_1
import DowningTheSlavers2 as downing_the_slavers_2
import AngelExtravaganza as angel_extravaganza
import SilenceTheInformat as silence_the_informat
import NewFrontiers1 as new_frontiers_1
import NewFrontiers2 as new_frontiers_2
import NewFrontiers3 as new_frontiers_3
import NewFrontiers4 as new_frontiers_4
import NewFrontiers5 as new_frontiers_5
import NewFrontiers6 as new_frontiers_6
import NewFrontiers7 as new_frontiers_7
import GoneBerserk as gone_berserk
import TheMissingConvoy as the_missing_convoy
import TheSpaceTelescope as the_space_telescope
import CutThroatCompetition as cut_throat_competition
import Retribution as retribution

agent = 'img/agent.bmp'

battle = {
			'The Spg Stash':the_spy_stash,
			'Eliminate the Pirate Campers':eliminate_the_pirate_campers,
			'The Damsel In Distress':the_damsel_in_distress,
			# 'Pink \*nur Poison':pick_your_position,
			'Pirate Invasion':pirate_invasion,
			'Deadlg Arrival':deadly_arrival,
			'Rogue Drone Harassment':rouge_drone_harassment,
			'Tenhnalaginal Secrets (1 of 3)':technological_secrets_1,
			'Tenhnalaginal Secrets (3 of 3)':technological_secrets_3,
			'The Guristas Spies':the_guristas_spies,
			'Sunness Comes At A Price':success_comes_at_a_price,
			'Seek and Destmg':seek_and_destory,
			'Break Their Will':break_their_will,
			'Guristas Extravaganza':guristas_extravaganza,
			'Stop The Thief':stop_the_thief,
			'Smuggler lnterteption':smuggler_lnterteption,
			'lntertept The Pirate Smugglers':intercept_the_pirate_smugglers,
			'What Comes Around Goes Around':what_comes_around_goes_around,
			'Dun of Death':duo_of_death,
			'The Snare':the_score, 
			'The Blank Market Hub':the_black_market_hub,
			'Unauthorized Militarg Presence':unauthorized_military_presence,
			'Intercept The Sabateurs':intercept_the_sabateurs,
			'Cargo Deliverg':cargo_deliver,
			'The Rogue Slave Trader (1 of 2)':the_rogue_slave_trade_1,
			'Dawning The Slavers (2 of 2)':downing_the_slavers_2,
			'Angel Extravaganza':angel_extravaganza,
			'Silence The Informant':silence_the_informat,
			'New Frontiers - Raw Materials (1 of 1*]':new_frontiers_1,
			'New Frontiers - Mad Snientist (2 of 1*)':new_frontiers_2,
			'New Frontiers - The Unveiling (4 of 1*)':new_frontiers_4,
			'New Frontiers - An Unexpected Twist (':new_frontiers_5,
			# 'New Frontiers - Asnendanne (? of 1*)':new_frontiers_7, #heavy damage
			'Gone Berserk':gone_berserk,
			'The Missing Canvog':the_missing_convoy,
			'The Spate Telescope':the_space_telescope,
			'Cut-Throat Competition':cut_throat_competition,
			'Retributinn':retribution,
		}

transport = {
				'Tenhnalaginal Secrets (2 of 3)':technological_secrets_2,
				'New Frontiers - Toward a Solution (3 a':new_frontiers_3,
				'New Frontiers - Nanite Express (5 of ?':new_frontiers_6,
			}

skip = [
		'Lights Out', # gallent standing
		'The Blnnkade', # will attack drones, heavy damage, heavy shield
		'Illegal Mtivitg (1 of 3)', # gallent stading
		'The Good Word', # gate seens never unlock
		'Driving a Wedge - Get the Gallants (1 of', # gallent stading
		]


def run():
	print 'mission bot begin.\n'

	while True:

		if not station.startConversation(agent):
			print 'Error: Could not find target agent.'
			return False

		mission = pic.extractTextR(panel.MissionName).strip()
		missionType = ''
		print mission
		if mission in battle:
			missionType = 'b'
		elif mission in transport:
			missionType = 't'
		elif mission in skip:
			if not station.declineMission():
				return False
			else:
				continue
		else:
			print 'Error: Cant find bot for mission \'' + mission + '\'.'
			return False

		record(mission, 'begin')

		if not station.acceptMission():
			print 'Error: Accept mission failed.'
			return False

		# mouse.moveToP(panel.center(panel.Mission))
		# result = findAtFull('x')
		# if not result:
		# 	return False
		# mouse.leftClickAtP(result)

		if not general.setMissionWaypoint():
			print 'Error: Cant set mission waypoint.'
			return False

		if missionType == 'b':
			if not runBattle(mission):
				return False
		elif missionType == 't':
			if not runTransport(mission):
				return False

		record(mission, 'complete')

def runBattle(mission):
	print 'battle mission'
	bot = battle[mission]
	# bot = the_damsel_in_distress

	if bot == pick_your_position:
		if not station.activateShip('shuttle'):
			return False

	if not station.undock():
		return False

	pilot.autopilot()

	if not general.warpToMissionLocation():
		return False

	if not bot.run():
		return False

	if general.setMissionWaypoint():
		pilot.autopilot()
	else:
		mouse.leftClick()
		general.exitStarMap()
		general.backToAgentStation()

	if not station.startConversation(agent):
		return False

	if not station.completeMission():
		return False

	if not station.repair():
		print 'Error: repair faild'
		return False

	if bot == pick_your_position:
		if not station.activateShip('dominix'):
			return False

	return True

def runTransport(mission):
	print 'transport mission'
	bot = transport[mission]

	if not bot.run():
		return False

	return True

def record(mission, action):
	f = open('mission.log', 'a')
	f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	f.write('\t\t' + mission + '[' + action + ']' + '\n')
	f.close()


if __name__ == '__main__':
	mouse.leftClickAtP(panel.center(panel.Full))
	run()
	# runBattle('')


