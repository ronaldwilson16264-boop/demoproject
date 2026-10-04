import mysql.connector




# Creating table
con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="school_db1"
)

c = con.cursor()


c = con.cursor()

query = """create table student(
            roll_no int not null primary key,
            name varchar(20),
            age int,
            place varchar(20),
            phone varchar(20),
            total_mark int)""";

c.execute(query)
print("Table Created")