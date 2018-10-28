#!/usr/bin/env bash
# The script that on boot checks
# whether a device with the string "Keyboard",
# in the description is attached, and if not,
# executes update_weather.py,
# set when to reboot,
# and shuts down the raspberry pi.

# The path to this script needs to be added to weather.service

sudo hwclock -s
date

if lsusb |grep 'Keyboard'; then
    papirus-write "Keyboard present. startup.sh exiting."
else
    echo "Keyboard not present"
    sudo --preserve-env -u pi /usr/bin/python3 /home/pi/rp.weather/update_weather.py
    sudo -u pi /usr/bin/python3 /home/pi/rp.weather/set_reboot.py
    sudo poweroff
fi
