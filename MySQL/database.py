import mysql.connector

config  = {
    'user' : 'root',
    'password': '',
    'host': 'localhost',
    'database': 'pysql'
}
db = mysql.connector.connect(**config)

cursor = db.cursor()