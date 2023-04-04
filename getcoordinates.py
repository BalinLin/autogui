#! python3
import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        # x, y = (600, 630)
        x, y = pyautogui.position()
        pcolor = pyautogui.pixel(x, y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' C: ' + str(pcolor).rjust(18)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
