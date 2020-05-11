import database
# import only system from os 
from os import system, name 
    
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 


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


# welcome 
print("Welcome to your Local Password Manager")

# TODO: login or create user 
# TODO: set user as logged in

# password to log into manager
master_pass: str = input("Please enter your master password to continue: ")

db = database.Database()

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
        # Find a password
        if option == 1:
            retrieve_platform: str = input('Enter the name of the platform that you wish to see your password of: ')

            clear()
            db.retrievePassword(retrieve_platform)
            
            repeat = quitApp()

        # Store an existing password
        elif option == 2:
            # store existing password: make a class
            clear()

            print("Store a password\n")

            # values for query
            platform_name: str = input("Enter the name of the platform: ")
            username: str = input("Enter your username: ")
            password: str = input("Enter your password: ")

            # TODO: implement storePassword Method here
            db.storePassword(platform_name, username, password)

            repeat = quitApp()

        # Generate and store password
        elif option == 3:
            # Generate randomized password
            print("TODO")
            
            repeat = quitApp()

        elif option == 4:
            # changing master password 
            master = input('Enter your current master password: ')

            valid_master = False
            while not valid_master:
                if master:
                    new_master = input('Enter a new master password: ')
                    valid_master = True
                else:
                    print('Master output incorrect')

            repeat = quitApp()

        elif option == 5:
            clear()
            print("\nGoodbye!")
            break

        else:
            print("invalid option")

else:
    print("\nWrong password!")

