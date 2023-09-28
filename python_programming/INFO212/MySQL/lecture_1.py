import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="company"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

mydb.close()