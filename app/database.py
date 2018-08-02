"""Database config file"""
from datetime import date
import psycopg2
import os
from app import APP
from app.model import tables


class Database:
    """class with database configurtions"""

    def __init__(self):
        if not APP.config['TESTING']:
            DATABASE_URL = os.environ["DATABASE_URL"]
            self.con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = self.con.cursor()
            cur.execute(tables.USERTABLE,)
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.DAIRYTABLE,)
            self.con.commit()
        else:
            self.con = psycopg2.connect(host="localhost", user="postgres",
                                        password="chaos", dbname="test_db")
            cur = self.con.cursor()
            cur.execute(tables.USERTABLE, )
            self.con.commit()
            today = str(date.today())
            cur.execute("""INSERT INTO Users(firstname, lastname, username, password, gender)
            VALUES ('Dumba', 'kenneth', 'joy', '12345678', 'male')""")
            self.con.commit()
            cur = self.con.cursor()
            cur.execute(tables.DAIRYTABLE, )
            self.con.commit()
            cur.execute("""INSERT INTO Entries(title, body, entry_date, entry_time,
                        updated, user_id)VALUES('Testing', 'testing data', %s,
                        '3:00', '---', 1)""", (today, ))
            self.con.commit()

    @classmethod
    def testing_db_teardown(cls):
        """method to delete tables after testing"""
        con = psycopg2.connect(host="localhost", user="postgres",
                               password="chaos", dbname="test_db")
        return con

    def closedb(self):
        """method to close db connection"""
        self.con.close()

D = Database()
