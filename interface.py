# welcome 
print("Welcome to your Local Password Manager")

# TODO: login or create user 
# TODO: set user as logged in

# password to log into manager
master_pass = input("Please enter your master password to continue: ")

# divider 
print('\n-------------------------------------------------------------------------\n')

# login successful
print('Login Successful!\n')

# options to choose from 
# Store existing password
# Retrieve password 
# Generate new secure password
# Change Master password 


print('1. Find password\n2. Store existing password\n3. Generate new secure password\n4. Change master password\n')

valid_option: bool = False
while not valid_option:
    try:
        option = int(input('Please select from an option above (1, 2, 3, 4):'))
        valid_option = True
    except:
        print('Invalid option. Please select a valid number corresponding to your choice')

if option == 1:
    retrieve_key = input('Enter the name of the platform that you wish to see your password of: ')

elif option == 2:
    # store existing password: make a class
    print("TODO")

elif option == 3:
    # Generate randomized password
    print("TODO")

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

else:
    print("invalid option")