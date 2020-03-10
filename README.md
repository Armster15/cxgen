# cxgen 3.0.0

by Armaan Aggarwal
on March 9, 2020

![alt text](https://i.imgur.com/UMFWB2g.png "The cxgen GUI")

It's been a while (like a year) 
but I have made some new (more like big) 
changes to cxgen!

- There is now a GUI! (cxgen will now be more focused on a GUI converter)
- cxgen stil uses the 2.0.0 framework, it's  just rebranded as cxgenLegacy
- Some changes to the framework so that it could support the GUI
- Python 2 is no longer supported - only Python versions 3+ are supported

## How to use cxgen
**To run the GUI:** `from cxgen import GUI`

### Legacy
To run the legacy based console application: 

    from cxgen.Legacy import app
    app()

To run the legacy method to generate cx_Freeze setup code:

    from cxgen.Legacy import run
    run()

