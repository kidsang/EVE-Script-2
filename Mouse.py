import win32api as api
from win32api import GetSystemMetrics
import win32con as con
import time

innercd = 0.1
cd = 0.5
winWidth = GetSystemMetrics(0)
winHeight = GetSystemMetrics(1)
densx = 65535.0 / winWidth
densy = 65535.0 / winHeight

def moveTo(x, y):
    absX = int(x * densx)
    absY = int(y * densy)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(cd)

def moveToP(point):
    moveTo(point[0], point[1])

def leftDownAt(x, y):
    absX = int(x * densx)
    absY = int(y * densy)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(innercd)
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(cd)

def leftDownAtP(point):
    leftDownAt(point[0], point[1])

def leftClickAt(x, y):
    absX = int(x * densx)
    absY = int(y * densy)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(innercd)
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN | con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def leftClickAtP(point):
    leftClickAt(point[0], point[1])
    
def rightDownAt(x, y):
    absX = int(x * densx)
    absY = int(y * densy)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(innercd)
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(cd)

def rightDownAtP(point):
    rightDownAt(point[0], point[1])

def rightClickAt(x, y):
    absX = int(x * densx)
    absY = int(y * densy)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(innercd)
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN | con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(innercd)
    time.sleep(cd)

def rightClickAtP(point):
    rightClickAt(point[0], point[1])

def doubleClickAt(x, y):
    absX = int(x * densx)
    absY = int(y * densy)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(innercd)
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN | con.MOUSEEVENTF_LEFTUP, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN | con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def doubleClickAtP(point):
    doubleClickAt(point[0], point[1])

def move(dx, dy):
    api.mouse_event(con.MOUSEEVENTF_MOVE, dx, dy)
    time.sleep(cd)

def moveP(point):
    move(point[0], point[1])

def leftDown():
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(cd)

def leftUp():
    api.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def leftClick():
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def rightDown():
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(cd)

def rightUp():
    api.mouse_event(con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(cd)

def rightClick():
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN | con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(cd)

def doubleClick():
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN | con.MOUSEEVENTF_LEFTUP, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN | con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def wheel(dz):
    """
    scroll up when dz > 0
    scroll down when dz < 0
    """
    api.mouse_event(con.MOUSEEVENTF_WHEEL, 0, 0, dz * con.WHEEL_DELTA)
    time.sleep(cd)

def test():
    leftClick()
    pass

if __name__ == '__main__':
    test()
