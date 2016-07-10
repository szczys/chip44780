#!/usr/bin/python
import socket
import errno
from socket import error as socket_error
import sys
import subprocess
from time import sleep

daemonScript = '/root/compile/chip44780/chip44780daemon.py'

## How to catch Connection Refused socket error:
# http://stackoverflow.com/a/14425454

HOST = '127.0.0.1'
PORT = 10000

s = socket.socket()
try:
    s.connect((HOST, PORT))
except socket_error as serr:
    if serr.errno != errno.ECONNREFUSED:
        raise err
    print "This was a refused connection, launch the daemon and try again"
    subprocess.call(["python", daemonScript])

    #try connecting a few times (give daemon time to start running)
    i = 0
    while i<100:
        try:
            s.connect((HOST, PORT))
            i = 100
            pass
        except:
            sleep(.1)
            i += 1
    
while 1:
    msg = raw_input("Command To Send: ")
    if msg == "close":
	s.close()
	sys.exit(0)
    s.send(msg)
