"""Diary class"""
from datetime import date, datetime
from flask import jsonify
from app.validation1 import Validate
from app.database import Database


class Diary(Database):
    """class with diary attributes"""

    def __init__(self):
        """initializing constructor"""
        Database.__init__(self)

    def creating_entry(self,title1,body1,user_id1):
        try:
            today = str(date.today())
            current_time = str(datetime.time(datetime.now()))
            cur=self.con.cursor()               
            cur.execute("SELECT * FROM Entries where title = %s and body = %s and user_id = %s",(title1,body1,user_id1))
            self.con.commit()
            result=cur.rowcount
            if result>0:
                response = jsonify({"message":"Entry has been created previously,Duplicate data"})
                response.status_code =409
                return response
            else:   
                cur.execute("INSERT INTO Entries(title,body,entry_date,entry_time,updated,user_id)VALUES\
                (%s,%s,%s,%s,%s,%s)",(title1,body1,today,current_time,"---",user_id1))      
                self.con.commit()
                response = jsonify({"message":"Entry has been created successfully"})
                response.status_code =201
                return response
        except:
            response = jsonify({"message":"Entry cannot be created, contact ADMIN"})
            response.status_code =400
            return response
   
    def all_entries(self,user_id1):
        """method to get all entries"""
        cur=self.con.cursor()
        cur.execute("SELECT * FROM  Entries WHERE user_id = %s",(user_id1,));
        affected=cur.rowcount
        if affected >0: 
            result=cur.fetchall()
            lst=[]
            for row in result:
                data={}
                data["id"]= row[0]
                data["title"]=row[1]
                data["body"]=row[2]
                data["entry_time"]=row[3]
                data["entry_date"]=row[4]
                data["updated"]=row[5]
                data["user_id"]=row[6]
                lst.append(data)
            return jsonify({"result": lst})

    def single_entry(self, entryid ,user_id1):
        """method to get single entry"""
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Entries where id = %s and user_id = %s",(entryid, user_id1));
        affected=cur.rowcount
        result=cur.fetchall()
        if affected >0: 
            data={}
            lst=[]
            for row in result:
                data["id"]= row[0]
                data["title"]=row[1]
                data["body"]=row[2]
                data["entry_time"]=row[3]
                data["entry_date"]=row[4]
                data["updated"]=row[5]
                data["user_id"]=row[6]
                lst.append(data)
            return jsonify({"result": lst})
        else:
            response = jsonify({"message":"The URL is invalid ,wrong ID given"})
            response.status_code = 404
            return response 
