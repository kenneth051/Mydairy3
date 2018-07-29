from app import APP
from app.model import tables
import psycopg2

class Database:
    def __init__(self):
            if not APP.config['TESTING']:
                self.con = psycopg2.connect( host ="localhost",user = "postgres", password = "chaos", dbname = "diary")
                cur=self.con.cursor()
                cur.execute(tables.USERTABLE,)
                self.con.commit()
                cur=self.con.cursor()
                cur.execute(tables.DAIRYTABLE,)
                self.con.commit()
            else:
                self.con = psycopg2.connect( host ="localhost",user = "postgres", password = "chaos", dbname = "test_db")
                print("now testing")  
                if self.con:
                    cur=self.con.cursor()
                    cur.execute(tables.USERTABLE,)
                    self.con.commit()
                    cur.execute("INSERT INTO Users(firstname, lastname, username, password,gender)VALUES ('Dumba', 'kenneth', 'joy', '12345678', 'male')")
                    self.con.commit()
                    cur=self.con.cursor()
                    cur.execute(tables.DAIRYTABLE,)
                    self.con.commit()
                    cur.execute("INSERT INTO Entries(title,body,entry_date,entry_time,updated,user_id)VALUES\
                    ('Testing','testing data','28/1/2018','3:00','---',1)")      
                    self.con.commit()
                else:
                    pass
    @classmethod               
    def testing_db_teardown(cls):
        con = psycopg2.connect( host ="localhost",user = "postgres", password = "chaos", dbname = "test_db")
        return con
                       
    def closedb(self):
            self.con.close()  

d = Database()                     