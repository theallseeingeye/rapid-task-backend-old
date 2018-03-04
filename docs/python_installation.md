Installing Python
=================

**Package Versions Required:**  
Python 3.6.3  
virtualenv 15.1.0

For Windows:
------------

1. Install Python from [LINK](https://www.python.org/downloads/). Please make sure it is the 
    correct version.
1. Open the download
1. Customize the install path to a simple directory path.
1. Make sure to check the "Add Python *version#* to PATH" box, as shown at bottom of 
    image.  
![Python Installation](/docs/images/python_add_path.png)
1. Complete the installation.
1. Open the window's cmd.exe.
1. Type in the cmd.exe line: ```Python```.
1. It should print out the Python with the correct version number as above.  
![Python cmd](/docs/images/python_cmd.png)  
    *If it does not show this, please run through the installation again and double check that you have add Python to 
    PATH checked.* 

#### Yay! Python is installed!

### Setting up the Virtual Environment

You will need to install and be running on virtualenv. 

**Pycharm users**:
* Pycharm makes the handling of virtual environments easy and has a setup tool built in.
    1. From a **new** project:
        1. Open a ```New Project``` in Pycharm
        1. It has near the top, there is a "Interpreter" field. Click on the gear on the right and select ```Create 
            VirtualEnv```.  
        1. Now name your virtual environment, choose where you want it stored (Keep it out of project root directory) 
            and point the interpreter to the python.exe you have installed.
        1. Click ```Okay``` and your virtual environment will be created with new project.
    1. From an **existing** project:
        1. Select ```File/Settings/Project:name/Project Interpreter```. Click the gear icon to the right of "Project
            Interpreter" then select ```Create VirtualEnv```.
        1. Now name your virtual environment, choose where you want it stored (Keep it out of project root directory) 
            and point the interpreter to the python.exe you have installed.
        1. Click ```Okay``` and your virtual environment will be created.
        1. Open the Terminal and you should see your named virtual environment in brackets before the directory. This
            indicates the virtual environment you are working on. Always work on your environment when developing.  
            
**Non-Pycharm users**:  

We can use pip, which is already pre-packaged with Python. Pip is a handler for downloading and installing packages.  

Using cmd.exe
1. Check that you have pip installed by typing: ```pip -V```. It should show you the version number and directory it's 
    from.
1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/), use this command: 
```pip install virtualenv==X.X.X```.
1. install [virtualenvwrapper-win](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) by typing
```pip install virtualenvwrapper-win```. This will save from typing long repetitive command lines for virtualenv.
* Setup a virtual environment by following this manual: 
[virtualenvwrapper-win](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)  
![creating Virtual Environments](/docs/images/creating_virtual_env.png)  

    * Now it is set up where you need to activate the virtual environment, type ````workon```` then the name of the 
    environment. If you need to quit the environment, type ````deactivate````.
    
 
For Mac OS X:
-------------
*Please contribute as you go through this for the first time.*



