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

d = Dac(2.5)
print()
bin = d.ToDigital()
print(bin)
print(d.SetDigitalValue(bin))
