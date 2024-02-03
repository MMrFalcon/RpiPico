import machine
import utime

sensorSignal = machine.ADC(26)
# Max value means 100 % dry, min value is 0
sensorMaxValue = 65535
# sleepInSec = 2
# One hour
sleepInSec = 3600 

def readSoilMoisture():
    sensorValue = sensorSignal.read_u16()
    sensorValueInPercent = 100 - ((sensorValue/sensorMaxValue) * 100)
    valueForPrint = "Soil moisture: %f %%, value: %f" % (sensorValueInPercent, sensorValue)
    print(valueForPrint)
    utime.sleep(sleepInSec)

while True:
    readSoilMoisture()

# TODO add temp/hum sensor support
# TODO display data on the screen
# TODO Save as main.py on pico with bootsel button