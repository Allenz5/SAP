import digitalio
import adafruit_bmp280
import adafruit_dht
import adafruit_ltr390
import busio
import adafruit_blinka.microcontroller.bcm283x.pin as bcm_pin

def get_pressure():
	SCL = bcm_pin.D3
	SDA = bcm_pin.D2

	i2c = busio.I2C(SCL, SDA)

	try:
		bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

		temperature = bmp280.temperature
		pressure = bmp280.pressure
	except RuntimeError as error:
		print(f"Sensor error: {error}")
	finally:
		return pressure
	return None

def get_temperature_and_humidity():
	try:
		dhtDevice = adafruit_dht.DHT11(bcm_pin.D4)
		temperature = dhtDevice.temperature
		humidity = dhtDevice.humidity
	except RuntimeError as error:
		print(f"Sensor error: {error}")
	finally:
		return temperature, humidity
	return None

def get_uv_and_light():
	SCL = bcm_pin.D23
	SDA = bcm_pin.D22
	i2c = busio.I2C(SCL, SDA)

	try:
		ltr = adafruit_ltr390.LTR390(i2c, address=0x53)
		uv = ltr.uvs
		light = ltr.light
		return uv,light
	except RuntimeError as error:
		print(f"Sensor error: {error}")
	return None, None
