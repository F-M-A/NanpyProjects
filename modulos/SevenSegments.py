'''
Created on 24/03/2013

@author: Fernando Molina
'''

class SevenSegments():
	def __init__(self, arduino, pines=(8,9,10,11)):
		self.arduino = arduino
		self.pines = pines
	
	def generarNumero(self, num:"int"):
		for i in range(4):
			arduino.digitalWrite(pines[i], num%2)
			arduino.delay(2)
			num = num//2
