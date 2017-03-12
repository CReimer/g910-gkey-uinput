#!/usr/bin/python

import uinput
import pyudev
import glob

context = pyudev.Context()

device = None
for hidraw in glob.glob("/dev/hidraw*"):
    dev = pyudev.Devices.from_device_file(context, hidraw)
    if "046D:C335.0002" in dev.device_path:
        device = hidraw

g1 = uinput.KEY_FN_F1
g2 = uinput.KEY_FN_F2
g3 = uinput.KEY_FN_F3
g4 = uinput.KEY_FN_F4
g5 = uinput.KEY_FN_F5
g6 = uinput.KEY_FN_F6
g7 = uinput.KEY_FN_F7
g8 = uinput.KEY_FN_F8
g9 = uinput.KEY_FN_F9
m1 = uinput.KEY_F13
m2 = uinput.KEY_F14
m3 = uinput.KEY_F15
mr = uinput.KEY_F16

f = open(device, 'rb')
device = uinput.Device((g1, g2, g3, g4, g5, g6, g7, g8, g9, m1, m2, m3, mr))

while True:
    binary = f.read(20)
    prefix = binary[0:3]

    if prefix == b'\x11\xff\x08':
        device.emit(g1, binary[4] & 1 != 0)
        device.emit(g2, binary[4] & 2 != 0)
        device.emit(g3, binary[4] & 4 != 0)
        device.emit(g4, binary[4] & 8 != 0)
        device.emit(g5, binary[4] & 16 != 0)
        device.emit(g6, binary[4] & 32 != 0)
        device.emit(g7, binary[4] & 64 != 0)
        device.emit(g8, binary[4] & 128 != 0)
        device.emit(g9, binary[5] & 1 != 0)
    elif prefix == b'\x11\xff\t':
        device.emit(m3, binary[4] & 1 != 0)
        device.emit(m2, binary[4] & 2 != 0)
        device.emit(m1, binary[4] & 4 != 0)
    elif prefix == b'\x11\xff\n':
        device.emit(mr, binary[4] & 1 != 0)
