# The script that on boot checks
# whether a device with the string "Keyboard",
# in the description is attached, and if not,
# update the git repo, executes update_weather.py,
# and shuts down the raspberry pi.

# Will probably need to chmod this to executable and being owned by root

# The path to this script needs to be added to /etc/rc.local

if lsusb |grep 'Keyboard'; then
    echo "Keyboard present"
else
    echo "Keyboard not present"
    git --git-dir=/home/pi/rp.weather/.git pull
    python /home/pi/rp.weather/update_weather.py
    # python /home/pi/rp.weather/set_reboot.py
    # sudo poweroff
fi
