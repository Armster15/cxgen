def pythonbit():
    """Returns 64 or 32 depending if the python interpreter is 32 or 64 bit"""
    import struct
    return struct.calcsize("P") * 8

def pythonVersion():
    """Returns python version in a string format"""
    from platform import python_version
    return python_version()

def getOS():
    """Returns operating system"""
    import platform
    return platform.system()

def hide_me(event):
    """
    Hides an event/widget, but doesn't get rid of it,
    Use .grid() to respawn the widget
    """
    event.grid_forget()

def fileExt(filename):
    """Returns file extension of inputed filename. One paramater is required: filename"""
    import os
    return os.path.splitext(filename)[1]

def noneFunc(thing):
    """
    Function checks if nothing is supplied

    Returns True if nothing it is "null"
    Returns False if it haves stuff
    """
    if thing == None or thing == " " or thing == "":
        return True
    else:
        return False