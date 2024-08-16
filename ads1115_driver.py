CHANNELS = [
    0x0000, 0x1000, 0x2000, 0x3000
]

class ADS1115:
    def __init__(self, i2c, address=0x48, gain=1):
        self.i2c = i2c
        self.address = address
        self.gain = gain
        self.holding_register = bytearray(2)

    def write_register(self, reg, value):
        self.holding_register[0] = value >> 8
        self.holding_register[1] = value & 0xFF
        self.i2c.writeto_mem(self.address, reg, self.holding_register)

    def read_register(self, reg):
        self.i2c.readfrom_mem_into(self.address, reg, self.holding_register)
        return self.holding_register[0] << 8 | self.holding_register[1]
    
    def read(self, channel=0):
        config = 0x0000
        config |= CHANNELS[channel]
        self.write_register(0x01, config)
        while not self.read_register(0x01) & 0x8000:
            break
        res = self.read_register(0x00)
        if res < 32768:
            return res
        else:
            return res - 65536
        
    def read_voltage(self, channel=0):
        return self.read(channel) * self.gain