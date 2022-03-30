import tkinter as tk
import turtle as tr
import time as tm

#Creates the base circle
def base():
    tr.speed(0)
    tr.width(10)
    tr.up()
    tr.setpos(0,-200)
    tr.down()
    tr.circle(200)
    tr.hideturtle()

#Creates the hour hand
def hourhand():
    hour.speed(0)
    hour.width(7)
    hour.hideturtle()
    hour.left(90)
    hour.right(hourlocation)
    hour.forward(120)

#Creates the minute hand
def minutehand():
    minute.speed(0)
    minute.width(5)
    minute.hideturtle()
    minute.left(90)
    minute.right(minlocation)
    minute.forward(150)

#Creates the second hand
def secondhand():
    second.speed(0)
    second.width(4)
    second.hideturtle()
    second.left(90)
    second.right(seclocation)
    second.forward(180)

def updatehour():
    hour.undo()
    hour.right(30)
    hour.forward(120)

#Updates the minute hand
def updatemin():
    minute.undo()
    minute.right(6)
    minute.forward(150)

#Updates the second hand
def updatesec():
    second.undo()
    second.right(6)
    second.forward(180)

def updatesetback():
    hour.undo()
    hour.setheading(90)
    hour.right(setbacklocation + hourlocation)
    hour.forward(120)

root = tk.Tk()
global setback
setback = 0

def easterntime():
    global setback
    setback = 0

def centraltime():
    global setback
    setback = 11

def mountaintime():
    global setback
    setback = 10

def pacifictime():
    global setback
    setback = 9
    
label = tk.Label(root, text="Clock")
et = tk.Button(root, text="Eastern Time", padx=10, pady=15, command=easterntime).grid(row=0, column=0)
ct = tk.Button(root, text="Central Time", padx=10, pady=15, command=centraltime).grid(row=0, column=1)
mt = tk.Button(root, text="Mountain Time", padx=10, pady=15, command=mountaintime).grid(row=0, column=2)
pt = tk.Button(root, text="Pacific Time", padx=10, pady=15, command=pacifictime).grid(row=0, column=3)


hour = tr.Turtle()
minute = tr.Turtle()
second = tr.Turtle()

curenthour = int(tm.localtime()[3])
if curenthour > 12:
    curenthour = curenthour - 12
curentmin = int(tm.localtime()[4])
curentsec = int(tm.localtime()[5])

base()
created = 0  
setbackcheck = 0
def my_mainloop():
    #make those global variables
    global created
    global hourhand
    global hour
    global minutehand
    global minute
    global secondhand
    global second
    global updatehour
    global updatemin
    global updatesec
    global setback
    global easterntime
    global centraltime
    global mountaintime
    global pacifictime
    global hours
    global minutes
    global seconds
    global hourlocation
    global minlocation
    global seclocation
    global curenthour
    global curentmin
    global curentsec
    global setbackcheck
    global setbacklocation
    

    #gets hours
    hours = int(tm.localtime()[3])
    rawhours = hours
    if hours > 12:
        hours = hours - 12
    #get minutes
    minutes = int(tm.localtime()[4])
    #gets seconds
    seconds = int(tm.localtime()[5])
    
    if created == 0:
        hourlocation = hours * 30
        minlocation = minutes * 6
        seclocation = seconds * 6
        hourhand()
        minutehand()
        secondhand()
        created = 1

    if curenthour != hours:
        updatehour(setback)
        curenthour = hours

    if curentmin != minutes:
        updatemin()
        curentmin = minutes

    if curentsec != seconds:
        updatesec()
        curentsec = seconds

    setbacklocation = setback * 30
    if setbackcheck != setback:
        updatesetback()
        setbackcheck = setback

    root.after(10, my_mainloop)

root.after(0, my_mainloop)

root.mainloop()
