## chip44780: Character LCD driver for CHIP

This is a quick and dirty proof of concept for hooking up an HD44780 Character LCD to the CHIP SBC (@NextThingCo)

![LCD that says "Sweet!"](https://pbs.twimg.com/media/Cm-P0_wUIAAF2jp.jpg)

This was accomplished with a 1x8 3.3v display.

Depends on [CHIP_IO module](https://github.com/xtacocorex/CHIP_IO) by xtacocorex 

### Files:

*  chip44780.py:  Library with pin definitions and screen control functions
*  chip44780daemon.py:  Runs as a python daemon, listening on 127.0.0.1 port 10000 for messages to scroll
*  sendMessages.py:  Command line tool takes keyboard input for messages and sends the to the daemon for display

### Status 
 

*  Working
*  TODO: Modularize this so it can be called by other programs

