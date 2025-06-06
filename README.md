# pimoroni-trackball-circuitpy

A fork of a basic [CircuitPython-compatible library for using the Pimoroni Trackball module as a mouse](https://github.com/jspinella/pimoroni-trackball-circuitpy). 

I forked this, becuase in my project the trackball is mounted in such a way, that I needed to modify the directions to get the pointer to do what I expected. It is possible this is a bug in the original code, or even a change in the device or libraries, but `"It works for me."`

## Upstream README

Based on [Pimoroni's official Python library](https://github.com/pimoroni/trackball-python), which is incompatible with CircuitPython.

I (_jspinella_) don't have a totally clear understanding of how the Pimoroni Trackball works under the hood or why their official library does some of the things that it does. Anyway, I find the Trackball unsuitable for desktop OS use as it loses precision at higher acceleration/sensitivity value (set by the `multiplier` in the code.py file). Maybe someone smarter than me can fix this, but I suspect it's a hardware issue (e.g. the ball is too small to have the precision of a traditional trackball mouse).

## Dependencies
This code is tested to work with CircuitPython 7-10 and two of the libraries from the [Adafruit CircuitPython bundle](https://circuitpython.org/libraries):

- adafruit_bus_device
- adafruit_hid

