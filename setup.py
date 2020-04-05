import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cxgen",
    version="unstable-3.0.0~", 
    author="Armaan Aggarwal",
    description="A package to generate cx_Freeze setup.py file!",
    python_requires='>=3, <4',
    long_description=long_description,
    packages=setuptools.find_packages(),
    license='MIT',
    url = "https://github.com/armaan115/cxgen",

    include_package_data=True,
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
