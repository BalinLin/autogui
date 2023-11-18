import pyautogui
import pydirectinput
import time

delaySecond = 0.05
x, y = (640, 610)
xSpace, ySpace = (740, 810)

print('Press Ctrl-C to quit.')
def keywithdelay(command = "", delay = delaySecond):
    if command:
        pydirectinput.press(command)
        time.sleep(delay)

try:
    while True:
        pcolor = pyautogui.pixel(x, y)
        pcolorSpace = pyautogui.pixel(xSpace, ySpace)

        if pcolorSpace[0] >= 200 and pcolorSpace[1] >= 200 and pcolorSpace[2] >= 200: keywithdelay('space')
        else:
            if pcolor[0] >= 200: keywithdelay('up')
            elif pcolor[1] >= 200: keywithdelay('left')
            elif pcolor[2] >= 200: keywithdelay('right')

except KeyboardInterrupt:
    print('\n')
