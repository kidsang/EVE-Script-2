import win32api as api
import win32con as con
import re
import string
import time

innercd = 0.1
cd = 0.5

# vk map
vkmap = {}
# a - z
for i in range(65, 91):
    vkmap[string.lowercase[i - 65]] = i
# 0 - 9
for i in range(48, 58):
    vkmap[str(i - 48)] = i
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

vkstrpat = re.compile(r'\s*\+\s*')

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
    global vkstrpat
    tokens = vkstrpat.split(input.strip())
    vkcodes = [vkmap[tk] for tk in tokens]
    return vkcodes

def down(vkcodes):
    for code in vkcodes:
        api.keybd_event(code, 0, 0, 0)
        time.sleep(innercd)
    time.sleep(cd)

def up(vkcodes):
    for code in vkcodes:
        api.keybd_event(code, 0, con.KEYEVENTF_KEYUP, 0)
        time.sleep(innercd)
    time.sleep(cd)

def downEx(input):
    down(parseInput(input))

def upEx(input):
    up(parseInput(input))

def pressEx(input):
    vkcodes = parseInput(input)
    down(vkcodes)
    up(vkcodes)

if __name__ == '__main__':
    print parseInput('ctrl+1')
    pass
