from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import Wall_E_Communication as comms
import threading
import time

# Design GUI
root = Tk()
root.title("Wall-E Autonomous Rover GUI")
root.iconbitmap("images/UAS-Icon.ico")
root.configure(bg="#36a3ff")

root.minsize(1190, 600)

# Header
headerFrame = LabelFrame(root, padx=10, pady=10, bg="white")
headerFrame.grid(row=0, column=0, padx=20, pady=15, sticky=N, rowspan=2)
uasLogo = ImageTk.PhotoImage(Image.open("images/UASLogo.png"))
headerImage = Label(headerFrame, image=uasLogo, bg="white", padx=10, pady=10).grid(row=0, column=0, padx=10, pady=10)
headerMessage = Label(headerFrame, text="Wall-E Autonomous Rover GUI", font=("Arial", "16", "bold"), bg="white").grid(row=1, column=0, padx=10, pady=10)
WallEImage = ImageTk.PhotoImage(Image.open("images/Wall-E.png").resize((300, 300), Image.ANTIALIAS))
WallELabel = Label(headerFrame, image=WallEImage, bg="white", padx=10, pady=10).grid(row=2, column=0, padx=10, pady=10)

# Rover Status
## Variables
connected = StringVar()
connected.set("Not Connected")
landingStatus = StringVar()
landingStatus.set("On Aircraft")
altitude = DoubleVar()
altitude.set(0)
currentLat = DoubleVar()
currentLat.set(0)
currentLon = DoubleVar()
currentLon.set(0)
targetLat = DoubleVar()
targetLat.set(0)
targetLon = DoubleVar()
targetLon.set(0)
distance = DoubleVar()
distance.set(0)
heading = DoubleVar()
heading.set(0)
speed = DoubleVar()
speed.set(0)
fix = DoubleVar()
fix.set(0)
numSatellites = DoubleVar()
numSatellites.set(0)
PValue = DoubleVar()
PValue.set(0)
IValue = DoubleVar()
IValue.set(0)
DValue = DoubleVar()
DValue.set(0)

def updateVariables():
    global altitude
    while comms.isConnected:
        newValues = comms.data
        newValues.updateValues()
        if newValues.landingStatus == 0:
            landingStatus.set("On Aircraft")
        elif newValues.landingStatus == 1:
            landingStatus.set("Deploying")
        else:
            landingStatus.set("Landed")
        altitude.set(newValues.altitude)
        currentLat.set(newValues.currentLat)
        currentLon.set(newValues.currentLon)
        distance.set(newValues.distance)
        heading.set(newValues.heading)
        speed.set(newValues.speed)
        fix.set(newValues.fix)
        numSatellites.set(newValues.numSatellites)
        PValue.set(newValues.PValue)
        IValue.set(newValues.IValue)
        DValue.set(newValues.DValue)
        time.sleep(comms.updateInterval)

updateThread = threading.Thread(target=updateVariables)

# def reportToConsole():
#     while comms.isConnected:
#         if comms.ser.in_waiting > 0:
#             message = comms.ser.readline()
#             print(comms.decrypt(message))

# updateThread = threading.Thread(target=reportToConsole)

def connectSerial():
    global connectedButton
    global updateThread
    if not comms.isConnected:
        comms.connectToSerial()
        if not comms.isConnected:
            response = messagebox.showerror("ERROR", "Could not connect to serial monitor!")
    if comms.isConnected:
        connectedButton.grid_forget()
        connectedButton = Button(roverStatusFrame, text="Disconnect from Serial", bg="#50e673", font=("Arial", "10"), width=18, command=disconnectSerial)
        connectedButton.grid(row=1, column=0, padx=8, pady=8, sticky=W)
        connected.set("Connected")
        updateThread.start()

def disconnectSerial():
    global connectedButton
    global updateThread
    if comms.isConnected:
        comms.disconnectFromSerial()
    if not comms.isConnected:
        connectedButton.grid_forget()
        connectedButton = Button(roverStatusFrame, text="Connect To Serial", bg="#e85a6d", font=("Arial", "10"), width=18, command=connectSerial)
        connectedButton.grid(row=1, column=0, padx=8, pady=8, sticky=W)
        connected.set("Not Connected")
        updateThread.join()
        updateThread = threading.Thread(target=updateVariables)


## Widget Creation
roverStatusFrame = LabelFrame(root, padx=10, pady=10, bg="white")
roverStatusHeader = Label(roverStatusFrame, text="Wall-E's Status", bg="white", font=("Arial", "16", "bold underline"))

connectedButton = Button(roverStatusFrame, text="Connect To Serial", bg="#e85a6d", font=("Arial", "10"), width=18, command=connectSerial)
connectedVal = Label(roverStatusFrame, textvariable=connected, bg="white", font=("Arial", "10"), padx=5, pady=2, width=12, height=1, anchor=W, relief=SUNKEN)

landingStatusLabel = Label(roverStatusFrame, text="Landing Status", bg="white", font=("Arial", "12"))
landingStatusVal = Label(roverStatusFrame, textvariable=landingStatus, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)

altitudeLabel = Label(roverStatusFrame, text="Altitude", bg="white", font=("Arial", "12"))
altitudeVal = Label(roverStatusFrame, textvariable=altitude, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
altitudeUnits = Label(roverStatusFrame, text="m", bg="white", font=("Arial", "12"))

currentLatLabel = Label(roverStatusFrame, text="Current Latitude", bg="white", font=("Arial", "12"))
currentLatVal = Label(roverStatusFrame, textvariable=currentLat, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
currentLatUnits = Label(roverStatusFrame, text="\N{DEGREE SIGN}", bg="white", font=("Arial", "12"))

currentLonLabel = Label(roverStatusFrame, text="Current Longitude", bg="white", font=("Arial", "12"))
currentLonVal = Label(roverStatusFrame, textvariable=currentLon, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
currentLonUnits = Label(roverStatusFrame, text="\N{DEGREE SIGN}", bg="white", font=("Arial", "12"))

targetLatLabel = Label(roverStatusFrame, text="Target Latitude", bg="white", font=("Arial", "12"))
targetLatVal = Label(roverStatusFrame, textvariable=targetLat, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
targetLatUnits = Label(roverStatusFrame, text="\N{DEGREE SIGN}", bg="white", font=("Arial", "12"))

targetLonLabel = Label(roverStatusFrame, text="Target Longitude", bg="white", font=("Arial", "12"))
targetLonVal = Label(roverStatusFrame, textvariable=targetLon, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
targetLonUnits = Label(roverStatusFrame, text="\N{DEGREE SIGN}", bg="white", font=("Arial", "12"))

distanceLabel = Label(roverStatusFrame, text="Distance", bg="white", font=("Arial", "12"))
distanceVal = Label(roverStatusFrame, textvariable=distance, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
distanceUnits = Label(roverStatusFrame, text="m", bg="white", font=("Arial", "12"))

headingLabel = Label(roverStatusFrame, text="Heading", bg="white", font=("Arial", "12"))
headingVal = Label(roverStatusFrame, textvariable=heading, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
headingUnits = Label(roverStatusFrame, text="\N{DEGREE SIGN}", bg="white", font=("Arial", "12"))

speedLabel = Label(roverStatusFrame, text="Speed", bg="white", font=("Arial", "12"))
speedVal = Label(roverStatusFrame, textvariable=speed, bg="white", font=("Arial", "12"), padx=5, pady=2, width=10, height=1, anchor=W, relief=SUNKEN)
speedUnits = Label(roverStatusFrame, text="m/s", bg="white", font=("Arial", "12"))

fixAndSatLabel = Label(roverStatusFrame, text="Fix / # of Satellites", bg="white", font=("Arial", "12"))
fixVal = Label(roverStatusFrame, textvariable=fix, bg="white", font=("Arial", "12"), padx=5, pady=2, width=2, height=1, relief=SUNKEN)
numSatellitesVal = Label(roverStatusFrame, textvariable=numSatellites, bg="white", font=("Arial", "12"), padx=5, pady=2, width=2, height=1, relief=SUNKEN)

## Widget Placement
roverStatusFrame.grid(row=0, column=2, padx=20, pady=15, sticky=N, rowspan=2)
roverStatusHeader.grid(row=0, column=0, padx=8, pady=8, columnspan=4)

connectedButton.grid(row=1, column=0, padx=8, pady=8, sticky=W)
connectedVal.grid(row=1, column=1, padx=8, pady=8, columnspan=2)

landingStatusLabel.grid(row=2, column=0, padx=8, pady=8, sticky=W)
landingStatusVal.grid(row=2, column=1, padx=8, pady=8, columnspan=2)

altitudeLabel.grid(row=3, column=0, padx=8, pady=8, sticky=W)
altitudeVal.grid(row=3, column=1, padx=8, pady=8, columnspan=2)
altitudeUnits.grid(row=3, column=3, padx=8, pady=8, sticky=W)

currentLatLabel.grid(row=4, column=0, padx=8, pady=8, sticky=W)
currentLatVal.grid(row=4, column=1, padx=8, pady=8, columnspan=2)
currentLatUnits.grid(row=4, column=3, padx=8, pady=8, sticky=W)

currentLonLabel.grid(row=5, column=0, padx=8, pady=8, sticky=W)
currentLonVal.grid(row=5, column=1, padx=8, pady=8, columnspan=2)
currentLonUnits.grid(row=5, column=3, padx=8, pady=8, sticky=W)

targetLatLabel.grid(row=6, column=0, padx=8, pady=8, sticky=W)
targetLatVal.grid(row=6, column=1, padx=8, pady=8, columnspan=2)
targetLatUnits.grid(row=6, column=3, padx=8, pady=8, sticky=W)

targetLonLabel.grid(row=7, column=0, padx=8, pady=8, sticky=W)
targetLonVal.grid(row=7, column=1, padx=8, pady=8, columnspan=2)
targetLonUnits.grid(row=7, column=3, padx=8, pady=8, sticky=W)

distanceLabel.grid(row=8, column=0, padx=8, pady=8, sticky=W)
distanceVal.grid(row=8, column=1, padx=8, pady=8, columnspan=2)
distanceUnits.grid(row=8, column=3, padx=8, pady=8, sticky=W)

headingLabel.grid(row=9, column=0, padx=8, pady=8, sticky=W)
headingVal.grid(row=9, column=1, padx=8, pady=8, columnspan=2)
headingUnits.grid(row=9, column=3, padx=8, pady=8, sticky=W)

speedLabel.grid(row=10, column=0, padx=8, pady=8, sticky=W)
speedVal.grid(row=10, column=1, padx=8, pady=8, columnspan=2)
speedUnits.grid(row=10, column=3, padx=8, pady=8, sticky=W)

fixAndSatLabel.grid(row=11, column=0, padx=8, pady=8, sticky=W)
fixVal.grid(row=11, column=1, padx=2, pady=8)
numSatellitesVal.grid(row=11, column=2, padx=2, pady=8)


# Navigation
## Initialize Variables and Define Methods
isDecimalDegrees = True

def setToDecimalDegrees():
    global isDecimalDegrees
    global setDecimalDegrees
    global setDegMinSec
    isDecimalDegrees = True
    setDecimalDegrees.grid_forget()
    setDegMinSec.grid_forget()
    setDecimalDegrees = Button(navigationFrame, text="Decimal Degrees", bg="#00bfff", font=("Arial", "10", "bold"), width=15, command=setToDecimalDegrees, state=DISABLED)
    setDegMinSec = Button(navigationFrame, text="DegMinSec", bg="white", font=("Arial", "10"), width=15, command=setToDegMinSec)
    setDecimalDegrees.grid(row=2, column=2, padx=8, pady=8, sticky=E)
    setDegMinSec.grid(row=3, column=2, padx=8, pady=8, sticky=E)

def setToDegMinSec():
    global isDecimalDegrees
    global setDecimalDegrees
    global setDegMinSec
    isDecimalDegrees = False
    setDecimalDegrees.grid_forget()
    setDegMinSec.grid_forget()
    setDecimalDegrees = Button(navigationFrame, text="Decimal Degrees", bg="white", font=("Arial", "10"), width=15, command=setToDecimalDegrees)
    setDegMinSec = Button(navigationFrame, text="DegMinSec", bg="#00bfff", font=("Arial", "10", "bold"), width=15, command=setToDegMinSec, state=DISABLED)
    setDecimalDegrees.grid(row=2, column=2, padx=8, pady=8, sticky=E)
    setDegMinSec.grid(row=3, column=2, padx=8, pady=8, sticky=E)

def sendCoords():
    if not comms.isConnected:
        response = messagebox.showerror("ERROR", "Not connected to serial!")
    else:
        try:
            if isDecimalDegrees:
                latToSend = float(latEntry.get())
                lonToSend = float(lonEntry.get())
            else:
                latToSend = convertToDecDegrees(float(latEntry.get()))
                lonToSend = convertToDecDegrees(float(lonEntry.get()))
            if (latToSend > 90 or latToSend < -90 or lonToSend > 180 or lonToSend < -180):
                response = messagebox.showerror("ERROR", "Invalid Latitude/Longitude!")
            else:
                latEntry.delete(0, END)
                lonEntry.delete(0, END)
                comms.data.sendNewValues(latToSend, lonToSend, PValue.get(), IValue.get(), DValue.get())
        except ValueError:
            if (str(latEntry.get()) == "" or str(lonEntry.get()) == ""):
                response = messagebox.showerror("ERROR", "Empty Entry!")
            else:
                response = messagebox.showerror("ERROR", "Cannot enter non-numeric characters!")

def convertToDecDegrees(DegMinSec):
    isNegative = DegMinSec < 0
    absDegMinSec = abs(DegMinSec)
    degrees = int(absDegMinSec)
    minutes = int((absDegMinSec - degrees) * 10)
    seconds = ((absDegMinSec - degrees) * 10 - minutes) * 10
    decDegrees = (degrees + minutes / 60 + seconds / 3600) * (-1 if isNegative else 1)
    return decDegrees

## Widget Creation
navigationFrame = LabelFrame(root, padx=10, pady=10, bg="white")
navigationHeader = Label(navigationFrame, text="Navigation", bg="white", font=("Arial", "16", "bold underline"))
setTargetLabel = Label(navigationFrame, text="Set Target Location", bg="white", font=("Arial", "12", "underline"))

latLabel = Label(navigationFrame, text="Latitude", bg="white", font=("Arial", "12"))
latEntry = Entry(navigationFrame, bg="white", width=10, font=("Arial", "12"))
lonLabel = Label(navigationFrame, text="Longitude", bg="white", font=("Arial", "12"))
lonEntry = Entry(navigationFrame, bg="white", width=10, font=("Arial", "12"))

setDecimalDegrees = Button(navigationFrame, text="Decimal Degrees", bg="#00bfff", font=("Arial", "10", "bold"), width=15, command=setToDecimalDegrees, state=DISABLED)
setDegMinSec = Button(navigationFrame, text="DegMinSec", bg="white", font=("Arial", "10"), width=15, command=setToDegMinSec)
sendCoordsBtn = Button(navigationFrame, text="SEND", bg="white", font=("Arial", "14"), width=10, command=sendCoords)

## Widget Placement
navigationFrame.grid(row=0, column=1, padx=20, pady=15, sticky=N)
navigationHeader.grid(row=0, column=0, padx=8, pady=8, columnspan=3)
setTargetLabel.grid(row=1, column=0, padx=8, pady=1, columnspan=3, sticky=W)

latLabel.grid(row=2, column=0, padx=8, pady=8, sticky=W)
latEntry.grid(row=2, column=1, padx=8, pady=8)
lonLabel.grid(row=3, column=0, padx=8, pady=8, sticky=W)
lonEntry.grid(row=3, column=1, padx=8, pady=8)

setDecimalDegrees.grid(row=2, column=2, padx=8, pady=8, sticky=E)
setDegMinSec.grid(row=3, column=2, padx=8, pady=8, sticky=E)
sendCoordsBtn.grid(row=4, column=2, padx=8, pady=8)


# Set PID
## Initialize Variables and Define Methods
P_IsChanged = BooleanVar()
P_IsChanged.set(True)
I_IsChanged = BooleanVar()
I_IsChanged.set(True)
D_IsChanged = BooleanVar()
D_IsChanged.set(True)

def sendPID():
    if not comms.isConnected:
        response = messagebox.showerror("ERROR", "Not connected to serial!")
    else:
        try:
            if P_IsChanged.get():
                PToSend = float(PEntry.get())
                PEntry.delete(0, END)
            else:
                PToSend = PValue.get()
            if I_IsChanged.get():
                IToSend = float(IEntry.get())
                IEntry.delete(0, END)
            else:
                IToSend = IValue.get()
            if D_IsChanged.get():
                DToSend = float(DEntry.get())
                DEntry.delete(0, END)
            else:
                DToSend = DValue.get()
            comms.data.sendNewValues(targetLat.get(), targetLon.get(), PToSend, IToSend, DToSend)
        except ValueError:
            if ((str(PEntry.get()) == "" and P_IsChanged.get()) or (str(IEntry.get()) == "" and I_IsChanged.get()) or (str(DEntry.get()) == "" and D_IsChanged.get())):
                response = messagebox.showerror("ERROR", "Empty Entry!")
            else:
                response = messagebox.showerror("ERROR", "Cannot enter non-numeric characters!")

## Widget Creation
PIDFrame = LabelFrame(root, padx=10, pady=10, bg="white")
PIDHeader = Label(PIDFrame, text="PID", bg="white", font=("Arial", "16", "bold underline"))
setPIDLabel = Label(PIDFrame, text="Set PID Values", bg="white", font=("Arial", "12", "underline"))
newPIDValsLabel = Label(PIDFrame, text="New PID Value?", bg="white", font=("Arial", "12", "italic"))
yesLabel = Label(PIDFrame, text="Yes", bg="white", font=("Arial", "10"))
noLabel = Label(PIDFrame, text="No", bg="white", font=("Arial", "10"))

PLabel = Label(PIDFrame, text="P", bg="white", font=("Arial", "12"))
PEntry = Entry(PIDFrame, bg="white", width=10, font=("Arial", "12"))
ILabel = Label(PIDFrame, text="I", bg="white", font=("Arial", "12"))
IEntry = Entry(PIDFrame, bg="white", width=10, font=("Arial", "12"))
DLabel = Label(PIDFrame, text="D", bg="white", font=("Arial", "12"))
DEntry = Entry(PIDFrame, bg="white", width=10, font=("Arial", "12"))

PTrueBtn = Radiobutton(PIDFrame, variable=P_IsChanged, value=True, bg="white")
PFalseBtn = Radiobutton(PIDFrame, variable=P_IsChanged, value=False, bg="white")
ITrueBtn = Radiobutton(PIDFrame, variable=I_IsChanged, value=True, bg="white")
IFalseBtn = Radiobutton(PIDFrame, variable=I_IsChanged, value=False, bg="white")
DTrueBtn = Radiobutton(PIDFrame, variable=D_IsChanged, value=True, bg="white")
DFalseBtn = Radiobutton(PIDFrame, variable=D_IsChanged, value=False, bg="white")

sendPIDBtn = Button(PIDFrame, text="SEND", bg="white", font=("Arial", "14"), width=10, command=sendPID)

## Widget Placement
PIDFrame.grid(row=1, column=1, padx=20, pady=15, sticky=N)
PIDHeader.grid(row=0, column=0, padx=8, pady=8, columnspan=4)
setPIDLabel.grid(row=1, column=0, padx=8, pady=1, columnspan=2, rowspan=2, sticky=W)
newPIDValsLabel.grid(row=1, column=2, padx=8, pady=1, columnspan=2)
yesLabel.grid(row=2, column=2, padx=2, pady=1)
noLabel.grid(row=2, column=3, padx=2, pady=1)

PLabel.grid(row=3, column=0, padx=8, pady=8, sticky=W)
PEntry.grid(row=3, column=1, padx=8, pady=8)
ILabel.grid(row=4, column=0, padx=8, pady=8, sticky=W)
IEntry.grid(row=4, column=1, padx=8, pady=8)
DLabel.grid(row=5, column=0, padx=8, pady=8, sticky=W)
DEntry.grid(row=5, column=1, padx=8, pady=8)

PTrueBtn.grid(row=3, column=2, padx=2, pady=8)
PFalseBtn.grid(row=3, column=3, padx=2, pady=8)
ITrueBtn.grid(row=4, column=2, padx=2, pady=8)
IFalseBtn.grid(row=4, column=3, padx=2, pady=8)
DTrueBtn.grid(row=5, column=2, padx=2, pady=8)
DFalseBtn.grid(row=5, column=3, padx=2, pady=8)
sendPIDBtn.grid(row=6, column=2, padx=8, pady=8, columnspan=2)


root.mainloop()