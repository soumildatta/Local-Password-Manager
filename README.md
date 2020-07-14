# Local-Password-Manager
This is a simple command line interface password manager written in Python which stores all of your manually inputted passwords locally. All the passwords are encrypted before storing to keep them secure. All of the passwords are stored in a .db file in the folder containing the this program's files. 

## Get started
To get this running on your local machine, make sure you have Python 3.6 or higher installed. 
Follow [this link](https://www.python.org/downloads/) to download Python.

Next, if you do not have PIP(Python Package Manager) already, install it on your computer as it will be used to download the packages necessary for this application. 
Follow the instructions [here](https://pip.pypa.io/en/stable/installing/) to install PIP. 

Install the cryptography library using PIP:
``` python
pip install cryptography
```

Go inside the cloned project directory. Run the **interface.py** file in your terminal:
``` python
python interface.py
```

# Using the password manager
**The choices in this program are based on numerical input. Type the number corresponding to your choice and hit enter to pick the choice.**  
When you start the program (interface.py), it will prompt you to log in or sign up. If this is your first time using this program, choose sign up (2) and enter a password that you will use to log into the program every time.  
If this is not your first time, then choosing login (1) and entering your password will log you into the password manager.    
From there, you find the basic password manager functions which are - **find a password (1)** and **store a password (2)**. You can also choose to **generate a random 18 character password (3)** consisting of numbers, and uppercase and lowercase letters. The program will then automatically store the generated random password for the platform that the user specifies.   
### What to do if you forget the master-password
We are only human. Sometimes our memory fails us, and in that case, it is easy to reset the password manager to make it functional again.
Simply go to the directory that contains the **_database.py_** file of the program. In that directory, delete the file named **_database.db_** and it will reset the password manager database, allowing you to create a new superuser. 
