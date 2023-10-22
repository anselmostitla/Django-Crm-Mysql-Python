import mysql.connector

dataBase = mysql.connector.connect(
  host =  'localhost',
  user = 'root',
  passwd = 'Mysql100#',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print(f"All done!")

