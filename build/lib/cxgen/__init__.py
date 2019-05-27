import time
import pkg_resources

name = "cxgen"
version='1.0.2.2'

#cxgen.run() variables:
    #for no icon, make icon=None
    #console: True if u want console, False if u don't want console
    #tkinterusage: if u want tkinter, make True, False, if u don't want quit
def run(appname,filename,tkinterusage,console,icon):
    """To learn how cxgen.run() works, call the function 'cxgen.manual()'."""

    if console != True and console != False:
        error="is not a valid value for the console parameter. Learn more about this paramter by calling 'cxgen.manual()'"

    if tkinterusage != True and tkinterusage != False:
        error="is not a valid value for the tkinterusage parameter. Learn more about this paramter by calling 'cxgen.manual()'"

        tkinterusage=str(tkinterusage)
        tkinterusage="'"+tkinterusage+"' " #adds a space at the end of tkinterusage for formatting reasons

        error=tkinterusage+error #creates the 'final draft' of the error
        
        raise ValueError(error)

        console=str(console)
        console="'"+console+"' " #adds a space at the end of console for formatting reasons

        error=console+error #creates the 'final draft' of the error
        
        raise ValueError(error)

    if icon!=None:
        icon=str(icon)

    appname=str(appname)
    filename=str(filename)
    
    appname='"'+appname+'",'
    filename='"'+filename+'",'

    if tkinterusage==True:
        print()

        print("Copy and Paste the code below in a new .py file.")
        print("IMPORTANT: Save it in the same folder as",filename)
        print()
        
        print("import cx_Freeze")
        print("from cx_Freeze import *")

        print("imodules=['tkinter'] #modules to include")
        print()
        print("emodules=[] ###modules to NOT include")
        print("            #(useful if a module is forcefully installed")
        print("            #even if you don't want that module)")
        print()
        
        print('import pkg_resources as p')
        print('tkdll=p.resource_filename("cxgen","/files/tk86t.dll)')
        print('tcldll=p.resource_filename("cxgen","/files/tcl86t.dll)')
        print()
        print("includefiles=[tkdll,tcldll] #files to include (these can be images, documents, dlls, etc.)")
        print()
        print("#NOTE: DO NOT remove tcldll and tkdll in includefiles if you are using tkinter.")
        print("       #They are required dlls for tkinter to work.")
        print('       #But, you can also include other files your program requires')
        print()
        print('build_exe_options={"packages":imodules,"excludes":emodules,include_files:includefiles}')

        
        if console==True:
            print("base=None")
            
        if console==False:
            print("import sys")
            print('if sys.platform == "win32":')
            print('     base = "Win32GUI"')
            


        print("setup(")
        print('        name=',appname)
        print('        options={"build_exe":build_exe_options},')
        print("        executables=[")
        print("        Executable(")

        if icon != None:
            iconname='"'+iconname+'",'
            print("                ",filename,'base=base,icon=',icon)


        if icon==None:
            print("                ",filename,'base=base,')

        print("                )")
        print("            ]")
        print("        )")



    if tkinterusage==False:
        
        if icon!=None:
            icon=str(icon)
            
        print()

        print("Copy and Paste the code below in a new .py file.")
        print("IMPORTANT: Save it in the same folder as",filename)
        print()
        print("import cx_Freeze")
        print("from cx_Freeze import *")
        print()

        
        print("imodules=[] #modules to include")
        print()
        print("emodules=[] ###modules to NOT include")
        print("            #(useful if a module is forcefully installed")
        print("            #even if you don't want that module)")
        print()

        print("includefiles=[] #files to include")
        print("                #(these can be images, documents, dlls, etc.)")
        
        print()
              
        print('build_exe_options={"packages":imodules,"excludes":emodules,include_files:includefiles}')
        
        
        if console==True:
            print("base=None")
        if console==False:
            print("import sys")
            print('if sys.platform == "win32":')
            print('     base = "Win32GUI"')

        if console !=True or console != False:
            raise ValueError(console, 'is not a valid argument for the console paramater. To know how to use this paramter, run the "cxgen.manual()" function')

        print("setup(")
        print('        name=',appname)
        print('        options={"build_exe":build_exe_options},')
        print("        executables=[")
        print("        Executable(")

        if icon !=None:
            icon='"'+icon+'",'
            print("                ",filename,'base=base,icon=',icon)

        if icon==None:
            print("                ",filename,'base=base,')

        print("                )")
        print("            ]")
        print("        )")




#cxgen.app() variables:
    #appname= name of app
    #filename= the python file
    #pyga=variable for storing y/n if the user wants to use pygame
    #console=variable for storing y/n if the user wants console
    #iconyn=variable for checking whether or not you want icon for app
    #iconname=varibale for ico file name


def app():
    from cxgen import appfile
        
def cxgen_license():
    lf=pkg_resources.resource_filename('cxgen','files/LICENSE-for-function.txt')

    with open(lf) as l: # The with keyword automatically closes the file when you are done
        print (l.read())
def manual():
    lfa=pkg_resources.resource_filename('cxgen','files/manual.txt')
    
    with open(lfa) as m: # The with keyword automatically closes the file when you are done
        print (m.read())

def about():
    print("About cxgen {}".format(version))
    print()
    print("Created by Armaan Aggarwal on May 26, 2019")

