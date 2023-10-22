import math

class Dac:
    def __init__(self, voltage):
        self.voltage = voltage

    def DecimalToBinary(self, num):
        return int("{0:b}".format(math.ceil(num)))
        
    def ToDigital(self):
        if self.voltage == 0:
            return 0
        return self.DecimalToBinary(1023 / (5 / self.voltage))

    def binaryToDecimal(self, n):
        return int(str(n), 2)
 
    def SetDigitalValue(self, value):
        return round(5 / (1023 / self.binaryToDecimal(value)), 2)
    
class Dac:
    def __init__(self, voltage, max_voltage, num_of_bits):
        self.voltage = voltage
        self.max_voltage = max_voltage
        self.num_of_bits = num_of_bits
        self.dec_num_of_bits = pow(2, num_of_bits) - 1

    def DecimalToBinary(self, num):
        return int("{0:b}".format(math.ceil(num)))
        
    def ToDigital(self):
        if self.voltage == 0:
            return 0
        return self.DecimalToBinary(self.dec_num_of_bits / (self.max_voltage / self.voltage))

    def binaryToDecimal(self, num):
        return int(str(num), 2)
 
    def SetDigitalValue(self, value):
        return round(self.max_voltage / (self.dec_num_of_bits / self.binaryToDecimal(value)), 2)

d = Dac(2.5)
print()
bin = d.ToDigital()
print(bin)
print(d.SetDigitalValue(bin))