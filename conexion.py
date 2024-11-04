import mysql.connector 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #port = 3306,
    #database = "mysql"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASES")
#cursor.execute("SHOW DATABASES")

#for db in cursor:
#    print(db)

conn.close()