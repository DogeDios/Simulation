import mysql.connector

class DB():
    def __init__(self):
        self.mysql_conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="o863454681",
            database="Simulation")
        self.mysql_cursor = self.mysql_conn.cursor()

    def create_person(self, name, lastname, age, birthdate, height, picture):
        query = """
        INSERT INTO Person (Name, Lastname, age, birthdate, height, picture)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (name, lastname, age, birthdate, height, picture)
        self.mysql_cursor.execute(query, values)
        self.mysql_conn.commit()

    # Function to read a person by ID
    def read_person(self, person_id):
        query = "SELECT * FROM Person WHERE id = %s"
        self.mysql_cursor.execute(query, (person_id,))
        result = self.mysql_cursor.fetchone()
        return result

    # Function to update a person by ID
    def update_person(self, person_id, name, lastname, age, birthdate, height, picture):
        query = """
        UPDATE Person
        SET Name = %s, Lastname = %s, age = %s, birthdate = %s, height = %s, picture = %s
        WHERE id = %s
        """
        values = (name, lastname, age, birthdate, height, picture, person_id)
        self.mysql_cursor.execute(query, values)
        self.mysql_conn.commit()

    # Function to delete a person by ID
    def delete_person(self, person_id):
        query = "DELETE FROM Person WHERE id = %s"
        self.mysql_cursor.execute(query, (person_id,))
        self.mysql_conn.commit()

    def close_connection(self):
        self.mysql_cursor.close()
        self.mysql_conn.close()

# # Example usage:
# db = DB()
# #db.create_person("John", "Doe", 30, "1993-09-15", 175.5, b'\x00\x01\x02\x03')
# result = db.read_person(2)
# print(result)
# #db.update_person(1, "Updated John", "Updated Doe", 31, "1992-09-15", 178.0, b'\x01\x02\x03\x04')
# #db.delete_person(1)
# db.close_connection()
