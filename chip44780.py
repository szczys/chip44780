## chip44780 by Mike Szczys 2016 ##
## MIT License

## Credits:
#  Elm-Chan is an excellent HD44780 info source and has been my
#  go-to for many years now: http://elm-chan.org/docs/lcd/hd44780_e.html
#
#  The CHIP_IO module does all of the SBC hardware handling:
#  https://github.com/xtacocorex/CHIP_IO
#  Well done xtacocorex on that package!

## Connect an HD44780 display in 4-bit mode to the CHIP by @NextThingCo


# Pinout Definitions
RS = "XIO-P0"
RW = "XIO-P1"
E = "XIO-P2"

DB4 = "XIO-P4"
DB5 = "XIO-P5"
DB6 = "XIO-P6"
DB7 = "XIO-P7"

BACKLIGHT = "CSID0"

### More Connection Info:
# Newhaven Display 1x8
# NHD-0108HZ-FSW-GBW
# LCD Pin   Function
# 1         VCC-3V3
# 2         GND
# 3         RS
# 4         RW
# 5         E
# 6         DB4
# 7         DB5
# 8         DB6
# 9         DB7
# 10        BACKLIGHT (LED+)
# 11        LED- (GND)
###

import CHIP_IO.GPIO as GPIO
from time import sleep

def initIO():
    GPIO.setup(RS, GPIO.OUT)
    GPIO.setup(RW, GPIO.OUT)
    GPIO.setup(E, GPIO.OUT)
    GPIO.setup(DB4, GPIO.OUT)
    GPIO.setup(DB5, GPIO.OUT)
    GPIO.setup(DB6, GPIO.OUT)
    GPIO.setup(DB7, GPIO.OUT)
    GPIO.setup(BACKLIGHT, GPIO.OUT)

    GPIO.output(RS, 0)
    GPIO.output(RW, 0)
    GPIO.output(E, 0)

    GPIO.output(DB4, 0)
    GPIO.output(DB5, 0)
    GPIO.output(DB6, 0)
    GPIO.output(DB7, 0)

    GPIO.output(BACKLIGHT, 0)

def sendCMD(binData):
    GPIO.output(RS, 0)  #Low to send command
    GPIO.output(RW, 0)
    print "Do Something Idiot"

def sendDATA(binData):
    GPIO.output(RS, 1)  #High to send data
    GPIO.output(RW, 0)
    print "Do Something Idiot"

def strobe():
    #Strobes the E line to read in data (with a pause for LCD to have a chance)
    GPIO.output(E, 1)
    sleep(0.001)
    GPIO.output(E, 0)

def setBus(binData):
    if (binData & 1<<0) > 0:
        GPIO.output(DB4, 1)
    else:
        GPIO.output(DB4, 0)

    if (binData & 1<<1) > 0:
        GPIO.output(DB5, 1)
    else:
        GPIO.output(DB5, 0)

    if (binData & 1<<2) > 0:
        GPIO.output(DB6, 1)
    else:
        GPIO.output(DB6, 0)

    if (binData & 1<<3) > 0:
        GPIO.output(DB7, 1)
    else:
        GPIO.output(DB7, 0)

def sendCMD(binData):
    GPIO.output(RS, 0)  #Low to send command
    GPIO.output(RW, 0)
    setBus(binData)
    strobe()

def sendDATA(binData):
    GPIO.output(RS, 1)  #High to send data
    GPIO.output(RW, 0)
    setBus(binData)
    strobe()

def cursor(position):
    #This only works for a 1-line display
    sendCMD((0x80+position)>>4)
    sendCMD(0x80+position)

def putString(myString):
    for i in myString:
        binVal = int(ord(i))
        sendDATA(binVal>>4)
        sendDATA(binVal)

def initLCD():
    sleep(0.1) # wait at least 40ms for CLCD powerup
    initIO()
    GPIO.output(BACKLIGHT, 1)
    sendCMD(0b0011) #Wake
    sleep(0.01) # wait at least 4.1ms
    sendCMD(0b0011) #Wake 2
    sleep(0.01)
    sendCMD(0b0011) #Wake 3
    sleep(0.01)
    sendCMD(0b0010) #4-bit interface
    sendCMD(0b0010) #4-bit again?
    sendCMD(0b1000) #1-line display
    sendCMD(0b0001) #set cursor
    sendCMD(0b0000) #rest of set cursor
    sendCMD(0b0000) #display on
    sendCMD(0b1111) #rest of display on
    sendCMD(0b0000) #entry mode set
    sendCMD(0b0110) #rest of entry mode set

initLCD()
#TODO: Clear screen here (need to write function)
cursor(0)
putString("Aw Yeah!")
