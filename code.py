import board
import busio
import usb_hid
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_hid.mouse import Mouse

I2C_ADDRESS = 0x0A
I2C_ADDRESS_ALTERNATIVE = 0x0B

CHIP_ID = 0xBA11
VERSION = 1

REG_LED_RED = 0x00
REG_LED_GRN = 0x01
REG_LED_BLU = 0x02
REG_LED_WHT = 0x03

REG_LEFT = 0x04
REG_RIGHT = 0x05
REG_UP = 0x06
REG_DOWN = 0x07
REG_SWITCH = 0x08
MSK_SWITCH_STATE = 0b10000000

REG_USER_FLASH = 0xD0
REG_FLASH_PAGE = 0xF0
REG_INT = 0xF9
MSK_INT_TRIGGERED = 0b00000001
MSK_INT_OUT_EN = 0b00000010
REG_CHIP_ID_L = 0xFA
RED_CHIP_ID_H = 0xFB
REG_VERSION = 0xFC
REG_I2C_ADDR = 0xFD
REG_CTRL = 0xFE
MSK_CTRL_SLEEP = 0b00000001
MSK_CTRL_RESET = 0b00000010
MSK_CTRL_FREAD = 0b00000100
MSK_CTRL_FWRITE = 0b00001000

# i2c @ address 0xA
m = Mouse(usb_hid.devices)
i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, I2C_ADDRESS)


# intensity of r,g,b,w LEDs from 0-100 e.g. set_leds(100,100,25,50)
def set_leds(r, g, b, w):
    device.write(bytes([REG_LED_RED, r & 0xFF]))
    device.write(bytes([REG_LED_GRN, g & 0xFF]))
    device.write(bytes([REG_LED_BLU, b & 0xFF]))
    device.write(bytes([REG_LED_WHT, w & 0xFF]))


def set_leds_purple():
    set_leds(60, 0, 90, 20)


def set_leds_orange():
    set_leds(99, 63, 8, 0)


def set_leds_yellow():
    set_leds(100, 85, 6, 0)


def set_leds_white():
    set_leds(0, 0, 0, 100)


def i2c_rdwr(data, length=0):
    """Write and optionally read I2C data."""
    device.write(bytes(data))

    if length > 0:
        msg_r = bytearray(length)
        device.readinto(msg_r)
        return list(msg_r)

    return []


def read():
    """Read down, up, left, right and switch data from trackball."""
    left, right, down, up, switch = i2c_rdwr([REG_LEFT], 5)

    switch = 129 == switch

    return left, right, down, up, switch


with device:
    # set_leds(0,0,5,100)
    set_leds_purple()

    multiplier = 9

    while True:
        down, up, left, right, switch = read()

        # Send movements and clicks to xte
        if switch:
            m.click(Mouse.LEFT_BUTTON)
        else:
            x = right - left
            y = down - up
            m.move(int(-x * multiplier), int(-y * multiplier), 0)
