import serial
import time

isConnected = False
newDataReceived = False
startMarker = "<"
endMarker = ">"
updateInterval = 0.5

def connectToSerial():
    global isConnected
    global ser
    try:
        ser = serial.Serial('COM3', 9600)
        isConnected = True
    except:
        isConnected = False

def disconnectFromSerial():
    global isConnected
    global ser
    isConnected = False
    ser.close()

def decrypt(string):
    return string.decode().rstrip()

class dataTransfer:
    def __init__(self):
        self.landingStatus = 0
        self.altitude = 0
        self.currentLat = 0
        self.currentLon = 0
        self.targetLat = 0
        self.targetLon = 0
        self.distance = 0
        self.heading = 0
        self.speed = 0
        self.fix = 0
        self.numSatellites = 0
        self.PValue = 0
        self.IValue = 0
        self.DValue = 0

    def updateValues(self):
        global newDataReceived
        newDataReceived = False
        while isConnected and not newDataReceived:
            while ser.in_waiting > 0:
                try:
                    recString = ser.readline()
                    decryptedStr = decrypt(recString)
                    values = decryptedStr.split(",")
                    if len(values) == 12:
                        newDataReceived = True
                    print(values)
                except:
                    print("Error")

            if newDataReceived:
                try:
                    self.landingStatus = int(values[0])
                    self.altitude = float(values[1])
                    self.currentLat = float(values[2])
                    self.currentLon = float(values[3])
                    self.distance = float(values[4])
                    self.heading = float(values[5])
                    self.speed = float(values[6])
                    self.fix = int(values[7])
                    self.numSatellites = int(values[8])
                    self.PValue = float(values[9])
                    self.IValue = float(values[10])
                    self.DValue = float(values[11])
                    print("Updated")
                except ValueError:
                    newDataReceived = False


    def sendNewValues(self, _targetLat, _targetLon, _PValue, _IValue, _DValue):
        self.targetLat = _targetLat
        self.targetLon = _targetLon
        self.PValue = _PValue
        self.IValue = _IValue
        self.DValue = _DValue

        newValues = startMarker + str(self.targetLat) + "," + str(self.targetLon) + "," + str(self.PValue) + "," + str(self.IValue) + "," + str(self.DValue) + endMarker

        ser.write(newValues.encode())

data = dataTransfer()

connectToSerial()

