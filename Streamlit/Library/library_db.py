import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con = mysql.connector.connect(
            user="root", password="root", host="localhost", database="library_db"
        )
        self.cursor = self.con.cursor()
        print("Successfully connected")

    def list(self):
        query = "select * from book"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            return records
        else:
            return []











        

    def create(self, title, author, price, pages, language):
        query = "insert into book(title, author, price, pages, language) values(%s, %s, %s, %s, %s)"
        data = (title, author, price, pages, language)
        self.cursor.execute(query, data)
        self.con.commit()
        print("Inserted Data Successfully")

    def retrieve(self, id):
        query = "select * from book where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        record = self.cursor.fetchone()
        if record:
            return record
        else:
            return None





        

    def delete(self, id):
        query = "delete from book where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.con.commit()
        return self.cursor.rowcount > 0









    def update(self, id, title, author, price, pages, language):
        query = "update book set title=%s, author=%s, price=%s, pages=%s, language=%s where id=%s"
        data = (title, author, price, pages, language, id)
        self.cursor.execute(query, data)
        self.con.commit()
        return self.cursor.rowcount > 0