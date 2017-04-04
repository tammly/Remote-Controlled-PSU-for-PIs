#!/usr/bin/python

import time
import RPi.GPIO as GPIO #apt-get install python-dev python-rpi.gpio
import sys

channels = 24

class Start(object):

    def __init__(self, channels):
        self.channels = channels

    def Generator(num):

        if num == 'all':
            bin = [1] * channels
        else:
            bin = [0] * channels
            bin[num-1] = 1

        str1 = ''.join(str(e) for e in bin) # convert array to string
        str1 = str1[::-1] # reverse binary string
        r1,r2 = str1[:-16],str1[8:] # splice binary into 2 groups for each relay

        # Function for formatting the Hex value to something usable
        #def padhexa(s):
        #    return s[2:].zfill(6)
        #    return '0x' + s[2:].zfill(4)
        return (r1,r2)

    def USBRelay(x):
        count = 0
        for i in reversed(x):
            if i == '1':
                h = i + ('0' * count)
                j = hex(int(h,2))
                j = 'Sending USB code %s' %  j
                time.sleep(1)
                print(j)
            else:
                pass
            count += 1
        print('reset relay')
        return 0

    def GPIORelay(var, gid):
        var.setmode(var.BCM)
        var.setwarnings(False)
        led = 4
        # Representing relay 17-24 (8 ch relay)
        relay = "gpio17", "gpio18", "gpio19", "gpio20", "gpio21", "gpio22", "gpio23", "gpio24";
        count = 0
        for i in reversed(gid):
            if i == '1':
                #var.setup(led,var.OUT)
                print("Light on")
                #var.output(led,var.HIGH)
                print(relay[count])
                time.sleep(1)
                print("Light off")
                #var.output(led,var.LOW)
            count += 1
        var.cleanup()
        return 0

    if len(sys.argv) == 2:
        t = sys.argv[1]
        # change to argument to lower case, if possible.
        try:
            t = t.lower()
            t = int(t)
        except:
            pass
    else:
        msg = 'Example: grelay_multi.py [relay#] or [all]'
        sys.exit(msg)

    if t == 'all':
        pass    
    elif 1 <= t <= channels:
        pass
    else:
        sys.exit('Invalid Relay Number! Exiting script...')
    r8,r16 = Generator(t)
    
    USBRelay(r16) # Send code to USB relays
    GPIORelay(GPIO, r8) # Send code to GPIO relay

Start(channels)
