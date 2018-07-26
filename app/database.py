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
                    cur=self.con.cursor()
                    cur.execute(tables.DAIRYTABLE,)
                    self.con.commit()
                   
                else:
                    pass
                   
    def closedb(self):
            self.con.close()  

d = Database()                     