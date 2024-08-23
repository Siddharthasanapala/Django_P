import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql@1234'
)

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE db")

print('ALL Done!')
