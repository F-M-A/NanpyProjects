'''
Created on 29/03/2013

@author:Fernando Molina
'''

from nanpy import Arduino
from SevenSegments import SevenSegments

def startArduino(outs):
    for i in range(len(outs)):
        Arduino.pinMode(outs[i], Arduino.OUTPUT)
        Arduino.digitalWrite(outs[i], 0)

def main():
    pines=(8, 9, 10, 11)
    siete = SevenSegments(arduino=Arduino, pines=pines)
    startArduino(pines)
    while True:
        numero = int(input("Numero a mostrar: "))
        if numero == -1: break
        siete.numberGenerator(numero)
    print("Adios")

if __name__=="__main__":
    main()
