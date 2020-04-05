try:
    from . import utils

except:
    import utils
    
import pkg_resources
import sys, os

if sys.version[0]==3:
    from importlib import reload
    #for reload module since it isnt built in Python 3.x


cxcommand = [] #all the code that will be executed soon using the following code
               # for x in cxcommand:
               #    exec(x)

def print2command(*args):
    import sys
    global cxcommand
    """
    Yes, the name is misleading: 
    what the function does is print the inputed text 
    and appends it to this giant list called cxcommand
    """
    fakelist = []
    for z in args:
        #print(z, end = ' ', flush=True)
        fakelist.append(z)
    
    str1 = ' '.join(fakelist)
    cxcommand.append(str1)
    #print()
    
#cxgen.run() variables:
    #for no icon, make icon=None
    #console: True if u want console, False if u don't want console
    #tkinterusage: if u want tkinter, make True, False, if u don't want quit

def run(appname,filename,version,tkinterusage,console,icon, cdFolder = None):
    global cxcommand
    """To learn how cxgen.run() works, call the function 'cxgen.manual()'."""
    
    cxcommand = [] #new running segment, delete old code

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
        # print()

        # print("Copy and Paste the code below in a new .py file.")

        # saveinsamefolder=("IMPORTANT: Save it in the same folder as",filename)
        # saveinsamefolder=str(saveinsamefolder)
        # saveinsamefolder=saveinsamefolder.replace('(','')
        # saveinsamefolder=saveinsamefolder.replace(')','')
        # saveinsamefolder=list(saveinsamefolder)
        # saveinsamefolder[0]=''
        # saveinsamefolder[-1]=''
        # saveinsamefolder=''.join(saveinsamefolder)
        # print(saveinsamefolder,'\n')
        # for x in saveinsamefolder:
        #     print('-',end='')
        # print('\n')
        # #all of this to have a cool line that seperates the notices and code
        
        print2command("import cx_Freeze")
        print2command("from cx_Freeze import *")
        print2command('import os')
        print2command('import os.path')

        print2command()

        if cdFolder != None:
            print2command("os.chdir(r'{}')".format(cdFolder))
            print2command()

        print2command("import sys")
        print2command('sys.argv.append("build")')
        print2command()
        
        if sys.platform == "win32":
            print2command('PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))')
            
            print2command("os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', '{}')"
                .format(utils.name_plus_version('tcl')))
            
            print2command("os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', '{}')"
                .format(utils.name_plus_version('tk')))

        print2command()

        print2command("imodules=['tkinter'] #modules to include")
        print2command()
        print2command("emodules=[] ###modules to NOT include")
        print2command("            #(useful if a module is forcefully installed")
        print2command("            #even if you don't want that module)")
        print2command()

        tkdll='r"'+utils.findtkdll()+'"'
        tcldll='r"'+utils.findtcldll()+'"'
        
        print2command('tkdll={}'.format(tkdll))
        print2command('tcldll={}'.format(tcldll))
        print2command()
        print2command("includefiles=[tkdll,tcldll] #files to include (these can be images, documents, dlls, etc.)")
        print2command()
        print2command("#NOTE: DO NOT remove tcldll and tkdll in includefiles if you are using tkinter.")
        print2command("       #They are required dlls for tkinter to work.")
        print2command('       #But, you can also include other files your program requires')
        print2command()
        print2command('build_exe_options={"packages":imodules,"excludes":emodules,"include_files":includefiles}')

        
        if console==True:
            print2command("base=None")
            
        if console==False:
            print2command("import sys")
            print2command('base = "Win32GUI"')            


        if icon !=None:
            icon='"'+icon+'"'

            print2command("setup(name={}".format(appname), 
            'version="{}",'.format(version),
            'options={"build_exe":build_exe_options},',
            "executables=[Executable({0} base=base, icon = {1}".format(filename, icon),
            ")])"
            )

            #'{0} base=base,icon= {1}'.format(filename,icon),

        if icon==None:
            print2command("setup(name={}".format(appname), 
            'version="{}",'.format(version),
            'options={"build_exe":build_exe_options},',
            "executables=[Executable({} base=base".format(filename),
            ")])"
            )




    if tkinterusage==False:
        
        if icon!=None:
            icon=str(icon)
            
        # print()

        # print("Copy and Paste the code below in a new .py file.")

        # saveinsamefolder=("IMPORTANT: Save it in the same folder as",filename)
        # saveinsamefolder=str(saveinsamefolder)
        # saveinsamefolder=saveinsamefolder.replace('(','')
        # saveinsamefolder=saveinsamefolder.replace(')','')
        # saveinsamefolder=list(saveinsamefolder)
        # saveinsamefolder[0]=''
        # saveinsamefolder[-1]=''
        # saveinsamefolder=''.join(saveinsamefolder)
        # print(saveinsamefolder,'\n')
        # for x in saveinsamefolder:
        #     print('-',end='')
        # print('\n')
        # #all of this to have a cool line that seperates the notices and code
        
        
        print2command("import cx_Freeze")
        print2command("from cx_Freeze import *")
        print2command()

        if cdFolder != None:
            print2command("import os")
            print2command("os.chdir(r'{}')".format(cdFolder))
            print2command()

        print2command("import sys")
        print2command('sys.argv.append("build")')
        print2command()

        print2command("imodules=[] #modules to include")
        print2command()
        print2command("emodules=[] ###modules to NOT include")
        print2command("            #(useful if a module is forcefully installed")
        print2command("            #even if you don't want that module)")
        print2command()

        print2command("includefiles=[] #files to include")
        print2command("                #(these can be images, documents, dlls, etc.)")
        
        print2command()
              
        print2command('build_exe_options={"packages":imodules,"excludes":emodules,"include_files":includefiles}')
        
        
        if console==True:
            print2command("base=None")
        if console==False:
            print2command("import sys")
            print2command('base = "Win32GUI"')

        if console !=True and console != False:
            raise ValueError(console, 'is not a valid argument for the console paramater. To know how to use this paramter, run the "cxgen.manual()" function')

        # print2command("setup(name={}".format(appname), 
        # 'version="{}",'.format(version),
        # 'options={"build_exe":build_exe_options},',
        # "executables=[",
        # "Executable(",
        # "XXX",
        # ")])"
        # )

        if icon !=None:
            icon='"'+icon+'"'

            print2command("setup(name={}".format(appname), 
            'version="{}",'.format(version),
            'options={"build_exe":build_exe_options},',
            "executables=[Executable({0} base=base, icon = {1}".format(filename, icon),
            ")])"
            )

            #'{0} base=base,icon= {1}'.format(filename,icon),

        if icon==None:
            print2command("setup(name={}".format(appname), 
            'version="{}",'.format(version),
            'options={"build_exe":build_exe_options},',
            "executables=[Executable({} base=base".format(filename),
            ")])"
            )

        # print()


    return cxcommand

#cxgen.app() variables:
    #appname= name of app
    #filename= the python file
    #pyga=variable for storing y/n if the user wants to use pygame
    #console=variable for storing y/n if the user wants console
    #iconyn=variable for checking whether or not you want icon for app
    #iconname=varibale for ico file name


def app():
    cxcommand = [] #new running segment, delete old code
    from . import appfile
    appfile.main()
        
def cxgen_license():
    lf=pkg_resources.resource_filename('cxgen','files/LICENSE-for-function.txt')

    with open(lf) as l: # The with keyword automatically closes the file when you are done
        print (l.read())
def manual():
    lfa=pkg_resources.resource_filename('cxgen','files/manual.txt')
    
    with open(lfa) as m: # The with keyword automatically closes the file when you are done
        print (m.read())

