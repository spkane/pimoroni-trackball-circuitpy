# pimoroni-trackball-circuitpy

A fork of a basic [CircuitPython-compatible library for using the Pimoroni Trackball module as a mouse](https://github.com/jspinella/pimoroni-trackball-circuitpy).

I forked this for a few reasons:

- The original didn't really work well as a library, so I re-worked it a bit so that it could be imported and called like a standard library and I2C functions that needed to request locks were doing so and then releasing them when done.
- Also, in my project the trackball is mounted in such a way, that I needed to modify the directions to get the pointer to do what I expected. It is possible this is my misunderstanding of something simple, a bug in the original code, or even a change in the device or libraries, but `"It works for me."™`

## Upstream README (_with a few minor updates_)

Based on [Pimoroni's official Python library](https://github.com/pimoroni/trackball-python), which is incompatible with CircuitPython.

I (_jspinella_) don't have a totally clear understanding of how the Pimoroni Trackball works under the hood or why their official library does some of the things that it does. Anyway, I find the Trackball unsuitable for desktop OS use as it loses precision at higher acceleration/sensitivity value (set by the `multiplier` in the code.py file). Maybe someone smarter than me can fix this, but I suspect it's a hardware issue (e.g. the ball is too small to have the precision of a traditional trackball mouse).

## Dependencies

This library code is tested to work with CircuitPython 7-10 and the required library from the [Adafruit CircuitPython bundle](https://circuitpython.org/libraries):

- adafruit_bus_device

The example code makes use of a few addition libraries, including:

- adafruit_hid
