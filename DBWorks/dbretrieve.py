import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="school_db1"
)

print(con)

c = con.cursor()

query = "select * from student where roll_no=%s"
data = (102,)

c.execute(query, data)

record = c.fetchone()

if record:
    print(record)
else:
    print("No Record Found")

c.close()
con.close()