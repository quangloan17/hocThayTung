import MySQLdb

dbServer = '34.87.120.250'
dbUser = 'dichthuat'
dbPass = 'quangloan17'
dbName = 'datapro'

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