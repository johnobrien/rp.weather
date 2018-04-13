#! /usr/bin/env python
# from https://github.com/PiSupply/PaPiRus/blob/master/RTC-Hat-Examples/RTCreboot/rtcreboot

import argparse
from smbusf import SMBus
from datetime import datetime, timedelta
from dateutil import tz
from prtc import readrtc, writealm, enablealm0
from papirus import Papirus
from pwrite_text import write_text

import os

parser = argparse.ArgumentParser()
parser.add_argument('delay',
                    nargs='?',
                    default=60,
                    type=int,
                    help='delay in seconds till reboot, default 3600')

args=parser.parse_args()

i2cbus = SMBus(1)
papirus = Papirus()
papirus.clear()

# time to wait before booting
delta=timedelta(seconds=args.delay)

dtrtc = readrtc(i2cbus)
reboot = dtrtc + delta
writealm(i2cbus, 0, reboot)

# RTC is in UTC, convert to local time
HERE = tz.tzlocal()
UTC  = tz.gettz('UTC')
reboot = reboot.replace(tzinfo=UTC)
reboot = reboot.astimezone(HERE)
reboottime = reboot.strftime('%H:%M:%S')

# Enable alrm 0
enablealm0(i2cbus)

print("Reboot time set for {0}".format(reboottime))