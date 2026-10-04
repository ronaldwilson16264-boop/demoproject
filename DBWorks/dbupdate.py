import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="school_db1"
)

c = con.cursor()

query = "update student set name=%s where roll_no=%s"
data = ('amal', 101)

c.execute(query, data)
con.commit()

if c.rowcount > 0:
    print('record updated')
else:
    print('no record found')

c.close()
con.close()