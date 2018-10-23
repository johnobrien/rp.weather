#! /usr/bin/env python
# from https://github.com/PiSupply/PaPiRus/blob/master/RTC-Hat-Examples/RTCreboot/rtcreboot

import argparse
from smbusf import SMBus
from datetime import datetime, timedelta
from dateutil import tz
from prtc import readrtc, writealm, enablealm0

import os

parser = argparse.ArgumentParser()
parser.add_argument('alarm',
                    nargs='?',
                    default=0400,
                    type=list,
                    help='time to restart')

args=parser.parse_args()

# i2cbus = SMBus(1)

# time to wait before booting

now = datetime.datetime.now()
print(now)


# delta=timedelta(seconds=args.delay)
#
# dtrtc = readrtc(i2cbus)
# reboot = dtrtc + delta
# writealm(i2cbus, 0, reboot)
#
# # RTC is in UTC, convert to local time
# HERE = tz.tzlocal()
# UTC  = tz.gettz('UTC')
# reboot = reboot.replace(tzinfo=UTC)
# reboot = reboot.astimezone(HERE)
# reboottime = reboot.strftime('%H:%M:%S')
#
# # Enable alrm 0
# enablealm0(i2cbus)
# print("Current time is {0}".format(datetime.now()))
# print("Reboot time set for {0}".format(reboottime))