import time

#variables:
#appname= name of app
#filename= the python file
#pyga=variable for storing y/n if the user wants to use tkinter
#console=variable for storing y/n if the user wants console
#iconyn=variable for checking whether or not you want icon for app
#iconname=varibale for ico file name
#error=variable for error messages that should be displayed (basically what to tell the user if they screw up)


#segment 1: does the opening/intro of app
print("cx_Freeze Script Creator (the cxgen App)")
time.sleep(.7)
print("By Armaan Aggarwal")
time.sleep(.7)

#segment 2: collect user data
print("Type in the name of your app:")
appname=input()
appname='"'+appname+'",' #don't get overwhelmed, this is for adding quotes to appname for setup file

print("Type in file name with the .py extention:")
filename=input()

print("Are you using tkinter? (y/n)")
pyga=input()

print("Do you want the console/shell window? (y/n)")
console=input()

print("Do you want to add an icon to the application? (y/n)")
iconyn=input()
if iconyn=='y':
    print("Type in icon file name (MUST BE A .ico FILE):")
    iconname=input()

#segment 3: print the code.
error=None #because the user didn't make any mistakes (yet)
if pyga in 'Yy':
    print()

    print("Copy and Paste the code below in a new .py file.")
    print("IMPORTANT: Save it in the same folder as",filename)

    print()

    filename='"'+filename+'",'

    print("import cx_Freeze")
    print("from cx_Freeze import *")

    if console in 'Yy':
        print("base=None")
    if console in 'Nn':
        print("import sys")
        print('if sys.platform == "win32":')
        print('     base = "Win32GUI"')

    print()
    print("imodules=['tkinter'] #modules to include")
    print()
    print("emodules=[] ###modules to NOT include")
    print("            #(useful if a module is forcefully installed")
    print("            #even if you don't want that module)")
    print()
    
    print("includefiles=[tkdll,tcldll] #files to include (these can be images, documents, dlls, etc.)")
    print()
    
    print("#NOTE: DO NOT remove tcldll and tkdll in includefiles if you are using tkinter.")
    print("       They are required for tkinter to work")
    print('       But, you can also include other files if your program requires. This is not required.')
    
    print()
    print('build_exe_options={"packages":imodules,"excludes":emodules,include_files:includefiles}')

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

if pyga in 'Nn':
    print()

    print("Copy and Paste the code below in a new .py file.")
    print("IMPORTANT: Save it in the same folder as",filename)

    filename='"'+filename+'",'

    print()
    print("import cx_Freeze")
    print("from cx_Freeze import *")

    if console in 'Yy':
        print("base=None")
    if console in 'Nn':
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

    print("includefiles=[] #files to include (these can be images, documents, dlls, etc.")
    print("                #You aren't required to add files in this list.")
    print()

    print('build_exe_options={"packages":imodules,"excludes":emodules,include_files:includefiles}')
    print()
    
    print("setup(")
    print('        name=',appname)
    print('        options={"build_exe":build_exe_options},')
    print("        executables=[")
    print("        Executable(")

    if iconyn in 'yY':
        iconname='"'+iconname+'",'
        print("                ",filename,'base=base,icon=',iconname)

    if iconyn in 'Nn':
        print("                ",filename,'base=base,')

    print("                )")
    print("            ]")
    print("        )")

    if pyga not in 'Yy' and pyga not in 'Nn':
        error="is not a valid value for the tkinter usage. The correct usage is the standard y/n."

        pyga=str(pyga)
        pyga="'"+pyga+"' " #adds a space at the end of tkinter usage for formatting reasons

        error=pyga+error #creates the 'final draft' of the error
        
        raise ValueError(error)


del error, pyga, iconyn, console, filename, appname
