#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import sys

# Function creates a binary value for each relay
def binarymaker(n, m):
    if m == 'all':
        listofbinary = [1] * n
    else:
        listofbinary = [0] * n
        listofbinary[t-1] = 1        
    return listofbinary

# Function for formatting the Hex value to something usable
#def padhexa(s):
#    return s[2:].zfill(6)
#    return '0x' + s[2:].zfill(4)

# Function for parsing through binary and send to each relay with USB
def usbrelay(x):
    count = 0
    for i in reversed(x):
        if i == '1':
    	    h = i + ('0' * count)
	    j = hex(int(h,2))
            j = 'Sending USB code ' +  j #placeholder for actual codes
            time.sleep(1)            
            print(j)
        else:
            pass
        count += 1
    print('reset relay') #placeholder for actual codes
    return 0

# Function that Parses through binary and processes each gpio relay
def sendgpio(var, gid):
    var.setmode(var.BCM)
    var.setwarnings(False)
    # Representing relay 17-24 (8 ch relay)
    relay = "gpio17", "gpio18", "gpio19", "gpio20", "gpio21", "gpio22", "gpio23", "gpio24"; #placeholder for actual codes
    count = 0
    for i in reversed(gid):
        if i == '1':            
#             var.setup(led,var.OUT)
            print("Relay on")
#             var.output(led,var.HIGH)
            print(relay[count])
            time.sleep(1)
            print("Relay off")
#             var.output(led,var.LOW)
        count += 1
    var.cleanup()
    return 0

########### Start of main  ############

# set number of relays
channels = 24

# Check for 1 argument
if len(sys.argv) == 2:
    t = sys.argv[1]
    # change to argument to lower case, if possible.
    try:
        t = t.lower()
        t = int(t)
    except:
        pass
else:
    msg = 'Example: 24chRelay.py [relay#] or [all]'
    sys.exit(msg)

if t == 'all':
    pass    
elif 1 <= t <= channels:
    pass
else:
    sys.exit('Invalid Relay Number! Exiting script...')

# Create binary string
barr = binarymaker(channels, t)
str1 = ''.join(str(e) for e in barr) # convert array to string
str1 = str1[::-1] # reverse binary string
r8,r16 = str1[:-16],str1[8:] # splice binary into 2 groups for each relay
#hstr = padhexa(hex(int((str1[::-1]),2))) # convert binary to hex with 6 digits

# Send code to USB relays
usbrelay(r16)

# Send code to GPIO relay
sendgpio(GPIO, r8)

# End of script
