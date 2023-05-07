import time
import serial
import serial.tools.list_ports
from tkinter import * 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


class AnimationPlot:
    def animate(self, i, dataList, ser):
        arduinoData_string = ser.readline().decode('ascii')
        newData = arduinoData_string.split()

        try:
                # this will be graphed on the y axis
                dataList.append(float(newData[6]))
                print(float(newData[6]))
                # this will be displayed on the right side of the window as the current altitude
                myString.set("Current Altitude: " + str(newData[6]))

        except:
                pass

        dataList = dataList[-25:]
        ax.clear()
        self.getPlotFormat()
        ax.plot(dataList)

    def getPlotFormat(self):
        # change y axis bounds
        ax.set_ylim([0, 1000])
        #sets x-axis label
        ax.set_title("Time")
        #sets y-axis label
        ax.set_ylabel("Particle Density")


dataList = []
portList = []
ports = serial.tools.list_ports.comports()

# gets and prints portList
for onePort in ports:
	portList.append(str(onePort))
	print(str(onePort))

# takes user input to listen for serial input
iport = input("Select Port: COM")

# creates parent tkinter window
window = Tk()

window.resizable(False,False)

#creates frame to store right side widgets
frame = Frame(window)
frame.pack(side=RIGHT)

# sets the title 
window.title('CyRoc')
  
# sets the dimensions of the main window
window.geometry("1200x800")

# changes background color to light grey
window.configure(bg="#f0f0f0")

# sets iowa state icon
photo = PhotoImage(file = "../image/istate.png")
window.iconphoto(False, photo)

#adds iowa state image
imgC = Canvas(frame, width = 300, height = 300)
imgC.pack(side=TOP)
img = PhotoImage(file="../image/istate.png")      
imgC.create_image(0,0, anchor=NW, image=img)


# creates widget to display altitude
myString = StringVar()
altitude = myString.get()
w = Label(frame, textvariable=myString, font=('Helvetica bold', 15))
w.pack()

# setup to prepare animated graph
fig = plt.figure()
ax = fig.add_subplot(111)
realTimePlot = AnimationPlot()

# sets port for serial input 
ser = serial.Serial("COM" + str(iport), 9600)

time.sleep(1)

# creates canvas for graph
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()

# creates toolbar
toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
toolbar.update()

# creates Quit button
button = Button(master=frame, text="Quit", command=window.quit)
button.pack(side=BOTTOM, pady = 220)

# creates toolbar
toolbar.pack(side=BOTTOM, fill=X)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# handles graph animation
ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(dataList, ser), interval=100) 

# run the gui
window.mainloop()
    
