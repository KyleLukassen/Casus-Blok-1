import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="UPGL4eC&mSHXT%9mQZ8P",
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)



