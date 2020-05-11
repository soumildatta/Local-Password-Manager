import sqlite3 
import hashing
import database

data = database.Database()

conn = sqlite3.connect('database.db')

# create cursor object 
c = conn.cursor()

# sql queries
# c.execute(''' CREATE TABLE passwords (
#         platform text, 
#         username text, 
#         hashed_password text, 
#         key text
#     )''')

# password = hashing.hashPassword("hello")
# print(hashing.verifyPassword(password, "hello"))

#! master password
# c.execute("INSERT INTO passwords VALUES ('none', 'master_pass', ?, '0000')", (password,))
# conn.commit()
data.createTable()
# data.createMasterPass("heythere")

#! Store platform
# data.storePassword("Mozilla", "someone", "testing")

#! Retrieve 
# print(data.retrievePassword("jit"))

# data = database.Database()
# print(data.checkMasterPass("hello"))

conn.close()