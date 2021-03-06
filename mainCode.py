#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#    Feb 22, 2021 02:32:02 AM PKT  platform: Windows NT

from tkinter import *
from PIL import ImageTk, Image
import cv2
import time
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from EnviroCode import enviro_data

root = Tk()
root.geometry("1980x1024+0+0")
root.title("Smart Garden System")
# Create a frame
app = Frame(root)#, bg="white", height = 1980, width = 1024)
app.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
app.configure(relief='groove', borderwidth="2", background="#0000ff", highlightbackground="#d9d9d9", highlightcolor="black")

#------global variables
tempData = []
cond = False

#-----plot data-----
def plot_data():
    global cond, tempData
    data = enviro_data()
    if (cond == True):
        if(len(tempData) < 100):
            tempData.append(data["Temperature"]))
        else:
            tempData[0:99] = tempData[1:100]
            tempData[99] = float(data["Temperature"])
                    
        linesHum.set_xdata(np.arange(0,len(tempData)))
        linesHum.set_ydata(tempData)
        
        canvas1.draw()
    root.after(60000,plot_data)

def msgBox():
    data = enviro_data()
    current_time = time.strftime('%I:%M:%S %p %x').lstrip('0').replace(' 0',' ')
    msgbox = str(current_time) + "\tTemperature: " + str(data["Temperature"]) + " °C\t"
    msgbox =  msgbox + "Hum: " + str(data["Humidity"])+" \n%"
    msgbox = msgbox + "Pressure: " + str(data["Pressure"]) + " hPa\t"
    msgbox = msgbox + "Gas: " + str(data["Gas"]) + " kO\t"
    msgbox = msgbox + "Light: " + str(data["Light"]) + " Lux\n"
    messageBox.configure(text = msgbox)
    root.update()
    messageBox.after(60000, msgBox)
    
#------global variables for Humidity
humData = []
cond = False

#-----plot data-----
def plot_data_hum():
    global cond, humData
    data = enviro_data()
    if (cond == True):
        if(len(humData) < 100):
            humData.append(data["Humidity"]))
        else:
            humData[0:99] = humData[1:100]
            humData[99] = float(data["Humidity"])
                    
        linesHum.set_xdata(np.arange(0,len(humData)))
        linesHum.set_ydata(humData)
        
        canvas1.draw()
    root.after(60000,plot_data_hum)

def plot_start():
    global cond
    cond = True
    s.reset_input_buffer()

def plot_stop():
    global cond
    cond = False

def close():
    global root
    #s.close()
    root.destroy()
    root = None

titleLabelM = Label( app)
titleLabelM.place(relx=0.01, rely=0.0, height=66, width=1882)
titleLabelM.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
titleLabelM.configure(font="-family {Segoe UI} -size 24 -weight bold", foreground="#000000", highlightbackground="#d9d9d9")
titleLabelM.configure(highlightcolor="black", text='''Smart Garden System''')
def tick():
    #This function is used to display current time
    current_time = time.strftime('%I:%M:%S %p %x').lstrip('0').replace(' 0',' ')
    datetime.config(text=current_time)
    datetime.after(200,tick)
datetime = Label( app)
datetime.place(relx=0.031, rely=0.128, height=104, width=702)
datetime.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 32 -weight bold")
datetime.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Date & Time''')
tick()

sensorFrame = Frame( app)
sensorFrame.place(relx=0.036, rely=0.285, relheight=0.692, relwidth=0.363)
sensorFrame.configure(relief='groove', borderwidth="2", background="#ff8000", highlightbackground="#d9d9d9", highlightcolor="black")


# Create a label in the frame
lmain = Label(app)
lmain.place(relx=0.542, rely=0.128, height=502, width=827)
lmain.configure(relief='groove', borderwidth="0", background="#0000ff", highlightbackground="#d9d9d9", highlightcolor="black")

#lmain.grid()

# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

graphbutton = Button( app)
graphbutton.place(relx=0.59, rely=0.698, height=154, width=645)
graphbutton.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 32 -weight bold")
graphbutton.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Graph Plotting''', command = lambda: graphFrame.tkraise())

closeButton = Button( app)
closeButton.place(relx=0.928, rely=0.9)
closeButton.configure(font="-family {Segoe UI} -size 18 -weight bold", text='''Close''', command = close)

Message2 = Message( sensorFrame)
Message2.place(relx=0.014, rely=0.014, relheight=0.13, relwidth=0.976)
Message2.configure(background="#ff8000", font="-family {Segoe UI Historic} -size 24 -weight bold")
Message2.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", justify='center', text='''Enviro+\nCurrent Readings''', width=680)

def showSensorData():
    data = enviro_data()
    msg = "Temp: " + str(data["Temperature"]) + " °C"
    templabel.configure(msg)
    humData = "Hum: " + str(data["Humidity"])+" %"
    humlabel.configure(text = humData)
    msg = "Pressure: " + str(data["Pressure"]) + " hPa"
    pressurelabel.configure(text = msg)
    msg = "Gas: " + str(data["Gas"]) + " kO"
    gaslabel.configure( text = msg)
    msg = "Light: " + str(data["Light"]) + " Lux"
    lightlabel.configure(text = msg)
    lightlabel.after(1000, showSensorData)
    root.update()

templabel = Label( sensorFrame)
templabel.place(relx=0.057, rely=0.17, height=81, width=614)
templabel.configure(activebackground="#f9f9f9", activeforeground="black", background="#0080c0", disabledforeground="#a3a3a3")
templabel.configure(font="-family {Segoe UI} -size 20 -weight bold", foreground="#000000", highlightbackground="#d9d9d9")
templabel.configure(highlightcolor="black", text='''Label''')

humlabel = Label( sensorFrame)
humlabel.place(relx=0.057, rely=0.341, height=81, width=614)
humlabel.configure(activebackground="#f9f9f9", activeforeground="black", background="#0080c0", disabledforeground="#a3a3a3")
humlabel.configure(font="-family {Segoe UI} -size 20 -weight bold", foreground="#000000", highlightbackground="#d9d9d9")
humlabel.configure(highlightcolor="black", text='''Label''')

pressurelabel = Label( sensorFrame)
pressurelabel.place(relx=0.057, rely=0.511, height=81, width=614)
pressurelabel.configure(activebackground="#f9f9f9", activeforeground="black")
pressurelabel.configure(background="#0080c0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 20 -weight bold")
pressurelabel.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Label''')

gaslabel = Label( sensorFrame)
gaslabel.place(relx=0.057, rely=0.682, height=81, width=614)
gaslabel.configure(activebackground="#f9f9f9", activeforeground="black", background="#0080c0", disabledforeground="#a3a3a3")
gaslabel.configure(font="-family {Segoe UI} -size 20 -weight bold", foreground="#000000", highlightbackground="#d9d9d9")
gaslabel.configure(highlightcolor="black", text='''Label''')

lightlabel = Label( sensorFrame)
lightlabel.place(relx=0.057, rely=0.852, height=81, width=614)
lightlabel.configure(activebackground="#f9f9f9", activeforeground="black", background="#0080c0", disabledforeground="#a3a3a3")
lightlabel.configure(font="-family {Segoe UI} -size 20 -weight bold", foreground="#000000", highlightbackground="#d9d9d9")
lightlabel.configure(highlightcolor="black", text='''Label''')

############# Plot Frame #############

graphFrame = Frame(root)
graphFrame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
graphFrame.configure(relief='groove', borderwidth="2", background="#0000ff", highlightbackground="#d9d9d9", highlightcolor="black")

fig = Figure();
ax = fig.add_subplot(111)

#ax = plt.axes(xlim=(0,100),ylim=(0, 120)); #displaying only 100 samples
ax.set_title('Temperature Plot');
ax.set_xlabel('Sample')
ax.set_ylabel('Temperature')
ax.set_xlim(0,100)
ax.set_ylim(-0.5,60)
lines = ax.plot([],[])[0]

canvas = FigureCanvasTkAgg(fig, master=graphFrame)  # A tk.DrawingArea.
canvas.get_tk_widget().place(relx=0.313, rely=0.079, relheight=0.327, relwidth=0.679)
#canvas.get_tk_widget().place(x = 10,y=10, width = 500,height = 400)
canvas.draw()


figHum = Figure();
axHum = figHum.add_subplot(111)

axHum.set_title('Humidity Plot');
axHum.set_xlabel('Sample')
axHum.set_ylabel('Humidity %')
axHum.set_xlim(0,100)
axHum.set_ylim(-0.5,100)
linesHum = axHum.plot([],[])[0]

canvas1 = FigureCanvasTkAgg(figHum, master=graphFrame)  # A tk.DrawingArea.
canvas1.get_tk_widget().place(relx=0.313, rely=0.452, relheight=0.327, relwidth=0.679)
canvas1.draw()

homeButton = Button(graphFrame)
homeButton.place(relx = 0.941, rely = 0.784)
homeButton.configure(font="-family {Segoe UI} -size 18 -weight bold", text = "Home", relief = 'groove', border = '2', command = lambda: app.tkraise())

startButton = Button( graphFrame)
startButton.place(relx=0.05, rely=0.2)
startButton.configure(font="-family {Segoe UI} -size 18 -weight bold", text='''Start Plotting''', command = lambda: plot_start())

stopButton = Button( graphFrame)
stopButton.place(relx=0.05, rely=0.6)
stopButton.configure(font="-family {Segoe UI} -size 18 -weight bold", text='''Stop Plotting''', command = lambda: plot_stop())


messageBox = Message( graphFrame)
messageBox.place(relx=0.01, rely=0.846, relheight=0.138, relwidth=0.979)
messageBox.configure(background="#ffffff", font="-family {Segoe UI} -size 16 -weight bold", foreground="#000000", highlightbackground="#d9d9d9")
messageBox.configure(highlightcolor="black", text='''Message\nMessage''', width=1880)

logsLabel = Label( graphFrame)
logsLabel.place(relx=0.01, rely=0.787, height=65, width=171)
logsLabel.configure(activebackground="#f9f9f9", activeforeground="black", background="#ffffff", disabledforeground="#a3a3a3",
                    font="-family {Segoe UI} -size 16 -weight bold", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Logs:''')

titleLabel = Label( graphFrame)
titleLabel.place(relx=0.01, rely=0.01, height=56, width=1882)
titleLabel.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3",
                     font="-family {Segoe UI} -size 24 -weight bold", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Smart Garden System''')
#----start serial port----
s = sr.Serial('COM5',9600);
s.reset_input_buffer()

root.after(1,plot_data)
video_stream()
app.tkraise()
root.mainloop()


