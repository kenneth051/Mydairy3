"""file with table sql"""

USERTABLE = """create table IF NOT EXISTS Users (id serial
            primary key not null,firstname text not null,
                    lastname text not null, username text
                    not null,password text not null,
                    gender text not null)"""

DAIRYTABLE = """create table IF NOT EXISTS Entries
             (id serial primary key not null,title 
              text not null,body text not null, 
              entry_time text not null,entry_date text not null,
                    updated text not null,user_id int references Users(id))"""
