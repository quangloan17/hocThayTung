import MySQLdb

dbServer = '127.0.0.1'
dbUser = 'quangcvn'
dbPass = '270588'
dbName = 'quangcvn'

db = MySQLdb.connect(dbServer,
        dbUser,dbPass,dbName,charset='utf8')

cursor = db.cursor()

try:
  cursor.execute('''INSERT INTO STUDENT(name,address)
                    VALUES ('Nguyen Van An', 'Ha Noi')''')
                                         
  cursor.execute('''INSERT INTO STUDENT(name,address)
                    VALUES ('Nguyen Thi Binh', 'TP.HCM')''')
                                         
  db.commit()
except Exception as e:
  print(str(e))
  db.rollback()

db.close()

print('sucess')