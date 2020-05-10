# welcome 
print("Welcome to your Local Password Manager")

# password to log into manager
# master_pass = input("Please enter your master password to continue: ")

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
