import RPi.GPIO as GPIO

OP_NOOP = 0
OP_DIGIT0 = 1
OP_DIGIT1 = 2
OP_DIGIT2 = 3
OP_DIGIT3 = 4
OP_DIGIT4 = 5
OP_DIGIT5 = 6
OP_DIGIT6 = 7
OP_DIGIT7 = 8
OP_DECODEMODE = 9
OP_INTENSITY = 10
OP_SCANLIMIT = 11
OP_SHUTDOWN = 12
OP_DISPLAYTEST = 15



#define the LedCOntrol class
class LedControl:
  
	
	def spiTransfer(self, opAddr, data):
		firstBits = bin(opAddr)[2:].zfill(8)
		dataBits = bin(data)[2:].zfill(8)

		
		dataToSend = firstBits+dataBits
		#print dataToSend
		
		GPIO.output(self.SPI_LOAD, GPIO.LOW)
		dataToSend = dataToSend[2:]
		for i in dataToSend:
			GPIO.output(self.SPI_CLK, GPIO.LOW)
			
			if(i=='1'):
				GPIO.output(self.SPI_DATA, GPIO.HIGH)
			else:
				GPIO.output(self.SPI_DATA, GPIO.LOW)
					
			GPIO.output(self.SPI_CLK, GPIO.HIGH)
			
		GPIO.output(self.SPI_LOAD, GPIO.HIGH)
		
	#shutdown	
	def shutdown(self, b):
		if(b):
			self.spiTransfer(OP_SHUTDOWN, 0)
		else:
			self.spiTransfer(OP_SHUTDOWN, 1)
			
	
	#setScanLimit
	def setScanLimit(self, limit):
		if(limit>= 0) and (limit<8):
			self.spiTransfer(OP_SCANLIMIT, limit)
			
	
	#initialiser
	def __init__(self, dataPin, clkPin, csPin):
		self.SPI_DATA = dataPin
		self.SPI_CLK = clkPin
		self.SPI_LOAD = csPin

		self.rows = [0]*8
		print "initialising"

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.SPI_DATA, GPIO.OUT)
		GPIO.setup(self.SPI_CLK, GPIO.OUT)
		GPIO.setup(self.SPI_LOAD, GPIO.OUT)
		GPIO.output(self.SPI_LOAD, GPIO.HIGH)
			

		self.spiTransfer(OP_DISPLAYTEST, 0)
		self.setScanLimit(7)
		self.spiTransfer(OP_DECODEMODE, 0)
		self.shutdown(False)
		
	#set led
	def setLed(self, row, col, val):
		if(row<0) or (row>7) or (col<0) or (col>7):
			return
		
		led = 1
		led = led<<col
		
		
		
		if(val == 1):
			self.rows[row] = self.rows[row] | led
		else:
			led = ~led
			self.rows[row] = self.rows[row] & led
			

		#print bin(self.rows[row])[2:].zfill(8)
		#print self.rows[row]
		self.spiTransfer(row+1, self.rows[row])
		
			
		
		
	#setIntensity
	def setIntensity(self, intensity):
		if(intensity>=0) and (intensity<16):
			self.spiTransfer(OP_INTENSITY, intensity)
	
	
	#clear display
	def clearDisplay(self):
		for i in range(8):
			self.rows[i] = 0
			self.spiTransfer(i+1, self.rows[i])
			
			
		
	def end(self):
		self.shutdown(True)
		self.spiTransfer(OP_DISPLAYTEST, 0)
		GPIO.cleanup();		
	
		
		
