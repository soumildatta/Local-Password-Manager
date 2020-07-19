import database
# import only system from os 
from os import system, name
import sys 
import random
import string
    
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 

def randomPassword():
    password_items = []

    letters = string.ascii_letters
    numbers = [x for x in range(0, 10)]

    counter = 0
    while counter <= 8:
        password_items.append(random.choice(letters))
        password_items.append(str(random.choice(numbers)))
        counter += 1

    final = ""
    for x in password_items:
        final += x

    return final    

def quitApp() -> bool:
    print("\n\nWould you like to:\n1. Pick another option\n2. Quit Application")
    choice = int(input(": "))
    if choice == 1:
        repeat = True
    elif choice == 2:
        repeat = False
    else: 
        print("Invalid choice\n")

    return repeat


db = database.Database()


# welcome 
clear()
print("Welcome to your Local Password Manager")

login_option = int(input("\nWould you like to\n1. Login\n2. Sign up\n3. Quit\n: "))

master_pass = ""
if login_option == 1:
    # password to log into manager
    master_pass: str = input("Please enter your master password to continue: ")

elif login_option == 2:
    bool = db.createTable()
    if bool:
        password = input("Please enter a master password (you will use this every time to log into this application)\n: ")
        db.createMasterPass(password)
        master_pass = password
    else: 
        sys.exit()


elif login_option == 3:
    sys.exit()
    
else:
    print("\nInvalid choice")
    sys.exit()
    
if db.checkMasterPass(master_pass):
    print('\n-------------------------------------------------------------------------\n')

    # login successful
    print('Login Successful!\n')

    # options to choose from 
    # Store existing password
    # Retrieve password 
    # Generate new secure password
    # Change Master password 

    repeat = True
    while repeat:
        clear()
        print('1. Find password\n2. Store a password\n3. Generate new secure password\n4. Change master password\n5. Exit\n')

        valid_option = False
        while not valid_option:
            try:
                option = int(input('Please select from an option above (1, 2, 3, 4, 5): '))
                valid_option = True
            except:
                print('Invalid option. Please select a valid number corresponding to your choice')


        #! OPTIONS
        #* Find a password
        if option == 1:
            retrieve_platform: str = input('Enter the name of the platform that you wish to see your password of: ')

            clear()
            db.retrievePassword(retrieve_platform)
            
            repeat = quitApp()

        #* Store an existing password
        elif option == 2:
            # store existing password: make a class
            clear()

            print("Store a password\n")

            # values for query
            platform_name: str = input("Enter the name of the platform: ")
            username: str = input("Enter your username: ")
            password: str = input("Enter your password: ")

            db.storePassword(platform_name, username, password)

            repeat = quitApp()

        #* Generate and store password
        elif option == 3:
            # Generate randomized password
            print("Generate a random password")

            platform: str = input("Enter the name of the platform: ")
            username: str = input("Enter your username for this platform: ")
            
            generated_password = randomPassword()
            print(f"\nGenerated password: {generated_password}")

            db.storePassword(platform, username, generated_password)

            repeat = quitApp()

        # change master password
        elif option == 4:
            master = input('Enter your current master password: ')
            master_authenticated = db.checkMasterPass(master)

            if master_authenticated:
                clear()
                new_master = input('Enter a new master password: ')
                
                db.updateMasterPass(new_master)
            else:
                print("Wrong password")

            repeat = quitApp()
        
        #* Exit
        elif option == 5:
            clear()
            print("\nGoodbye!")
            break

        else:
            print("invalid option")

else:
    print("\nWrong password!")
