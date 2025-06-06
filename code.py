import time

import pimoroni_trackball_circuitpy as tb
import usb_hid
from adafruit_hid.mouse import Mouse

old_coord = (0, 0, 0)

m = Mouse(usb_hid.devices)

tb.set_leds_red()

multiplier = 9

tb.set_leds_green()

lastSetTime = time.monotonic()

while True:
    up, down, left, right, switch = tb.read()

    # Enact movements and clicks
    if switch:
        m.click(Mouse.LEFT_BUTTON)
        print(f"BUTN↓")
    else:
        x = right - left
        y = down - up
        xmult = int(-x * multiplier)
        ymult = int(-y * multiplier)
        new_coord = (xmult, ymult, 0)
        if new_coord != old_coord:
            timeNow = time.monotonic()
            if timeNow - lastSetTime > 2:
                print(f"MOUS↑↓←→")
                lastSetTime = time.monotonic()
        m.move(xmult, ymult, 0)
