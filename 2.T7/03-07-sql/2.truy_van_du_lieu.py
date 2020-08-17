import MySQLdb

dbServer = '34.87.120.250'
dbUser = 'dichthuat'
dbPass = 'quangloan17'
dbName = 'datapro'

db = MySQLdb.connect(dbServer,
        dbUser,dbPass,dbName,charset='utf8')

cursor = db.cursor()

try:
   cursor.execute("SELECT name, address FROM STUDENT")
   results = cursor.fetchall()

   for name, address in results:
            print(name, address)
                
except Exception as e:
  print(str(e))

db.close()
