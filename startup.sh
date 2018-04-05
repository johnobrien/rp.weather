# The script that on boot checks
# whether a USB device is attached, and if not,
# update the git repo, executes update_weather.py,
# and shuts down the raspberry pi.

if not(lsusb -v 2>/dev/null|grep -q 'bInterfaceProtocol.*Keyboard' &&)
    echo "Keyboard not present"
    git --git-dir=/path/to/kd.weather/on/pi pull
    python /path/to/update_wather.py/on/pi
    # Set restart to an hour from now
    # Shutdown raspberry pi
else
    echo "Keyboard present"
