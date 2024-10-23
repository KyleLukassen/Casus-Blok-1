import mysql.connector

#Verbinding maken met de database
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=input('Enter your database password: '),
    database="mydatabase"
)

#cursor om door de database te kunnen lopen
mycursor = mydb.cursor()

#databases ophalen
mycursor.execute("SHOW DATABASES")

#print de inhoud van de database
for x in mycursor:
  print(x)



