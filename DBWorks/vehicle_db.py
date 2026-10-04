import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con = mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            database="vehicle_db"
        )
        self.cursor = self.con.cursor()
        print("Successfully connected")

    def list(self):
        query = "select * from vehicle"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records Found")

    def create(self, brand, model, type, price, year):
        query = "insert into vehicle(brand, model, type, price, year) values(%s, %s, %s, %s, %s)"
        data = (brand, model, type, price, year)
        self.cursor.execute(query, data)
        self.con.commit()
        print("Inserted Data Successfully")

    def retrieve(self, id):
        query = "select * from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("No record found")

    def delete(self, id):
        query = "delete from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print("deleted data successfully")
        else:
            print("No record found")

    def update(self, id, brand, model, type, price, year):
        query = "update vehicle set brand=%s, model=%s, type=%s, price=%s, year=%s where id=%s"
        data = (brand, model, type, price, year, id)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            print("Updated Data successfully")
        else:
            print("No record found")

v = VehicleListCreateRetrieveUpdateDelete()
# v.list()
# v.create(brand='Toyota', model="Corolla", type="Sedan", price=20000, year=2023)
# v.retrieve(1)
# v.delete(1)
# v.update(id=1, brand="Toyota", model="Camry", type="Sedan", price=25000, year=2024)