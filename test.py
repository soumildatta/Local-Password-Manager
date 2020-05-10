import sqlite3 
import hashing
import database

conn = sqlite3.connect('database.db')

# create cursor object 
c = conn.cursor()

# sql queries
# c.execute(''' CREATE TABLE passwords (
#         platform text, 
#         username text, 
#         hashed_password text 
#     )''')

# password = hashing.hashPassword("hello")
# print(hashing.verifyPassword(password, "hello"))


# c.execute("INSERT INTO passwords VALUES ('none', 'master_pass', ?)", (password,))
# conn.commit()

# print(rowed)
for row in c.execute('SELECT hashed_password FROM passwords WHERE username = "master_pass"'):
    print(row[0])

data = database.Database()
print(data.checkMasterPass("hello"))

conn.close()