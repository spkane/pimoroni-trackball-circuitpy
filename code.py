import pimoroni_trackball_circuitpy as tb
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

tb.set_leds_magenta()

with tb.device:
    multiplier = 9

    while True:
        down, up, left, right, switch = tb.read()

        # Send movements and clicks to xte
        if switch:
            m.click(Mouse.LEFT_BUTTON)
        else:
            x = right - left
            y = down - up
            m.move(int(-x * multiplier), int(-y * multiplier), 0)
