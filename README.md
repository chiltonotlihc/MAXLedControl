MAXLedControl
=============

A python library for controlling the MAX7221 and MAX7219 LED drivers with the RaspberryPi. 
A port of the Arduino LedControl library.

This library is in its very early stages and is not ready for general use. It requires the use of the RPi.GPIO
python library which requires root permissions.
The plan is to incorporate the wonderful WiringPi library.

Hope it is of use to someone.

Chilton


USE
===========

Initialise with the following format:
  newArray = LedControl.LedControl(DATA_PIN, CLK_PIN, LOAD_PIN)
  Pin numbers refer to the GPIO.BOARD numbers.

---------------------------------------------------------------
Data can be sent with the method:
  .spiTransfer(OP_ADDR, DATA) method.

---------------------------------------------------------------
Leds can be set individually with the method:
  .setLed(ROW, COLUMN, STATE)
  Where STATE is either '0' for off or '1' for on.
  
---------------------------------------------------------------
The display can be cleared with the method:
  .clearDisplay()
  
---------------------------------------------------------------
Intensity can be set with the following method:
  .setIntensity(INTENSITY)
  where INTENSITY is between 0 and 8.

---------------------------------------------------------------
Scan limit (the number of rows that are controllable) can be set with the following method:
  .setScanLimit(LIMIT)
  where LIMIT is between 0 and 8.

---------------------------------------------------------------
The chip can be sent into shutdown mode with the following method:
  .shutdown(STATE)
  Where state is either '0' for off or '1' for on.

---------------------------------------------------------------
For GPIO cleanup, put the following method at the end of your program or in the exceptions case:
  .end()
  
  
More methods coming soon.....
