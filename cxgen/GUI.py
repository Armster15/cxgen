try: from .Legacy import run as cxgen
except: from Legacy import run as cxgen
    
try: from .utils import *
except: from utils import *

from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename, askopenfile, askopenfilenames, askopenfiles, asksaveasfile, asksaveasfilename
from tkinter.messagebox import *
from threading import Thread
import time

root = Tk()
root.title("cxgen 3")

#TODO: Add an abort function and a GUI output window

def changeState(state):
    """
    Changes the state of all the tkinter elements to either normal or diabled
    state can take two of values: "normal" and "disabled"  
    """
    global nameEntry, versionEntry, pathEntry, pathButton
    global tKUsageR1, tKUsageR2, consoleR1, consoleR2
    global iconUsageR1, iconUsageR2
    global iconUsageR1, iconUsageR2, convertButton
    global iconEntry
    global iconButton

    elements = [
        nameEntry, versionEntry, pathEntry, pathButton,
        tKUsageR1, tKUsageR2, consoleR1, consoleR2,
        iconUsageR1, iconUsageR2,
        iconUsageR1, iconUsageR2, convertButton
        ] #seem familliar?
    
    try: 
        elements.append(iconEntry)
        elements.append(iconButton)

    except: pass
    # if iconEntry/Button doesn't "exist", don't kill the whole thing

    for e in elements:
        if state == "normal":
            e.config(state = NORMAL)
        elif state == "disabled":
            e.config(state = DISABLED)
    

def selectIcon():
    global iconVar
    global iconEntry
    iconfile = askopenfilename()
    if iconfile != None and iconfile != " " and iconfile != "": #just dont do anything if the user presses cancel or doesnt select anything
        if fileExt(iconfile) != '.ico':
            showwarning("Icon File Type Warning", 
            "Please use a .ico file for the icon. This is simply a warning and you may choose to dismiss it.")
        
        iconEntry.delete(0,END) #deletes current text
        iconEntry.insert(0,iconfile) #insers text for iconpath

        # print(iconVar.get())


def selectMainFile():
    global pathVar
    global pathEntry
    mainfile = askopenfilename()
    if mainfile != None and mainfile != " " and mainfile != "": #just dont do anything if the user presses cancel or doesnt select anything
        pathEntry.delete(0,END) #deletes current text
        pathEntry.insert(0,mainfile) #insers text for iconpath

        # print(iconVar.get())

def iconSelection(yes_or_no):
    global iconButton
    global iconEntry 
    global iconLabel
    global iconVar
    if yes_or_no == 1:
        iconVar = StringVar()

        iconLabel = Label(text = "Icon File ")
        iconLabel.grid(row = 7, column = 0)

        iconEntry = Entry(width = 40, textvariable = iconVar)
        iconEntry.grid(row = 7, column = 1, columnspan = 1)

        iconButton = Button(text = "Select File", width = 16, bd = 4, command = selectIcon)
        iconButton.grid(row = 7, column = 2)
    
    elif yes_or_no == 0:
        hide_me(iconLabel)
        hide_me(iconEntry)
        hide_me(iconButton)


def convert():
    """The juicy stuff"""
    def main():
        global nameVar, versionVar, pathVar, tkUsageVar, consoleVar
        global iconUsageVar, iconVar, convertButton, dataLabel
        
        hide_me(dataLabel)

        if iconUsageVar.get() == 1:
            icon = iconVar.get()
        elif iconUsageVar.get() == 0:
            icon = None

        directory = askdirectory()

        if directory == None or directory == " " or directory == "":
            directory = None
            return #ABANDON SHIP

        name = nameVar.get()
        version = versionVar.get()
        path = pathVar.get()
        tkUsage = tkUsageVar.get()
        console = consoleVar.get()

        errorList = []
        
        if noneFunc(name) == True: errorList.append('Name')
        if noneFunc(version) == True: errorList.append('Version')
        if noneFunc(path) == True: errorList.append('Main File')
        if noneFunc(tkUsage) == True: errorList.append('Tkinter Usage')
        if noneFunc(console) == True: errorList.append('Console Usage')
        if iconUsageVar.get() == 1 and noneFunc(icon) == True: errorList.append("Icon")
            
        if len(errorList) >= 1:
            dataLabel.config(
                text = "Error: The following parameters weren't supplied: {} \n".format(errorList),
                fg = "red")

            dataLabel.grid(row = 9, column = 1)
            
            return

        cxcommand = cxgen(name,path,version,tkUsage,console,icon, cdFolder = directory)
        
        changeState("disabled") #disable all the widgets
        dataLabel.config(
                text = "Converting... Please refer to the output window for debugging information. \n".format(errorList),
                fg = "blue")
        dataLabel.grid(row = 9, column = 1)

        #the engine that runs it all...
        for x in cxcommand:
            exec(x)
        
        changeState("normal") #re-enable all the widgets
        

        print("==========")
        print("Task Ended")
        print("==========")

        dataLabel.config(
                text = "Task Ended \n".format(errorList),
                fg = "blue")
        dataLabel.grid(row = 9, column = 1)

    mainThread = Thread(target=main)
    mainThread.start()


mainLabel = Label(text = "cxgen 3 \n", font=("FakeFontOnPurpose", 23))
mainLabel.grid(row = 0, column = 1)

nameVar = StringVar()
nameLabel = Label(text = "Name of App ")
nameLabel.grid(row = 1, column = 0)
nameEntry = Entry(width = 60, textvariable = nameVar)
nameEntry.grid(row = 1, column = 1, columnspan = 3)

versionVar = StringVar()
versionLabel = Label(text = "Version ")
versionLabel.grid(row = 2, column = 0)
versionEntry = Entry(width = 60, textvariable = versionVar)
versionEntry.grid(row = 2, column = 1, columnspan = 3)

pathVar = StringVar()
pathLabel = Label(text = "Main File ")
pathLabel.grid(row = 3, column = 0)
pathEntry = Entry(width = 40, textvariable = pathVar)
pathEntry.grid(row = 3, column = 1, columnspan = 1)
pathButton = Button(text = "Select File", width = 16, bd = 4, command = selectMainFile)
pathButton.grid(row = 3, column = 2)

tkUsageVar = BooleanVar()
tkUsageLabel = Label(text = "Are you using tkinter?")
tkUsageLabel.grid(row = 4, column = 0)
tKUsageR1 = Radiobutton(text = "Yes", variable = tkUsageVar, value = True)
tKUsageR1.grid(row = 4, column = 1)
tKUsageR2 = Radiobutton(text = "No", variable = tkUsageVar, value = False)
tKUsageR2.grid(row = 4, column = 2)

consoleVar = BooleanVar()
consoleLabel = Label(text = "Do you want the console/shell window?")
consoleLabel.grid(row = 5, column = 0)
consoleR1 = Radiobutton(text = "Yes", variable = consoleVar, value = True)
consoleR1.grid(row = 5, column = 1)
consoleR2 = Radiobutton(text = "No", variable = consoleVar, value = False)
consoleR2.grid(row = 5, column = 2)

iconUsageVar = IntVar() #The code is working, I'm not gonna take the risk just to change it to a BooleanVar() (if it ain't broke, don't fix it!)
iconUsageLabel = Label(text = "Do you want an icon? (Use a .ico file)")
iconUsageLabel.grid(row = 6, column = 0)
iconUsageR1 = Radiobutton(text = "Yes", variable = iconUsageVar, value = 1, command = lambda: iconSelection(1))
iconUsageR1.grid(row = 6, column = 1)
iconUsageR2 = Radiobutton(text = "No", variable = iconUsageVar, value = 0, command = lambda: iconSelection(0))
iconUsageR2.grid(row = 6, column = 2)

convertButton = Button(command = convert, text = "Create {}-bit Build".format(pythonbit()), width = 64, bd = 4)
convertButton.grid(row=8,column=1)

diagnosticData = Label(text = "\n Python Version: {0} \n Bit Type: {1}-bit \n OS: {2} \n".format(pythonVersion(),pythonbit(),getOS())
,font=("FakeFontOnPurpose", 8))
diagnosticData.grid(row=8,column=2)

dataLabel = Label(fg = "blue")
dataLabel.grid(row = 9, column = 1)
hide_me(dataLabel)

root.mainloop()