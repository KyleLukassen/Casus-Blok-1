import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=input('Enter your database password: '),
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)



