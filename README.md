DHT11 GND (right): 6
DHT11 VCC (mid): 4
DHT11 Data (left): 7

HW611 VCC: 1
HW611 GND: 9
HW611 SCL: 5
HW611 SDA: 3

use sudo i2cdetect -y 1 to check connection

sudo nano /boot/firmware/config.txt
Add
dtparam=i2c_arm=on
dtoverlay=i2c6

LTR390 VCC: 17
LTR390 GND: 14
LTR390 SCL: 16
LTR390 SDA: 15

use sudo i2cdetect -y 6 to check connection
