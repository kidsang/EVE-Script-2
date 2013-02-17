import win32api as api
import win32con as con
import re
import string
import time

cd = 0.5

def down(vkcode):
    api.keybd_event(vkcode, 0, 0, 0)
    time.sleep(cd)

def up(vkcode):
    api.keybd_event(vkcode, 0, con.KEYEVENTF_KEYUP, 0)
    time.sleep(cd)

def press(vkcode):
    api.keybd_event(vkcode, 0, 0, 0)
    api.keybd_event(vkcode, 0, con.KEYEVENTF_KEYUP, 0)
    time.sleep(cd)

# vk map
vkmap = {}
# a - z
for i in range(65, 91):
    vkmap[string.lowercase[i - 65]] = i
# 0 - 9
for i in range(48, 58):
    vkmap[i - 48] = i
# f1 - f12
for i in range(112, 124):
    vkmap['f' + str(i - 111)] = i
# direction
vkmap['left'] = 37
vkmap['up'] = 38
vkmap['right'] = 39
vkmap['down'] = 40
# control
vkmap['shift'] = 16
vkmap['ctrl'] = 17
vkmap['alt'] = 18
# other
vkmap['space'] = 32

def parseInput(input):
    '''
    parse input string to vk codes
    all params are in lower case
    input: 'a'
    return [65]
    input: 'ctrl+shift+a'
    return [17, 16, 65]
    input: 'f1'
    return 112
    '''
    pat = re.compile(r'\s*\+\s*')
    tokens = pat.split(input.strip())
    vkcodes = []
    for tk in tokens:
        vkcodes.append(vkmap[tk])
    return vkcodes

def downEx(input):
    vkcodes = parseInput(input)
    for code in vkcodes:
        down(code)

def upEx(input):
    vkcodes = parseInput(input)
    for code in vkcodes:
        up(code)

def pressEx(input):
    vkcodes = parseInput(input)
    for code in vkcodes:
        down(code)
    for code in vkcodes:
        up(code)

def test():
    pass

if __name__ == '__main__':
    test()