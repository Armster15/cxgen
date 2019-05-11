import time
import pkg_resources
name = "cxgen"

#cxgen.run() variables:
    #for no icon, make icon=None
    #console: True if u want console, False if u don't want console
    #pygameusage: if u want pygame, make True, False, if u don't want quit
def run(appname,filename,pygameusage,console,icon):

    if icon!=None:
        icon=str(icon)

    appname=str(appname)
    filename=str(filename)
    
    appname='"'+appname+'",'
    filename='"'+filename+'",'

    if pygameusage==True:
        print()

        print("Copy and Paste the code below in a new .py file.")
        print("IMPORTANT: Save it in the same folder as",filename)
        print()
        
        print("import cx_Freeze")
        print("from cx_Freeze import *")

        print("imodules=['pygame'] #modules to include")
        print()
        print("emodules=[] ###modules to NOT include")
        print("            #(useful if a module is forcefully installed")
        print("            #even if you don't want that module)")
        print()
        print('build_exe_options={"packages":imodules,"excludes":emodules}')

        
        if console==True:
            print("base=None")
            
        if console==False:
            print("import sys")
            print('if sys.platform == "win32":')
            print('     base = "Win32GUI"')
##        if console != True or False:
##            raise ValueError(console, "is not a valid argument for the console paramater. To know how to use this paramter, run the 'cxgen.manual()' function")


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


    if pygameusage==False:
        
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
        print('build_exe_options={"packages":imodules,"excludes":emodules}')

        
        if console==True:
            print("base=None")
        if console==False:
            print("import sys")
            print('if sys.platform == "win32":')
            print('     base = "Win32GUI"')

##        if console !=True or False:
##            raise ValueError(console, 'is not a valid argument for the console paramater. To know how to use this paramter, run the "cxgen.manual()" function')

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


##    if pygameusage !=True:
##        raise ValueError(pygameusage, "is not a valid argument for the pygameusage paramater. To know how to use this paramter, run the 'cxgen.manual()' function")
##
##    if pygameusage !=False:
##        raise ValueError(pygameusage, "is not a valid argument for the pygameusage paramater. To know how to use this paramter, run the 'cxgen.manual()' function")

#cxgen.app() variables:
    #appname= name of app
    #filename= the python file
    #pyga=variable for storing y/n if the user wants to use pygame
    #console=variable for storing y/n if the user wants console
    #iconyn=variable for checking whether or not you want icon for app
    #iconname=varibale for ico file name


def app():
    import cxgen.appfile

def cxgen_license():
    lf=pkg_resources.resource_filename('cxgen','files/LICENSE-for-function.txt')

    with open(lf) as l: # The with keyword automatically closes the file when you are done
        print (l.read())
def manual():
    lfa=pkg_resources.resource_filename('cxgen','files/manual.txt')
    
    with open(lfa) as m: # The with keyword automatically closes the file when you are done
        print (m.read())

def about():
    print("About cxgen 1.0.2")
    print()
    print("Created by Armaan Aggarwal on April 18, 2019")

print("cxgen 1.0.1 successfully imported")
print("To see the manual of cxgen 1.0.2, use the command 'cxgen.manual()'")

