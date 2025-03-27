# Raspberry Pi Sensor Setup Guide

## Open Extra i2c port

Edit configuration:
```bash
sudo nano /boot/firmware/config.txt
```

Add the following lines:
```
dtparam=i2c_arm=on
dtoverlay=i2c6
```

Reboot to apply changes:
```bash
sudo reboot
```

---

## Hardware Connection

### DHT11 (Temperature and Humidity Sensor)
- **GND (right)** → GPIO Pin **6**
- **VCC (middle)** → GPIO Pin **4**
- **Data (left)** → GPIO Pin **7**

### HW611 (CO₂ Sensor)
- **VCC** → GPIO Pin **1**
- **GND** → GPIO Pin **9**
- **SCL** → GPIO Pin **5**
- **SDA** → GPIO Pin **3**

After wiring, check the connection:
```bash
sudo i2cdetect -y 1
```

---

### LTR390 (UV and Ambient Light Sensor)
- **VCC** → GPIO Pin **17**
- **GND** → GPIO Pin **14**
- **SCL** → GPIO Pin **16**
- **SDA** → GPIO Pin **15**

After wiring, check the connection:
```bash
sudo i2cdetect -y 6
```

---

## Python Environment Setup

Install required library:
```bash
sudo apt install libgpiod2
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirement.txt
```

> ⚠️ Do **not** use `sudo` inside the virtual environment.

---

## Running the Script

1. Use the following commands to find sensor addresses:
    ```bash
    sudo i2cdetect -y 1
    sudo i2cdetect -y 6
    ```

2. Edit the script and update:
    - **Line 15**: with the address from `i2cdetect -y 1`
    - **Line 42**: with the address from `i2cdetect -y 6`
