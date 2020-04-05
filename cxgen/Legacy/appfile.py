def main():
    import time
    from . import run
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

    print("Type in file name with the .py extention:")
    filename=input()

    print("Type in a version to give to your executable.")
    _version=input()

    print("Are you using tkinter? (y/n)")
    pyga=input().lower()
    if pyga=='y':
        pyga=True
    else:
        pyga=False

    print("Do you want the console/shell window? (y/n)")
    console=input().lower()
    if console=='y':
        console=True
    else:
        console=False

    print("Do you want to add an icon to the application? (y/n)")
    iconyn=input().lower() #.lower() to make it not case sensitive
    if iconyn=='y':
        print("Type in icon file name (MUST BE A .ico FILE):")
        iconname=input()

    else:
        iconname=None

    # segment 3: print the code.
    code = run(appname,filename,_version,pyga,console,iconname)
    for x in code:
        print(x)
    

    #segment 4: delete variables created
    del appname, filename, _version, pyga, console, iconyn, iconname
