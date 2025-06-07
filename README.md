# pimoroni-trackball-circuitpy

A simple, but effective CircuitPython-compatible library for using the Pimoroni Trackball module as a mouse. Based on [Pimoroni's official Python library](https://github.com/pimoroni/trackball-python), which is incompatible with CircuitPython.

I don't have a totally clear understanding of how the Pimoroni Trackball works under the hood or why their official library does some of the things that it does. Anyway, I find the Trackball unsuitable for desktop OS use as it loses precision at higher acceleration/sensitivity value (set by the `multiplier` in the code.py file). Maybe someone smarter than me can fix this, but I suspect it's a hardware issue (e.g. the ball is too small to have the precision of a traditional trackball mouse).

## Dependencies

This library code is tested to work with CircuitPython 7-10 and the required library from the [Adafruit CircuitPython bundle](https://circuitpython.org/libraries):

- adafruit_bus_device

The example code makes use of a few addition libraries, including:

- adafruit_hid
