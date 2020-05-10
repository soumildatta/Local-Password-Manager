import sqlite3 

conn = sqlite3.connect('testing.db')

# create cursor object 
c = conn.cursor()

# sql queries
# c.execute(''' CREATE TABLE passwords (
#         platform text, 
#         username text, 
#         hashed text, 
#         salt text
#     )''')

# c.execute("INSERT INTO passwords VALUES ('Chrome', 'hellothere', 'ahofiefiahe8f9oqi3#$1$ohfs0', 'f7*')")
# conn.commit()

for row in c.execute("SELECT * FROM passwords"):
    rowed = row[2]

print(rowed)

conn.close()