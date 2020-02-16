# Open i2c bus 1 and read one byte from address 80, offset 0
from smbus2 import SMBus
import time

address = 0x68

"""
bit 7: read bit (does not matter for continous)
bit 6-5: Channel: 00 = Channel 1
bit 4: conversion mode: 1 - continous conversion
bit 3-2: Sample rate, 01 = 60SPS (14 bits)
bit 1-0: Gain selection, 00 = 1x
"""
config_bit = '0b00010100'

with SMBus(1) as bus:
    bus.write_byte(address, config_bit)
    for i in range(10):
        bus.read_byte(address)
        time.sleep(1)
        # Returned value is a list of 16 bytes
    print(block)
