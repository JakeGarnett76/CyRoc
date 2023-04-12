import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class AnimationPlot:
    def animate(self, i, dataList, ser):
        ##Errrrrror
        arduinoData_string = ser.readline().decode('ascii')
        newData = arduinoData_string.split()

        try:
                dataList.append(float(newData[6]))
                print(float(newData[6]))

        except:
                pass

        dataList = dataList[-25:]
        ax.clear()
        self.getPlotFormat()
        ax.plot(dataList)

    def getPlotFormat(self):
        ax.set_ylim([0, 1000])
        ax.set_title("x")
        ax.set_ylabel("y")

window = Tk()

# setting the title 
window.title('cyroc')
  
# dimensions of the main window
window.geometry("800x800")


photo = PhotoImage(file = "istate.png")
window.iconphoto(False, photo)

dataList = []

fig = plt.figure()

ax = fig.add_subplot(111)

realTimePlot = AnimationPlot()

ser = serial.Serial("COM10", 9600)

time.sleep(1)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()

button = Button(master=window, text="Quit", command=window.quit)
button.pack(side=BOTTOM)

toolbar.pack(side=BOTTOM, fill=X)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
   
ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(dataList, ser), interval=100) 

  
# run the gui
window.mainloop()
#window.mainloop()
    
