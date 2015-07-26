import serial

connected = False

ser = serial.Serial("COM3", 9600) #SET PROPER COM PORT

while not connected:
    serin = ser.read()
    connected = True

ser.write("1")

while ser.read() == '1':
    ser.read()
    
ser.close()