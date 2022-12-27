class Solution(object):
    def convertTemperature(self, celsius):
        return celsius + 273.15, (celsius * 1.8)+ 32.00
