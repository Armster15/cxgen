import os, fnmatch

def find(file, path):
    """This function is used to find files
       This function is required to help find tk/tcl dlls."""
    
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, file):
                result.append(os.path.join(root, name))
    return result


def findtkdll():
    PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
    p=PYTHON_INSTALL_DIR

    DLL_FOLDER_LOCATION=p+'\DLLs'
    d=DLL_FOLDER_LOCATION

    alltkdlls=find('tk*.dll',d)

    dll=alltkdlls[-1] #selects the dll for the latest version of tk

    return dll


def findtcldll():
    PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
    p=PYTHON_INSTALL_DIR

    DLL_FOLDER_LOCATION=p+'\DLLs'
    d=DLL_FOLDER_LOCATION

    alltcldlls=find('tcl*.dll',d)

    dll=alltcldlls[-1] #selects the dll for the latest version of tcl

    return dll

def name_plus_version(name):
    """A weird name for a function (I couldn't think of anything better), This
       function adds name by version. name=tcl or tk
       while version=the version of name.
       This function is used for setting required env variables."""

    if name=='tcl':
        try:
            import tkinter
            tkv=tkinter.TkVersion

        except:
            import Tkinter
            tkv=Tkinter.TkVersion

        finally:
            tkv=str(tkv)
            a=name+tkv
            return a

    elif name=='tk':
        try:
            import tkinter
            tclv=tkinter.TclVersion

        except:
            import Tkinter
            tclv=Tkinter.TclVersion

        finally:
            tclv=str(tclv)
            a=name+tclv
            return a

    else:
        error='is not a valid argument for name. Valid arguments are "tcl" or "tk".'
        error="'"+name+"' "+error
        raise SyntaxError(error)
