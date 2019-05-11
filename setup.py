import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cxgen",
    version="1.0.1", 
    author="Armaan Aggarwal",
    description="A package to generate cx_Freeze setup.py file!",
    long_description=long_description,
    packages=setuptools.find_packages(),

##    data_files=[('', ['cxgen/files/manual.txt'])],
    include_package_data=True,
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
