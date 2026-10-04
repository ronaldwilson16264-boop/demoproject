import mysql.connector

con = mysql.connector.connect(user="root", password="root", host="localhost")

print(con)


# cursor object --for executing sql queries
c = con.cursor()



#query for creating a db 
query = "create database school_db1"
c.execute(query)

print("Database file created")
c.close()
con.close()

