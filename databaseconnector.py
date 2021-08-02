import mysql.connector
import time
con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"

)
cursor=con.cursor()
inputword=input("Enter a word\n")
query=cursor.execute("SELECT * FROM Dictionary WHERE Expression= '%s' " % inputword)
results=cursor.fetchall()

for result in results:
    if result:
     print(result[1])
    else :print("Word not found")

# query = cursor.execute("SELECT Definition   FROM Dictionary WHERE Expression LIKE 'r%' ")