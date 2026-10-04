import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="school_db1"
)

c = con.cursor()

query = "insert into student(roll_no, name, age, place, phone, total_mark) values(%s, %s, %s, %s, %s, %s)"
data = (101, "arun", 11, "ekm", "7889776667", 145)

c.execute(query, data)

con.commit()  # permanently saves data into database
print("Inserted data successfully")

c.close()
con.close()