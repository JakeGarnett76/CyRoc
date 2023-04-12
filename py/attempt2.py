import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimationPlot:
	

    def animate(self, i, dataList, ser):
        ser.write(b'g')
        arduinoData_string = ser.readline().decode('ascii')
        newData = arduinoData_string.split()
        #print(i)

        try:
             
 #            dataList1 = float(newData[0])
  #           dataList2 = float(newData[1])
   #          dataList3 = float(newData[2])
    #         dataList4 = float(newData[3])
     #        dataList5 = newData[4]
      #       dataList6 = newData[5]
             dataList.append(float(newData[6]))
             print(float(newData[6]))
       #      print(typeof(float(newData[6])))
        #     dataList8 = newData[7]
         #    dataList9 = newData[8]
         #    dataList10 = newData[9]
          #   dataList11 = newData[10]
           #  dataList12 = newData[11]

        except:
            pass

        dataList = dataList[-50:]
  #      dataList2 = dataList2[-50:]
   #     dataList3 = dataList3[-50:]
    #    dataList4 = dataList4[-50:]
     #   dataList5 = dataList5[-50:]
      #  dataList6 = dataList6[-50:]
       # dataList7 = dataList7[-50:]
        #dataList8 = dataList8[-50:]
        #dataList9 = dataList9[-50:]
        #dataList10 = dataList10[-50:]
        #dataList11 = dataList11[-50:]
        #dataList12 = dataList12[-50:]
        
        ax.clear()
        
        self.getPlotFormat()
        ax.plot(dataList)
        

    def getPlotFormat(self):
        ax.set_ylim([0, 500])
        ax.set_title("Distance")
        ax.set_ylabel("Time")

dataList = []


print("Hello")

fig = plt.figure()

print("Hello1")
ax = fig.add_subplot(111)

print("Hello2")

realTimePlot = AnimationPlot()

print("Hello3")

ser = serial.Serial("COM10", 9600)

print("Hello4")
time.sleep(2)

print("Hello5")
ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(dataList, ser), interval=100) 

print("Hello5")
plt.show()
ser.close()
