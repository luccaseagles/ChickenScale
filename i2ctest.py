# Open i2c bus 1 and read one byte from address 80, offset 0
from smbus2 import SMBus

with SMBus(1) as bus:
    # Read a block of 16 bytes from address 80, offset 0
    block = bus.read_i2c_block_data(80, 0, 16)
    # Returned value is a list of 16 bytes
    print(block)
