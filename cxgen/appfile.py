import time

#variables:
#appname= name of app
#filename= the python file
#pyga=variable for storing y/n if the user wants to use pygame
#console=variable for storing y/n if the user wants console
#iconyn=variable for checking whether or not you want icon for app
#iconname=varibale for ico file name

#segment 1: does the opening/intro of app
print("cx_Freeze Script Creator 2.1")
time.sleep(.7)
print("By Armaan Aggarwal")
time.sleep(.7)
print("Loading...")
time.sleep(2.3)

#segment 2: collect user data
print("Type in  the name of your app:")
appname=input()
appname='"'+appname+'",' #don't get overwhelmed, this is for adding quotes to appname for setup file

print("Type in file name with the .py extention:")
filename=input()

print("Are you using pygame? (y/n)")
pyga=input()

print("Do you want the console/shell window? (y/n)")
console=input()

print("Do you want to add an icon to the application? (y/n)")
iconyn=input()
if iconyn=='y':
    print("Type in icon file name (MUST BE A .ico FILE):")
    iconname=input()

#segment 3: print the code.
if pyga=='y':
    print()

    print("Copy and Paste the code below in a new .py file.")
    print("IMPORTANT: Save it in the same folder as",filename)

    print()

    filename='"'+filename+'",'

    print("import cx_Freeze")
    print("from cx_Freeze import *")

    if console=='y':
        print("base=None")
    if console=='n':
        print("import sys")
        print('if sys.platform == "win32":')
        print('     base = "Win32GUI"')

    print()
    print("imodules=['pygame'] #modules to include")
    print()
    print("emodules=[] ###modules to NOT include")
    print("            #(useful if a module is forcefully installed")
    print("            #even if you don't want that module)")
    print()
    print('build_exe_options={"packages":imodules,"excludes":emodules}')
    print()

    print("setup(")
    print('        name=',appname)
    print('        options={"build_exe":build_exe_options},')
    print("        executables=[")
    print("        Executable(")

    if iconyn=='y':
        iconname='"'+iconname+'",'
        print("                ",filename,'base=base,icon=',iconname)

    if iconyn=='n':
        print("                ",filename,'base=base,')

    print("                )")
    print("            ]")
    print("        )")

    while True:
        time.sleep(1)

if pyga=='n':
    print()

    print("Copy and Paste the code below in a new .py file.")
    print("IMPORTANT: Save it in the same folder as",filename)

    filename='"'+filename+'",'

    print()
    print("import cx_Freeze")
    print("from cx_Freeze import *")

    if console=='y':
        print("base=None")
    if console=='n':
        print("import sys")
        print('if sys.platform == "win32":')
        print('     base = "Win32GUI"')

    print()
    print("imodules=[] #modules to include")
    print()
    print("emodules=[] ###modules to NOT include")
    print("            #(useful if a module is forcefully installed")
    print("            #even if you don't want that module)")
    print()
    print('build_exe_options={"packages":imodules,"excludes":emodules}')
    print()
    
    print("setup(")
    print('        name=',appname)
    print('        options={"build_exe":build_exe_options},')
    print("        executables=[")
    print("        Executable(")

    if iconyn=='y':
        iconname='"'+iconname+'",'
        print("                ",filename,'base=base,icon=',iconname)

    if iconyn=='n':
        print("                ",filename,'base=base,')

    print("                )")
    print("            ]")
    print("        )")

