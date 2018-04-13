# The script that on boot checks
# whether a device with the string "Keyboard",
# in the description is attached, and if not,
# update the git repo, executes update_weather.py,
# and shuts down the raspberry pi.

# Will probably need to chmod this to executable and being owned by root

# The path to this script needs to be added to /etc/rc.local

if lsusb |grep 'Keyboard'; then
    echo "Keyboard present"
    # git --git-dir=/path/to/kd.weather/dir/on/pi pull
    # python /path/to/update_weather.py/on/pi
    # python /path/to/set_reboot.py/on/pi
    # sudo poweroff
else
    echo "Keyboard not present"
fi
