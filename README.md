# android pin cracker
If you have enabled usb debugging and have forgot your passcode, this tool is made for you! It was tested with Sony Xperia T (aliases: lt30p / mint). This script has no success detetion, so I'd recommend using a timlapse camera to film it (x10 speed is perfect)
## Prerequisites
- Python
- adb (added to PATH)
- A phone with USB debugging enabled
- A pin.txt that contains 4 length codes, separated by a new line (the one provided works just fine.)
## Usage
You have to manually define the position of each button. You can to this by manually typing "adb shell input tap x y" in a terminal.  
Example: `adb shell input tap 200 700`.  
The positions are hardcoded, so you'll have to modify the script.
## Troubleshooting
### USB debugging was enabled, but how to accept prompt on the phone?
Open emergency call and then reconnect to PC.  A dialog box should appear.
