import Picture as pic
import Panel as panel
import os


def find(rect, source, threshould):
	f = 'img/' + source + '.bmp'
	if not os.path.exists(f):
		f = '../' + f
		if not os.path.exists(f):
			print 'source "' + source + '" do not exists!'
			return None
	result = pic.findImgR(rect, f, threshould)
	if not result:
		print 'can not find "' + source + '"!'
	else:
		print '"' + source + '" finded!'
	return result


def findAtFull(source, threshould = 0.1):
	return find(panel.Full, source, threshould)


def findAtMenu(source, threshould = 0.5):
	return find(panel.Menu, source, threshould)

def findAtInfo(source, threshould = 0.1):
	return find(panel.Info, source, threshould)

def findAtDrones(source, threshould = 0.1):
	return find(panel.Drones, source, threshould)

def findAtMissionDetails(source, threshould = 0.1):
	return find(panel.MissionDetails, source, threshould)


def findAtSelectedItem(source, threshould = 0.1):
	return find(panel.SelectedItem, source, threshould)

def findAtOverview(source, threshould = 0.1):
	return find(panel.Overview, source, threshould)

def findAtStationServices(source, threshould = 0.5):
	return find(panel.StationServices, source, threshould)


def findAtProgressBar(source, threshould = 0.1):
	return find(panel.ProgressBar, source, threshould)

def findAtMessage(source, threshould = 0.1):
	return find(panel.Message, source, threshould)

def findAtDashboard(source, threshould = 0.1):
	return find(panel.Dashboard, source, threshould)


def findAtMission(source, threshould = 0.5):
	return find(panel.Mission, source, threshould)

def findAtMissionLeft(source, threshould = 0.5):
	return find(panel.MissionLeft, source, threshould)

def findAtMissionRight(source, threshould = 0.5):
	return find(panel.MissionRight, source, threshould)

def findAtInventory(source, threshould = 0.1):
	return find(panel.Inventory, source, threshould)


if __name__ == '__main__':
	pass
