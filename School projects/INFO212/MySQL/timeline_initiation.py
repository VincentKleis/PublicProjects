import mysql.connector

mydb = mysql.connector.connect(             #connects to the mysql host
    host="DESKTOP-1K5P67D",
    user="root",
    password='deNAKScL5jHy'                 #change string to the password you set in the mysql settup
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE timeline")    #creates a database called timeline
mycursor.execute("USE timeline")                #enters the database

mycursor.execute("CREATE TABLE USER(\n\
mail VARCHAR(300),\n\
hashed_passwords VARCHAR(1000),\n\
admin BOOL,\n\
f_name VARCHAR(100),\n\
l_name VARCHAR(100),\n\
PRIMARY KEY (mail)\n\
)")

mycursor.execute("CREATE TABLE EVENT(\n\
event_name VARCHAR(200)\n\
event_description LONGTEXT,\n\
event_place VARCHAR(255),\n\
event_duration CHAR(29),\n\
event_source_links VARCHAR(9999),\n\
event_id VARCHAR(700),\n\
added_by VARCHAR(300),\n\
PRIMARY KEY (event_id),\n\
FOREIGN KEY (added_by) REFERENCES USER(mail)\n\
)")                             #tids format "(AD/BC) yyyy/mm/dd - (AD/BC) yyyy/mm/dd"
                                #sted format "land/(region/stat)/by"
                                #event_id er en kombinasjon mellom "event_"-"duration"&"place"

mycursor.execute("CREATE TABLE DATES(\
start_year CHAR(4),\n\
start_month CHAR(2),\n\
start_day CHAR(2),\n\
stop_year CHAR(4),\n\
stop_mont CHAR(2),\n\
stop_day CHAR(2),\n\
event_id VARCHAR(300),\n\
FOREIGN KEY (event_id) REFERENCES EVENT(event_id)\n\
)")