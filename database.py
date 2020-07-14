import sqlite3
import hashing
from cryptography.fernet import Fernet
import sys

class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
    
    def createTable(self):
        try:
            self.cursor.execute('''CREATE TABLE passwords (
                platform text, 
                username text,
                password text,
                key text
            )''')
            self.conn.commit()

            print('\nNew table created')
            return True
        except:
            print('\nUser already exists')
            return False
    
    def createMasterPass(self, password):
        hashed_password = hashing.hashPassword(password)
        self.cursor.execute('INSERT INTO passwords VALUES ("none", "master_pass", ?, "none")', (hashed_password,))
        self.conn.commit() 
        print("\nSuperuser created")

    def checkMasterPass(self, master_password) -> bool:
        try:
            for row in self.cursor.execute('SELECT password FROM passwords WHERE username = "master_pass"'):
                password = row[0]

            # entered_password = hashing.hashPassword(self.master_password)
            check = hashing.verifyPassword(password, master_password)
            return check
        except:
            print("Sign up first!")
            sys.exit()
            

    def storePassword(self, platform, username, password):
        try:
            key = Fernet.generate_key()
            fnet = Fernet(key)

            encrypted_password = fnet.encrypt(str.encode(password))

            self.cursor.execute('INSERT INTO passwords VALUES (?, ?, ?, ?)', (platform.lower(), username, encrypted_password, key))
            self.conn.commit()

            print(f"\nSuccessfully saved password for {platform}")
        except:
            print(f"\nUnable to save password for {platform}")

    def retrievePassword(self, platform) -> bool:
        try:
            for row in self.cursor.execute('SELECT password, username, key FROM passwords WHERE platform = ?', (platform.lower(),)):
                row_items = row

            fnet = Fernet(row_items[2])
            username = row_items[1]
            password = fnet.decrypt(row_items[0])

            print(f"\nPlatform: {platform}\nUsername: {username}\nPassword: {password.decode()}")

            return True
        except:
            print("\nNo platform with this name found\n")
            return False

    # TODO update password