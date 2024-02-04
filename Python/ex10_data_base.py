# 10. Create a table in postgres, fill it with data and print some of it

import psycopg2

class DataBase:
    def __init__(self):        
        self.conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "toster1111", port = 5432)
        self.curs = self.conn.cursor()
        print("Connected successfully")

    def create_table(self):
        self.curs.execute("""CREATE TABLE IF NOT EXISTS person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
        );
        """)
        print("Table created")

    def instert_data_into_table(self):
        self.curs.execute("""INSERT INTO person (id, name, age, gender) VALUES
        (1, 'Mike', 30, 'm'),
        (2, 'John', 24, 'm'),
        (3, 'Lisa', 36, 'f'),
        (4, 'Jane', 28, 'f'),
        (5, 'Paul', 31, 'm');                                 
        """)
        print("Data inserted")

    def select_data_from_table(self):
        self.curs.execute("""SELECT * FROM person WHERE age >= 30""")
        print("Data selected")

    def delete_table(self):
        self.curs.execute("""DROP TABLE person""")
        print("Table deleted")

    def print_data_to_terminal(self):
        print("Chosen data:")
        for row in self.curs.fetchall():
            print(row)

    def perform_and_close(self):
        self.conn.commit()
        self.curs.close()
        self.conn.close()

if __name__ == "__main__":
    try:
        data_base = DataBase()
        action = False
        if action:
            data_base.create_table()
            data_base.instert_data_into_table()
            data_base.select_data_from_table()
            data_base.print_data_to_terminal()
        else:
            data_base.delete_table()
        data_base.perform_and_close()
    except Exception as error:
        print(f"Error!!, program shut down due to {error}")