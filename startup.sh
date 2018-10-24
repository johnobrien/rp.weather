# The script that on boot checks
# whether a device with the string "Keyboard",
# in the description is attached, and if not,
# update the git repo, executes update_weather.py,
# and shuts down the raspberry pi.

# Will probably need to chmod this to executable and being owned by root
# You can probably use git bash to do this.

# The path to this script needs to be added to /etc/rc.local

if lsusb |grep 'Keyboard'; then
    papirus-write "Keyboard present. startup.sh exiting."
else
    echo "Keyboard not present"
    # git --git-dir=/home/pi/rp.weather/.git pull
    # https://raspberrypi.stackexchange.com/questions/85185/accessing-exported-environment-variables-in-python
    sudo --preserve-env -u pi /usr/bin/python2.7 /home/pi/rp.weather/update_weather.py
    sudo -u pi /usr/bin/python2.7 /home/pi/rp.weather/set_reboot.py
    sudo poweroff
fi
