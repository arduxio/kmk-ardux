# kmk-ardux
KMK implementation of ardux. A fork of artsey.io
https://github.com/KMKfw/kmk_firmware

## Current Issues
* OneShot keys seem to stick rather than disabling after timeout or a keypress. 
* Mouse Functionality
* Implement shift hold (not caps lock - caps doesn't apply to numbers)
* What else?

## Native CircuitPython KMK vs. KMK Build


## CircuitPython dev in Linux Notes
Use screen to open a serial console on the rp2040 device:  
```
sudo apt install screen
screen /dev/ttyACM0 # or ACM1, etc, depending on what shows up.
```  
  



