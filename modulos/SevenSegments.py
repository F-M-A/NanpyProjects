'''
Create on 29/03/2013

Controls a SevenSegment display

@author: Fernando Molina
'''

from random import randint

class SevenSegments():
    #PinOut is a list with the outputs pins (4, A, B, C, D)
    def __init__(self, arduino, pinOut):
        self.pinOut = pinOut
        self.arduino = arduino

    def numberGenerator(self, num):
        for i in range(len(self.pines)):
             self.arduino.digitalWrite(self.pinOut[i], num%2)
             self.arduino.delay(2)
             num = num//2

    def throwDice(self):
        numberGenerator(self, randint(0, 6))
