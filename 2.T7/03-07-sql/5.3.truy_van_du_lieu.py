import MySQLdb

dbServer = '127.0.0.1'
dbUser = 'quangcvn'
dbPass = '270588'
dbName = 'quangcvn'

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
