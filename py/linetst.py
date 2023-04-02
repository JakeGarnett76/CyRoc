import serial
import matplotlib.pyplot as plt

plt.ion()
fig=plt.figure()


i=0
x=list()
y=list()
i=0
ser = serial.Serial('COM9',9600)
ser.close()
ser.open()
while True:

    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())

    #plt.scatter(i, float(data.decode()))
    plt.plot(i, x[i], "r")
    i += 1
    plt.show()
    plt.pause(0.0001)
