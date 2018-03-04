HOW TO INSTALL RAPID TASK FOR WINDOWS
=====================================

Welcome to the installation manual to have Rapid Task up and running! 

Table of Contents
-----------------
Setup Backend with Pycharm  
Setup Backend without Pycharm
Setup Frontend


Setup Backend with Pycharm
-------------------------
You will need to have your system setup with Python.  
    Instructions are [here](/docs/python_installation.md) for these following steps:
1. Have Python 3.6.3 installed. 
[Download Link](https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe). 
1. Have Git installed on to your computer if you don't have it already. [Git Home Page](https://git-scm.com/)
1. Have Pycharm installed. [Pycharm Home Link](https://www.jetbrains.com/pycharm/)
    
### Installation Steps

1. Open Pycharm.
1. If it opens an existing project: ```File>Close Project```
1. You should be on the main opening screen. 
1. Setup Git on Pycharm
    1. Open: ```Configure>Settings>Version Control>Git```
    1. Select: Path to Git Executable and point it to your location of *git.exe* installed. 
    (Default: *```c:/Program Files/Git/cmd/git.exe```*) 
    1. Click on ```test``` to see if it works
1. Setup your GitHub on Pycharm
    1. Open: ```Configure>Settings>Version Control>GitHub```
    1. Enter the following:
        1. Host: ```github.com```
        1. Auth Type: ```Token```
        1. Click on ```Create API Token```
        1. Enter your credentials
        1. Click ```test``` to ensure it worked
1. Then in the menus- open: ```Check out From Version Control>GitHub```  
    Enter the following:  
    * Git Repository URL: ```git@github.com:rapidtask/website.git```
    * Parent Directory: *Choose a path to store the files*
    * Directory Name: ```website```    
    ***Review the github_tutorial doc as needed**
1. Setup your virtual environment
    1. Open: ```File>Settings>Project: name>Project Interpreter```
        1. If you already have an existing: Click on the *gear* icon and select: ```Add Local```
        1. If you don't have and virtual environment setup:
            1. Click on the *gear* icon and select: ```Create VirtualEnv```
                1. Name: *Create a name for your environment (ex. rapidtaskenv)*
                1. Location: *Choose a path to store your environment- don't pick the same root as your project folders*
                1. Base Interpreter: *Find the original python.exe that you have first installed*
                1. Select: ```ok``` and it will create an environment for you to work on.
1. Now install the requirements into the virtual environment:
    1. Open Terminal
    1. Make sure you are in your environment (ex. ```(rapidtaskenv) c:/directory/path/of/project```)
    1. type: (In project root) ```pip install -r requirements/local.txt```
    1. This will install the files required onto the virtual environment for your project.
1. Create a secret key file  
    1. Under root of project, create a file called: ```secrets.json```  
    1. Enter the following in the *secrets.json*:    
    ```
    {   
    "FILENAME": "secrets.json",    
    "SECRET_KEY": "*Your secret key must be placed here!*",  
    "DATABASES_HOST": "127.0.0.1",  
    "PORT": "5432"
    "DATABASE_PASSWORD": "*Your Database password placed here*"  
    }
    ```
    * Make sure this file is marked in the .gitignore file - ```/secrets.json``` (VERY IMPORTANT- Should be already
        included in the file when you downloaded from github.)
    * Do not misplace your *secret key*. If you suspect or accidentally shown the *secret key* publicly
        PLEASE ALERT US! This is a SEVERE security risk and will need to create a new secret key.
    1. Save the file
    **NOTE: DO NOT ADD ```secrets.json``` TO VERSION CONTROL**
1. Now we need to install the database with the program.  
    * Install PostgreSQL https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows
    * Select PostgreSQL 9.6 version
    * Follow the installation steps.
    * Open the pgAdmin 4 and create the database (or you can use the shell command line)
    * To make your new database compatible with the project, we need to use the correct names that are already set in
        the settings folders:
        * Create user name ```postgres```
        * Create database named ```rapidtaskdb```
        * Choose your password and place it in the ```secrets.json``` you have created earlier.
1. Now the final step- Setting up the Python Console  
    We need to tell python to run the right settings folder for our project. This following example works if you are
        setting up in the local environment of your computer. Everytime you type ```python manage.py runserver```, it
        will know which settings file to use:  
    * Open the python console (not the one in terminal, or open python in terminal)
    * Type the following into the python console:  
    ```
    import django
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    django.setup()
    ```
Setup Backend Without Pycharm
-----------------------------

You will need to have your system setup with Python and a working virtual environment.  
    Instructions are [here](/docs/python_installation.md) for these following steps:
1. Have Python 3.6.3 installed. 
[Download Link](https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe). 
1. Have virtualenv 15.1.0 installed. See ["Setting up the Virtual Environment"](/docs/python_installation.md) in
    python_installation.md
1. Have git installed on to your computer if you don't have it already. [Git Home Page](https://git-scm.com/)
1. Install GitHub Desktop Client for easy version control handling [GitHub Desktop Link](https://desktop.github.com/), or can use bash console from Git directly. 
    

3) Download the Rapid Task github repository from www.github.com/rapidtask/website

**NEXT STEPS**
1) Activate your virtualenv
2) In the directory you wish to install, using command-line:
    pip install -r /website/requirements/local.txt

