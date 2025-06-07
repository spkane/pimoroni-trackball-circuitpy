import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

I2C_ADDRESS = 0x0A

REG_LED_RED = 0x00
REG_LED_GRN = 0x01
REG_LED_BLU = 0x02
REG_LED_WHT = 0x03

REG_LEFT = 0x04
REG_RIGHT = 0x05
REG_UP = 0x06
REG_DOWN = 0x07

# i2c @ address 0xA
i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, I2C_ADDRESS)

# intensity of r,g,b,w LEDs from 0-100 e.g. set_leds(100,100,25,50)
def set_leds(r, g, b, w):
    while not i2c.try_lock():
        pass
    device.write(bytes([REG_LED_RED, r & 0xFF]))
    device.write(bytes([REG_LED_GRN, g & 0xFF]))
    device.write(bytes([REG_LED_BLU, b & 0xFF]))
    device.write(bytes([REG_LED_WHT, w & 0xFF]))
    i2c.unlock()

def set_leds_cyan():
    set_leds(0, 100, 100, 0)


def set_leds_magenta():
    set_leds(100, 0, 100, 0)


def set_leds_yellow():
    set_leds(100, 100, 0, 0)


def set_leds_red():
    set_leds(100, 0, 0, 0)


def set_leds_green():
    set_leds(0, 100, 0, 0)


def set_leds_blue():
    set_leds(0, 0, 100, 0)


def set_leds_white():
    set_leds(0, 0, 0, 100)


def i2c_rdwr(data, length=0):
    """Write and optionally read I2C data."""
    while not i2c.try_lock():
        pass
    device.write(bytes(data))

    if length > 0:
        msg_r = bytearray(length)
        device.readinto(msg_r)
        i2c.unlock()
        return list(msg_r)

    i2c.unlock()
    return []


def read():
    """Read down, up, left, right and switch data from trackball."""
    left, right, down, up, switch = i2c_rdwr([REG_LEFT], 5)

    switch = 129 == switch

    return left, right, down, up, switch

