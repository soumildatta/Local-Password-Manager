import sqlite3
import hashing

class Database:
    
    def __init__(self):
        conn = sqlite3.connect('database.db')
        self.cursor = conn.cursor()

    def checkMasterPass(self, master_password):
        for row in self.cursor.execute('SELECT hashed_password FROM passwords WHERE username = "master_pass"'):
            password = row[0]

        # entered_password = hashing.hashPassword(self.master_password)
        check = hashing.verifyPassword(password, master_password)

        return check