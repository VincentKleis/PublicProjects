import mysql.connector
from hashlib import sha256

class loggin:
    mydb = None
    mycursor = None

    def __init__(self):
        self.mydb = mysql.connector.connect(             #connects to the mysql host
        host="DESKTOP-1K5P67D",                     #change hostename to the name of your server host
        user="root",
        password='deNAKScL5jHy'                     #change string to the password you set in the mysql settup
        )  
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE timeline')


    def register(self, admin:bool):
        mail = input("Mail: ")
        password = input("Password: ")      #input the pasword and mail
        f_name = input("First name: ")
        l_name = input("Last name: ")

        hash = password.encode()            #encodes the pasword string
        h = sha256()
        h.update(hash)                      #hashes the encoded string
        hash = h.hexdigest()     

        self.mycursor.execute(f"INSERT INTO user (mail, hashed_passwords, admin, f_name, l_name)\
            VALUES ('{mail}', '{hash}', {admin}, '{f_name}', '{l_name}');")
    
    def log_inn(self):
        mail = input("Mail: ")
        pas_to_match = self.mycursor.execute(f"SELECT hashed_passwords\
            FROM user\
            WHERE mail='{mail}'")
        password = input('Password: ')
        hash = password.encode()            
        h = sha256()
        h.update(hash)                      
        hash = h.hexdigest() 
        if pas_to_match == hash:
            print("sucsessfull loggin")
        else:
            print("your mail and pasword do not seem to match the mail and pasword registered")
        
        
        

test = loggin()
test.register(0)
output = test.mycursor.execute("USE timeline;\
SELECT mail, hashed_passwords FROM user;")
print(output)
