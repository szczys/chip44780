## chip44780: Character LCD driver for CHIP

This is a quick and dirty proof of concept for hooking up an HD44780 Character LCD to the CHIP SBC (@NextThingCo)

![LCD that says "Sweet!"](https://pbs.twimg.com/media/Cm-P0_wUIAAF2jp.jpg)

This was accomplished with a 1x8 3.3v display.

Depends on [CHIP_IO module](https://github.com/xtacocorex/CHIP_IO) by xtacocorex 

### Status 
 

*  Working
*  TODO: Add Clearscreen function 
*  TODO: Add support for scrolling longer messages
*  TODO: Modularize this so it can be called by other programs

